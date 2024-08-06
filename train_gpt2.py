from dataclasses import dataclass
import torch
import torch.nn as nn
from torch.nn import functional as F
import math
import tiktoken

# --------------------------------------------------------------------------------------------------------


class CausalSelfAttention(nn.Module):

    def __init__(self, config):
        super().__init__()
        assert config.n_embd % config.n_head == 0
        # key, query, value projections for all heads, but in a batch
        self.c_attn = nn.Linear(config.n_embd, 3 * config.n_embd)
        # output projection
        self.c_proj = nn.Linear(config.n_embd, config.n_embd)
        self.c_proj.NANOGPT_SCALE_INIT = 1
        # regularization
        self.n_head = config.n_head
        self.n_embd = config.n_embd
        # not really a 'bias', more of a mask, but following the OpenAI/HF naming though
        self.register_buffer(
            "bias",
            torch.tril(
                torch.ones(config.block_size, config.block_size).view(
                    1, 1, config.block_size, config.block_size
                )
            ),
        )

    def forward(self, x):
        B, T, C = (
            x.size()
        )  # batch size, sequence length, embedding dimensionality (n_embd)
        # calculate query, key, values for all heads in batch and move head forward to be the batch dim
        # nh is the number of heads, hs is the head size, C is the number of channels = nh * hs
        # e.g, in GPT-2 (124M), n_heads = 12, head_size = 64, C = 12 * 64 = 768 channels in the transformer
        qkv = self.c_attn(x)
        q, k, v = qkv.split(self.n_embd, dim=2)
        k = k.view(B, T, self.n_head, C // self.n_head).transpose(
            1, 2
        )  # (B, nh, T, hs)
        q = q.view(B, T, self.n_head, C // self.n_head).transpose(
            1, 2
        )  # (B, nh, T, hs)
        v = v.view(B, T, self.n_head, C // self.n_head).transpose(
            1, 2
        )  # (B, nh, T, hs)
        # attention (materializes the large (T, T) attention matrix for all the queries and keys)
        # T is the sequence length, so we attend over the full sequence
        att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(k.size(-1)))
        att = att.masked_fill(self.bias[:, :, :T, :T] == 0, float("-inf"))
        att = F.softmax(att, dim=-1)
        y = att @ v  # (B, nh, T, T) x (B, nh, T, hs) -> (B, nh, T, hs)
        y = (
            y.transpose(1, 2).contiguous().view(B, T, C)
        )  # re-assemble all head outputs side by side
        y = self.c_proj(y)
        return y


class MLP(nn.Module):

    def __init__(self, config):
        super().__init__()
        self.c_fc = nn.Linear(config.n_embd, 4 * config.n_embd)
        self.gelu = nn.GELU(approximate="tanh")
        self.c_proj = nn.Linear(4 * config.n_embd, config.n_embd)
        self.c_proj.NANOGPT_SCALE_INIT = 1

    def forward(self, x):
        x = self.gelu(self.c_fc(x))
        x = self.c_proj(x)
        return x


class Block(nn.Module):

    def __init__(self, config):
        super().__init__()
        self.ln_1 = nn.LayerNorm(config.n_embd)
        self.attn = CausalSelfAttention(config)
        self.ln_2 = nn.LayerNorm(config.n_embd)
        self.mlp = MLP(config)

    def forward(self, x):
        x = x + self.attn(self.ln_1(x))
        x = x + self.mlp(self.ln_2(x))
        return x


@dataclass
class GPTConfig:
    block_size: int = 1024  # max sequence length
    vocab_size: int = (
        50257  # number of tokens: 50,000 BPE merges + 256 bytes tokens + 1 <|endoftext|> token which delimits the end of a text
    )
    n_layers: int = 6  # number of layers
    n_head: int = 6  # number of heads
    n_embd: int = 6  # embedding dimension


