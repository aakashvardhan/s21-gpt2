
# Tiny Shakespeare GPT-2


## Introduction

This is a tiny GPT-2 model trained on Shakespeare's works. It is a smaller version of the original GPT-2 model, with 124M parameters, trained on a mixture of Shakespeare's plays and sonnets. This is adapted from Andrej Karpathy's [nanoGPT](https://github.com/karpathy/nanoGPT/tree/master) and youtube video [here](https://youtu.be/l8pRSuU81PU?si=ta5pJsj1eeQR5-Dm).

## Roadmap

### Model Architecture Optimizations

- [x] Overfit a single batch of data
  - Ensures the model can learn from a small dataset before scaling up
- [x] Added Weight Tying/Sharing
  - The embedding layer and the final linear layer share weights, reducing parameters
- [x] Override the vocab size to 50304
  - Aligns with power of 2 for potential performance benefits

### Data Handling and Processing

- [x] Created a DataloaderLite Class
  - Custom dataloader for efficient data feeding to the model

### Training Optimizations

- [x] Using model initialization with std = 0.02 and residual pathways init
  - Improves training stability and convergence
- [x] Setting the model to use tf32 precision at high
  - Balances speed and accuracy for NVIDIA GPUs
- [x] Switched to CUDA and trained the model with bf16 precision
  - Further optimizes training speed on compatible hardware
- [x] Added torch.compile() to speed up model training
  - JIT compilation for faster execution
- [x] Added Flash Attention to the model
  - Addresses memory bottleneck, improving efficiency for large models

### Optimizer and Learning Rate Adjustments

- [x] Modified AdamW beta parameters to 0.9 and 0.95 and eps to 1e-8
  - Fine-tuned optimizer settings for better convergence
- [x] Added gradient clipping of 1.0 to the model
  - Prevents exploding gradients during training
- [x] Added a learning rate scheduler to the model: warmup + cosine decay
  - Improves training stability and final model performance
- [x] Added Fused implementation of AdamW
  - Weight decay for 2D tensors (matmul + embedding), 1D tensors without weight decay
  - Optimizes memory usage and computation

### Performance Monitoring

- [x] Calculating time taken to train the model
  - Synchronize GPU to wait for model to finish training at tf32 precision
- [x] Calculating the number of tokens processed per second
  - Measures training efficiency and throughput