class GPT(nn.Module):

    def __init__(self, config: GPTConfig):
        super().__init__()
        self.config = config

        self.transformer = nn.ModuleDict(
            dict(
                wte=nn.Embedding(config.vocab_size, config.n_embd),
                wpe=nn.Embedding(config.block_size, config.n_embd),
                h=nn.ModuleList([Block(config) for _ in range(config.n_layers)]),
                ln_f=nn.LayerNorm(config.n_embd),
            )
        )
        self.lm_head = nn.Linear(config.n_embd, config.vocab_size, bias=False)

        # weight sharing scheme
        # the weights of the embedding layer are shared with the weights of the pre-softmax linear transformation
        self.transformer.wte.weight = self.lm_head.weight

        # initialize the weights
        self.apply(self._init_weights)

    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            std = 0.02
            if hasattr(module, "NANOGPT_SCALE_INIT"):
                std *= (2 * self.config.n_layers) ** -0.5 # multiply by 2 comes from the fact that we have two sub-layers in the block(attention and mlp)
            torch.nn.init.normal_(module.weight, mean=0.0, std=std)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)  # set bias to zero
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def forward(self, idx, targets=None):
        # idx is of shape (B, T) where T is the length of the sequence
        B, T = idx.size()
        assert (
            T <= self.config.block_size
        ), f"Cannot forward, model block size is exhausted. Got {T} but configured for {self.config.block_size}"
        # forward the token and position embeddings
        pos = torch.arange(T, dtype=torch.long, device=idx.device)  # (T)
        pos_emb = self.transformer.wpe(
            pos
        )  # positional embeddings of shape (T, n_embd)
        tok_emb = self.transformer.wte(idx)  # token embeddings of shape (B, T, n_embd)
        x = (
            tok_emb + pos_emb
        )  # combined embeddings (we could also use a layer norm here)
        # forward the blocks of the transformer
        for block in self.transformer.h:
            x = block(x)
        # forward the blocks of the transformer
        x = self.transformer.ln_f(x)
        logits = self.lm_head(x)  # (B, T, vocab_size)
        loss = None

        if targets is not None:
            loss = F.cross_entropy(
                logits.view(-1, logits.size(-1)), targets.view(-1)
            )  # flatten all the logits and the targets

        return logits, loss

    @classmethod
    def from_pretrained(cls, model_type):
        """Loads pretrained GPT-2 model from Hugging Face"""
        assert model_type in {"gpt2", "gpt2-medium", "gpt2-large", "gpt2-xl"}
        from transformers import GPT2LMHeadModel

        print(f"Loading model {model_type} from Hugging Face")

        # n_layer, n_head, n_embd are determined by the model_type
        config_args = {
            "gpt2": dict(n_layers=12, n_head=12, n_embd=768),  # 124M parameters
            "gpt2-medium": dict(n_layers=24, n_head=16, n_embd=1024),  # 350M parameters
            "gpt2-large": dict(n_layers=36, n_head=20, n_embd=1280),  # 774M parameters
            "gpt2-xl": dict(n_layers=48, n_head=25, n_embd=1600),  # 1558M parameters
        }[model_type]
        config_args["vocab_size"] = 50257  # always 50257 for GPT model checkpoints
        config_args["block_size"] = 1024  # always 1024 for GPT model checkpoints
        # create a from-scratch initialized minGPT model
        config = GPTConfig(**config_args)
        model = GPT(config)
        sd = model.state_dict()
        sd_keys = sd.keys()
        sd_keys = [
            k for k in sd_keys if not k.endswith(".attn.bias")
        ]  # discard this mask / buffer key

        # init a huggingface/transformers model
        model_hf = GPT2LMHeadModel.from_pretrained(model_type)
        sd_hf = model_hf.state_dict()

        # copy while ensuring all of the parameters are aligned and match in names and shapes
        sd_keys_hf = sd_hf.keys()
        sd_keys_hf = [
            k for k in sd_keys_hf if not k.endswith(".attn.masked_bias")
        ]  # ignore these mask keys
        sd_keys_hf = [
            k for k in sd_keys_hf if not k.endswith(".attn.bias")
        ]  # ignore these mask keys
        transposed = [
            "attn.c_attn.weight",
            "attn.c_proj.weight",
            "mlp.c_fc.weight",
            "mlp.c_proj.weight",
        ]
        # basically the openai checkpoints use a "conv1d" module, but we only want to use a vanilla linear layer
        # this means we need to transpose the weight matrices
        assert len(sd_keys) == len(
            sd_keys_hf
        ), f"mismatch in number of keys: {len(sd_keys)} != {len(sd_keys_hf)}"
        for k in sd_keys_hf:
            if any(k.endswith(w) for w in transposed):
                # special treatment for the conv1d weight matrices that need to be transposed
                assert sd_hf[k].shape[::-1] == sd[k].shape
                with torch.no_grad():
                    sd[k].copy_(sd_hf[k].t())
            else:
                # vanilla copy operation for all other weights
                assert sd_hf[k].shape == sd[k].shape
                with torch.no_grad():
                    sd[k].copy_(sd_hf[k])

        return model


# --------------------------------------------------------------------------------------------------------
num_return_sequences = 5
max_length = 30


class DataLoaderLite:
    def __init__(self, B, T):
        self.B = B
        self.T = T

        # at init load tokens from disk and store then in the memory
        with open("./input.txt", "r") as f:
            text = f.read()
        enc = tiktoken.get_encoding("gpt2")
        tokens = enc.encode(text)
        self.tokens = torch.tensor(tokens)
        print(f"loaded {len(self.tokens)} tokens")
        print(f"1 epoch = {len(self.tokens) // (B * T)} batches")

        # state
        self.current_position = 0

    def next_batch(self):
        B, T = self.B, self.T
        buf = self.tokens[self.current_position : self.current_position + B * T + 1]
        x = buf[:-1].view(B, T)  # (B, T)
        y = buf[1:].view(B, T)  # (B, T)
        self.current_position += B * T  # move the position forward
        # if loading the next batch would go over the tokens, reset the position
        if self.current_position + (B * T + 1) > len(self.tokens):
            self.current_position = 0

        return x, y


# attempt to autodetect the device
import time


device = "cpu"
if torch.cuda.is_available():
    device = "cuda"
elif hasattr(torch, "mps") and torch.backends.mps.is_available():
    device = "mps"

print(f"Using device: {device}")


torch.manual_seed(1337)
if torch.cuda.is_available():
    torch.cuda.manual_seed(1337)
elif hasattr(torch, "mps") and torch.backends.mps.is_available():
    torch.mps.manual_seed(1337)

# get a data batch
train_loader = DataLoaderLite(16,1024)
torch.set_float32_matmul_precision('high')
# the exponent sets the precision of the matrix multiplication

model = GPT(GPTConfig())
model.to(device)
# logits, loss = model(x, y)

# print(loss)  # (B, T, vocab_size) = (4, 32, 50257)
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)
for i in range(50):
    t0 = time.time()
    x, y = train_loader.next_batch()
    x, y = x.to(device), y.to(device)
    optimizer.zero_grad()
    with torch.autocast(device_type=device, dtype=torch.bfloat16):
        logits, loss = model(x, y)
        # import code; code.interact(local=locals())
    loss.backward()
    optimizer.step()
    torch.cuda.synchronize() # wait for the kernel to finish before measuring the time
    t1 = time.time()
    dt = (t1 - t0) * 1000 # in milliseconds
    tokens_per_sec = train_loader.B * train_loader.T / (t1 - t0) # number of tokens per second processed
    print(
        f"step {i}, loss: {loss.item()}, time: {dt:.2f} ms, tokens/sec: {tokens_per_sec:.2f}"
    )  # loss.item() converts the loss tensor to a scalar float 1D -> float internally in pytorch

import sys

sys.exit(0)
# sanity check the loss
# we should expect it to be very high since the model is randomly initialized
# and the targets are the next token in the sequence

# prefix tokens

# enc = tiktoken.get_encoding("gpt2")
# tokens = enc.encode("Hello, I'm a language model, and I can generate text")
# tokens = torch.tensor(tokens, dtype=torch.long)  # (8,)
# tokens = tokens.unsqueeze(0).repeat(num_return_sequences, 1)  # (5, 8)
# x = tokens.to(device)

# generate right now x is (B, T) where B = 5, T = 8
# set the seed to 42
# torch.manual_seed(42)
# torch.mps.manual_seed(42)
# while x.size(1) < max_length:
#     # forward the model to get the logits
#     with torch.no_grad():
#         logits = model(x)  # (B, T, voc ab_size)
#         # take the logits at the last position
#         logits = logits[:, -1, :]  # (B, vocab_size)
#         # get the probabilities
#         probs = F.softmax(logits, dim=-1)
#         # do top-k sampling of 50 (huggingface pipeline default)
#         # topk_probs here becomes (5, 50), topk_indices becomes (5, 50)
#         topk_probs, topk_indices = torch.topk(probs, 50, dim=-1)
#         # select a token from the top-k probabilities
#         ix = torch.multinomial(topk_probs, num_samples=1)  # (B, 1)
#         # gather the corresponding indices
#         xcol = torch.gather(topk_indices, -1, ix)  # (B, 1)
#         # append to the sequence
#         x = torch.cat((x, xcol), dim=1)

# # print the generated sequences
# for i in range(num_return_sequences):
#     tokens = x[i, :max_length].tolist()
#     decoded = enc.decode(tokens)
#     print(">", decoded)
