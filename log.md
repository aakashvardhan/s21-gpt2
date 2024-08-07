

Overfit a single batch of data

```
Using device: mps
step 0, loss: 10.899394989013672
step 1, loss: 10.719036102294922
step 2, loss: 9.968440055847168
step 3, loss: 9.226236343383789
step 4, loss: 8.359014511108398
step 5, loss: 7.292380332946777
step 6, loss: 6.059737682342529
step 7, loss: 5.028200149536133
step 8, loss: 4.337789535522461
step 9, loss: 3.7353901863098145
step 10, loss: 3.3103716373443604
step 11, loss: 3.0366311073303223
step 12, loss: 2.771650791168213
step 13, loss: 2.608070135116577
step 14, loss: 2.5165414810180664
step 15, loss: 2.420342445373535
step 16, loss: 2.279803514480591
step 17, loss: 2.187012195587158
step 18, loss: 2.035943031311035
step 19, loss: 1.870970368385315
step 20, loss: 1.71954345703125
step 21, loss: 1.586930751800537
step 22, loss: 1.4698750972747803
step 23, loss: 1.3565809726715088
step 24, loss: 1.248894214630127
step 25, loss: 1.1393696069717407
step 26, loss: 1.041056752204895
step 27, loss: 0.9740760326385498
step 28, loss: 0.891292154788971
step 29, loss: 0.8277447819709778
step 30, loss: 0.7795004844665527
step 31, loss: 0.7047560214996338
step 32, loss: 0.6074130535125732
step 33, loss: 0.5693652629852295
step 34, loss: 0.5064791440963745
step 35, loss: 0.4593380093574524
step 36, loss: 0.41031068563461304
step 37, loss: 0.36318719387054443
step 38, loss: 0.3214937448501587
step 39, loss: 0.28502658009529114
step 40, loss: 0.24368171393871307
step 41, loss: 0.21590185165405273
step 42, loss: 0.18931546807289124
step 43, loss: 0.16180768609046936
step 44, loss: 0.13912691175937653
step 45, loss: 0.11967606097459793
step 46, loss: 0.10034018754959106
step 47, loss: 0.08635707199573517
step 48, loss: 0.07231621444225311
step 49, loss: 0.06201247125864029
```

Using dataloaderlite to train a model

```
Using device: mps
loaded 338025 tokens
1 epoch = 2640 batches
step 0, loss: 10.959087371826172
step 1, loss: 10.610689163208008
step 2, loss: 10.070310592651367
step 3, loss: 9.76555061340332
step 4, loss: 8.978466033935547
step 5, loss: 8.123308181762695
step 6, loss: 8.350227355957031
step 7, loss: 8.284231185913086
step 8, loss: 7.465363502502441
step 9, loss: 7.708094120025635
step 10, loss: 7.912501335144043
step 11, loss: 7.087590217590332
step 12, loss: 7.369287014007568
step 13, loss: 6.9761199951171875
step 14, loss: 7.144923686981201
step 15, loss: 7.051121234893799
step 16, loss: 7.430870532989502
step 17, loss: 8.090654373168945
step 18, loss: 6.981069564819336
step 19, loss: 7.613379955291748
step 20, loss: 7.42721700668335
step 21, loss: 7.724188804626465
step 22, loss: 6.595221042633057
step 23, loss: 6.995755672454834
step 24, loss: 6.945620536804199
step 25, loss: 6.888222694396973
step 26, loss: 7.03505802154541
step 27, loss: 7.623309135437012
step 28, loss: 7.151457786560059
step 29, loss: 7.145349502563477
step 30, loss: 6.981725215911865
step 31, loss: 7.188508033752441
step 32, loss: 7.2151079177856445
step 33, loss: 7.170924663543701
step 34, loss: 8.022403717041016
step 35, loss: 7.836256980895996
step 36, loss: 7.637295246124268
step 37, loss: 7.729889869689941
step 38, loss: 7.944389820098877
step 39, loss: 7.460570812225342
step 40, loss: 7.50527811050415
step 41, loss: 6.997627258300781
step 42, loss: 7.102540493011475
step 43, loss: 7.107607841491699
step 44, loss: 6.9185309410095215
step 45, loss: 7.0374040603637695
step 46, loss: 6.319802761077881
step 47, loss: 6.525517463684082
step 48, loss: 7.10743522644043
step 49, loss: 6.971785545349121
```


Improving model with weight sharing

```
Using device: mps
loaded 338025 tokens
1 epoch = 2640 batches
step 0, loss: 11.080904006958008
step 1, loss: 10.733358383178711
step 2, loss: 10.351877212524414
step 3, loss: 10.082989692687988
step 4, loss: 9.462810516357422
step 5, loss: 8.657878875732422
step 6, loss: 8.426214218139648
step 7, loss: 7.927463531494141
step 8, loss: 7.441391468048096
step 9, loss: 8.125346183776855
step 10, loss: 8.855520248413086
step 11, loss: 7.112147331237793
step 12, loss: 7.62185001373291
step 13, loss: 7.0889105796813965
step 14, loss: 7.223770618438721
step 15, loss: 7.2259063720703125
step 16, loss: 7.444329738616943
step 17, loss: 8.163165092468262
step 18, loss: 6.923492431640625
step 19, loss: 7.649619102478027
step 20, loss: 7.438796043395996
step 21, loss: 7.787788391113281
step 22, loss: 6.654875755310059
step 23, loss: 6.947122573852539
step 24, loss: 6.940644264221191
step 25, loss: 6.813569068908691
step 26, loss: 6.903389930725098
step 27, loss: 7.630727291107178
step 28, loss: 7.019359111785889
step 29, loss: 6.948946952819824
step 30, loss: 6.922396659851074
step 31, loss: 7.0658674240112305
step 32, loss: 7.086988925933838
step 33, loss: 6.945941925048828
step 34, loss: 7.971220970153809
step 35, loss: 7.754841327667236
step 36, loss: 7.4936909675598145
step 37, loss: 7.522448539733887
step 38, loss: 7.643625736236572
step 39, loss: 7.314289093017578
step 40, loss: 7.3122782707214355
step 41, loss: 6.704894065856934
step 42, loss: 6.821822166442871
step 43, loss: 7.025929927825928
step 44, loss: 6.713400840759277
step 45, loss: 6.920466899871826
step 46, loss: 6.170239448547363
step 47, loss: 6.431720733642578
step 48, loss: 7.10091495513916
step 49, loss: 6.827264785766602
```

Using model initialization with std = 0.02 and residual pathways init

```
Using device: mps
loaded 338025 tokens
1 epoch = 2640 batches
step 0, loss: 10.823765754699707
step 1, loss: 10.582246780395508
step 2, loss: 10.05883502960205
step 3, loss: 9.503162384033203
step 4, loss: 8.640345573425293
step 5, loss: 7.619840621948242
step 6, loss: 8.048725128173828
step 7, loss: 8.263350486755371
step 8, loss: 7.78996467590332
step 9, loss: 8.250741958618164
step 10, loss: 8.615525245666504
step 11, loss: 6.81866979598999
step 12, loss: 7.309743404388428
step 13, loss: 7.276151657104492
step 14, loss: 7.188809394836426
step 15, loss: 7.016488075256348
step 16, loss: 7.562121391296387
step 17, loss: 8.325662612915039
step 18, loss: 6.8823418617248535
step 19, loss: 7.607054233551025
step 20, loss: 7.363595008850098
step 21, loss: 7.702338218688965
step 22, loss: 6.730830192565918
step 23, loss: 6.9982781410217285
step 24, loss: 6.882895469665527
step 25, loss: 6.825695991516113
step 26, loss: 7.046009540557861
step 27, loss: 7.827315330505371
step 28, loss: 7.141657829284668
step 29, loss: 7.012062072753906
step 30, loss: 6.851278305053711
step 31, loss: 7.09874153137207
step 32, loss: 7.222972869873047
step 33, loss: 7.081643104553223
step 34, loss: 8.025001525878906
step 35, loss: 7.891120910644531
step 36, loss: 7.529408931732178
step 37, loss: 7.59499454498291
step 38, loss: 7.743626594543457
step 39, loss: 7.4463019371032715
step 40, loss: 7.46870756149292
step 41, loss: 6.835247039794922
step 42, loss: 6.969829559326172
step 43, loss: 7.130365371704102
step 44, loss: 6.875461578369141
step 45, loss: 7.012744903564453
step 46, loss: 6.147722244262695
step 47, loss: 6.404941558837891
step 48, loss: 6.95660400390625
step 49, loss: 6.82475471496582
```


Calculating time taken to train the model and syncronize the gpu to wait for the model to finish training at tf32 precision
and calculating the number of tokens processed per second


```
Using device: mps
loaded 338025 tokens
1 epoch = 330 batches
step 0, loss: 10.826255798339844, time: 644.64 ms, tokens/sec: 1588.47
step 1, loss: 10.555530548095703, time: 101.84 ms, tokens/sec: 10054.87
step 2, loss: 10.052939414978027, time: 105.58 ms, tokens/sec: 9698.43
step 3, loss: 9.106203079223633, time: 105.08 ms, tokens/sec: 9744.57
step 4, loss: 8.660629272460938, time: 112.86 ms, tokens/sec: 9073.44
step 5, loss: 7.781713485717773, time: 110.06 ms, tokens/sec: 9304.26
step 6, loss: 7.224939346313477, time: 112.93 ms, tokens/sec: 9067.81
step 7, loss: 6.891262054443359, time: 106.32 ms, tokens/sec: 9631.48
step 8, loss: 7.056204795837402, time: 102.39 ms, tokens/sec: 10000.60
step 9, loss: 7.106714248657227, time: 101.67 ms, tokens/sec: 10071.70
step 10, loss: 6.96861457824707, time: 100.54 ms, tokens/sec: 10185.13
step 11, loss: 7.755661964416504, time: 98.37 ms, tokens/sec: 10409.67
step 12, loss: 6.778326034545898, time: 102.30 ms, tokens/sec: 10009.60
step 13, loss: 7.1150712966918945, time: 106.43 ms, tokens/sec: 9621.69
step 14, loss: 6.956608772277832, time: 101.11 ms, tokens/sec: 10127.39
step 15, loss: 6.798712253570557, time: 103.54 ms, tokens/sec: 9889.90
step 16, loss: 6.6381516456604, time: 102.81 ms, tokens/sec: 9960.11
step 17, loss: 6.688507080078125, time: 104.39 ms, tokens/sec: 9808.91
step 18, loss: 6.49716854095459, time: 113.38 ms, tokens/sec: 9031.94
step 19, loss: 6.676558494567871, time: 114.94 ms, tokens/sec: 8909.22
step 20, loss: 6.139944553375244, time: 107.11 ms, tokens/sec: 9560.45
step 21, loss: 6.696824073791504, time: 103.83 ms, tokens/sec: 9862.38
step 22, loss: 6.2066144943237305, time: 101.66 ms, tokens/sec: 10072.79
step 23, loss: 6.025382041931152, time: 105.54 ms, tokens/sec: 9702.85
step 24, loss: 6.290696620941162, time: 110.65 ms, tokens/sec: 9254.82
step 25, loss: 6.257389545440674, time: 103.98 ms, tokens/sec: 9848.34
step 26, loss: 6.333862781524658, time: 108.26 ms, tokens/sec: 9458.45
step 27, loss: 6.111874580383301, time: 98.22 ms, tokens/sec: 10425.56
step 28, loss: 6.279529571533203, time: 101.34 ms, tokens/sec: 10105.09
step 29, loss: 6.355197906494141, time: 100.73 ms, tokens/sec: 10165.99
step 30, loss: 6.300980567932129, time: 96.81 ms, tokens/sec: 10576.89
step 31, loss: 6.255526542663574, time: 98.14 ms, tokens/sec: 10433.77
step 32, loss: 6.609906196594238, time: 97.46 ms, tokens/sec: 10507.08
step 33, loss: 6.576773643493652, time: 100.79 ms, tokens/sec: 10159.33
step 34, loss: 6.464487552642822, time: 98.57 ms, tokens/sec: 10388.57
step 35, loss: 6.16191291809082, time: 97.59 ms, tokens/sec: 10493.09
step 36, loss: 6.079559803009033, time: 98.10 ms, tokens/sec: 10438.64
step 37, loss: 6.452757835388184, time: 100.62 ms, tokens/sec: 10176.42
step 38, loss: 5.982510089874268, time: 94.84 ms, tokens/sec: 10797.13
step 39, loss: 6.50678014755249, time: 96.34 ms, tokens/sec: 10628.58
step 40, loss: 6.466870307922363, time: 96.71 ms, tokens/sec: 10588.67
step 41, loss: 6.537384033203125, time: 98.26 ms, tokens/sec: 10421.64
step 42, loss: 6.331496715545654, time: 98.82 ms, tokens/sec: 10362.08
step 43, loss: 6.477449893951416, time: 98.39 ms, tokens/sec: 10407.48
step 44, loss: 6.4661054611206055, time: 97.17 ms, tokens/sec: 10538.37
step 45, loss: 6.444024562835693, time: 99.58 ms, tokens/sec: 10282.77
step 46, loss: 7.232758045196533, time: 97.13 ms, tokens/sec: 10543.03
step 47, loss: 6.997322082519531, time: 96.78 ms, tokens/sec: 10580.69
step 48, loss: 7.153199195861816, time: 97.67 ms, tokens/sec: 10483.87
step 49, loss: 7.082703590393066, time: 98.99 ms, tokens/sec: 10344.46
```


Setting the model to use tf32 precision at high 

```
Using device: mps
loaded 338025 tokens
1 epoch = 330 batches
step 0, loss: 10.826255798339844, time: 736.58 ms, tokens/sec: 1390.20
step 1, loss: 10.555530548095703, time: 102.95 ms, tokens/sec: 9947.05
step 2, loss: 10.052939414978027, time: 103.66 ms, tokens/sec: 9878.14
step 3, loss: 9.106203079223633, time: 122.14 ms, tokens/sec: 8383.83
step 4, loss: 8.660629272460938, time: 105.52 ms, tokens/sec: 9704.21
step 5, loss: 7.781713485717773, time: 131.95 ms, tokens/sec: 7760.58
step 6, loss: 7.224939346313477, time: 104.57 ms, tokens/sec: 9792.76
step 7, loss: 6.891262054443359, time: 102.67 ms, tokens/sec: 9974.15
step 8, loss: 7.056204795837402, time: 110.85 ms, tokens/sec: 9237.30
step 9, loss: 7.106714248657227, time: 100.53 ms, tokens/sec: 10186.22
step 10, loss: 6.96861457824707, time: 104.59 ms, tokens/sec: 9790.91
step 11, loss: 7.755661964416504, time: 106.64 ms, tokens/sec: 9602.24
step 12, loss: 6.778326034545898, time: 104.12 ms, tokens/sec: 9834.89
step 13, loss: 7.1150712966918945, time: 97.96 ms, tokens/sec: 10452.92
step 14, loss: 6.956608295440674, time: 104.55 ms, tokens/sec: 9794.05
step 15, loss: 6.798711776733398, time: 99.74 ms, tokens/sec: 10266.27
step 16, loss: 6.6381516456604, time: 109.71 ms, tokens/sec: 9333.70
step 17, loss: 6.688507080078125, time: 99.59 ms, tokens/sec: 10282.17
step 18, loss: 6.49716854095459, time: 98.05 ms, tokens/sec: 10443.13
step 19, loss: 6.676558494567871, time: 97.77 ms, tokens/sec: 10473.44
step 20, loss: 6.139944553375244, time: 98.20 ms, tokens/sec: 10427.28
step 21, loss: 6.696824073791504, time: 98.89 ms, tokens/sec: 10354.83
step 22, loss: 6.2066144943237305, time: 99.14 ms, tokens/sec: 10329.13
step 23, loss: 6.025382041931152, time: 100.74 ms, tokens/sec: 10164.47
step 24, loss: 6.290696620941162, time: 104.37 ms, tokens/sec: 9810.88
step 25, loss: 6.257389545440674, time: 99.15 ms, tokens/sec: 10327.89
step 26, loss: 6.333862781524658, time: 99.24 ms, tokens/sec: 10317.99
step 27, loss: 6.111874580383301, time: 100.12 ms, tokens/sec: 10227.62
step 28, loss: 6.279529571533203, time: 97.38 ms, tokens/sec: 10515.15
step 29, loss: 6.355198860168457, time: 97.63 ms, tokens/sec: 10488.58
step 30, loss: 6.300980567932129, time: 106.40 ms, tokens/sec: 9624.06
step 31, loss: 6.255526542663574, time: 97.57 ms, tokens/sec: 10494.63
step 32, loss: 6.6099066734313965, time: 97.93 ms, tokens/sec: 10456.43
step 33, loss: 6.576773643493652, time: 98.05 ms, tokens/sec: 10443.54
step 34, loss: 6.464478969573975, time: 98.42 ms, tokens/sec: 10404.60
step 35, loss: 6.161919593811035, time: 98.93 ms, tokens/sec: 10351.09
step 36, loss: 6.079485893249512, time: 101.43 ms, tokens/sec: 10095.54
step 37, loss: 6.452696323394775, time: 101.29 ms, tokens/sec: 10109.18
step 38, loss: 5.982548713684082, time: 103.10 ms, tokens/sec: 9932.33
step 39, loss: 6.505652904510498, time: 98.43 ms, tokens/sec: 10402.91
step 40, loss: 6.465283393859863, time: 98.59 ms, tokens/sec: 10385.93
step 41, loss: 6.538374423980713, time: 99.02 ms, tokens/sec: 10340.92
step 42, loss: 6.332828044891357, time: 98.89 ms, tokens/sec: 10355.23
step 43, loss: 6.477499485015869, time: 97.62 ms, tokens/sec: 10490.19
step 44, loss: 6.462174415588379, time: 101.87 ms, tokens/sec: 10051.83
step 45, loss: 6.442619323730469, time: 99.56 ms, tokens/sec: 10285.45
step 46, loss: 7.233522891998291, time: 98.74 ms, tokens/sec: 10370.68
step 47, loss: 6.99773645401001, time: 100.93 ms, tokens/sec: 10145.86
step 48, loss: 7.155838489532471, time: 100.28 ms, tokens/sec: 10210.99
step 49, loss: 7.094860076904297, time: 98.98 ms, tokens/sec: 10345.53
```


Switched to cuda and trained the model with bf16 precision

```
Using device: cuda
loaded 338025 tokens
1 epoch = 20 batches
step 0, loss: 10.823673248291016, time: 1134.84 ms, tokens/sec: 14437.23
step 1, loss: 10.773681640625, time: 356.77 ms, tokens/sec: 45922.92
step 2, loss: 10.696460723876953, time: 357.19 ms, tokens/sec: 45869.34
step 3, loss: 10.645000457763672, time: 357.26 ms, tokens/sec: 45860.65
step 4, loss: 10.569671630859375, time: 357.40 ms, tokens/sec: 45841.62
step 5, loss: 10.504947662353516, time: 357.14 ms, tokens/sec: 45875.99
step 6, loss: 10.413402557373047, time: 357.67 ms, tokens/sec: 45807.24
step 7, loss: 10.330463409423828, time: 357.32 ms, tokens/sec: 45852.72
step 8, loss: 10.247501373291016, time: 357.23 ms, tokens/sec: 45864.41
step 9, loss: 10.140941619873047, time: 357.51 ms, tokens/sec: 45828.66
step 10, loss: 10.052009582519531, time: 357.21 ms, tokens/sec: 45866.13
step 11, loss: 9.951866149902344, time: 357.03 ms, tokens/sec: 45890.26
step 12, loss: 9.854114532470703, time: 357.28 ms, tokens/sec: 45857.96
step 13, loss: 9.764053344726562, time: 357.18 ms, tokens/sec: 45870.93
step 14, loss: 9.674781799316406, time: 357.17 ms, tokens/sec: 45871.21
step 15, loss: 9.562599182128906, time: 357.27 ms, tokens/sec: 45858.48
step 16, loss: 9.468391418457031, time: 357.30 ms, tokens/sec: 45854.99
step 17, loss: 9.35312271118164, time: 357.74 ms, tokens/sec: 45798.36
step 18, loss: 9.262325286865234, time: 357.42 ms, tokens/sec: 45839.27
step 19, loss: 9.13851547241211, time: 357.23 ms, tokens/sec: 45864.57
step 20, loss: 8.955394744873047, time: 357.56 ms, tokens/sec: 45821.60
step 21, loss: 8.789409637451172, time: 357.03 ms, tokens/sec: 45889.50
step 22, loss: 8.691314697265625, time: 357.08 ms, tokens/sec: 45883.31
step 23, loss: 8.581092834472656, time: 357.49 ms, tokens/sec: 45830.49
step 24, loss: 8.462684631347656, time: 357.12 ms, tokens/sec: 45878.71
step 25, loss: 8.405288696289062, time: 357.33 ms, tokens/sec: 45851.41
step 26, loss: 8.302326202392578, time: 357.26 ms, tokens/sec: 45860.50
step 27, loss: 8.14952278137207, time: 357.28 ms, tokens/sec: 45857.04
step 28, loss: 8.056644439697266, time: 356.81 ms, tokens/sec: 45917.98
step 29, loss: 7.8988800048828125, time: 357.41 ms, tokens/sec: 45840.61
step 30, loss: 7.821723937988281, time: 357.38 ms, tokens/sec: 45844.86
step 31, loss: 7.720935821533203, time: 357.18 ms, tokens/sec: 45871.06
step 32, loss: 7.626550674438477, time: 357.45 ms, tokens/sec: 45835.57
step 33, loss: 7.547266006469727, time: 357.25 ms, tokens/sec: 45861.66
step 34, loss: 7.512643814086914, time: 357.30 ms, tokens/sec: 45855.51
step 35, loss: 7.381616592407227, time: 357.25 ms, tokens/sec: 45862.06
step 36, loss: 7.321258544921875, time: 357.31 ms, tokens/sec: 45853.12
step 37, loss: 7.258335113525391, time: 357.26 ms, tokens/sec: 45860.50
step 38, loss: 7.184694290161133, time: 357.33 ms, tokens/sec: 45851.47
step 39, loss: 7.07536506652832, time: 357.48 ms, tokens/sec: 45831.41
step 40, loss: 7.057899475097656, time: 357.19 ms, tokens/sec: 45868.76
step 41, loss: 6.868068695068359, time: 357.48 ms, tokens/sec: 45831.81
step 42, loss: 6.851839065551758, time: 357.54 ms, tokens/sec: 45824.59
step 43, loss: 6.777135848999023, time: 357.56 ms, tokens/sec: 45821.14
step 44, loss: 6.7092742919921875, time: 357.35 ms, tokens/sec: 45849.14
step 45, loss: 6.828512191772461, time: 357.37 ms, tokens/sec: 45846.02
step 46, loss: 6.846490859985352, time: 357.54 ms, tokens/sec: 45824.26
step 47, loss: 6.715211868286133, time: 357.35 ms, tokens/sec: 45848.62
step 48, loss: 6.6649169921875, time: 357.41 ms, tokens/sec: 45840.64
step 49, loss: 6.530155181884766, time: 357.32 ms, tokens/sec: 45853.00
```


Added torch.compile() to speed up the model training

```
Using device: cuda
loaded 338025 tokens
1 epoch = 20 batches
step 0, loss: 10.823673248291016, time: 49277.36 ms, tokens/sec: 332.49
step 1, loss: 10.773693084716797, time: 190.70 ms, tokens/sec: 85913.31
step 2, loss: 10.696449279785156, time: 190.74 ms, tokens/sec: 85896.88
step 3, loss: 10.64492416381836, time: 190.74 ms, tokens/sec: 85898.81
step 4, loss: 10.569671630859375, time: 190.97 ms, tokens/sec: 85791.46
step 5, loss: 10.504924774169922, time: 190.56 ms, tokens/sec: 85977.69
step 6, loss: 10.413410186767578, time: 191.21 ms, tokens/sec: 85684.28
step 7, loss: 10.330463409423828, time: 190.59 ms, tokens/sec: 85965.86
step 8, loss: 10.247486114501953, time: 190.88 ms, tokens/sec: 85836.26
step 9, loss: 10.140914916992188, time: 190.78 ms, tokens/sec: 85876.80
step 10, loss: 10.052017211914062, time: 190.98 ms, tokens/sec: 85790.39
step 11, loss: 9.951896667480469, time: 190.49 ms, tokens/sec: 86009.44
step 12, loss: 9.854106903076172, time: 190.94 ms, tokens/sec: 85805.17
step 13, loss: 9.764080047607422, time: 190.82 ms, tokens/sec: 85859.42
step 14, loss: 9.674781799316406, time: 191.06 ms, tokens/sec: 85755.06
step 15, loss: 9.562637329101562, time: 190.69 ms, tokens/sec: 85921.04
step 16, loss: 9.468360900878906, time: 190.78 ms, tokens/sec: 85880.13
step 17, loss: 9.353141784667969, time: 190.63 ms, tokens/sec: 85945.43
step 18, loss: 9.262317657470703, time: 191.04 ms, tokens/sec: 85762.77
step 19, loss: 9.138500213623047, time: 190.81 ms, tokens/sec: 85863.39
step 20, loss: 8.955375671386719, time: 191.15 ms, tokens/sec: 85711.85
step 21, loss: 8.789443969726562, time: 190.74 ms, tokens/sec: 85896.98
step 22, loss: 8.691009521484375, time: 191.01 ms, tokens/sec: 85777.01
step 23, loss: 8.581104278564453, time: 190.56 ms, tokens/sec: 85979.63
step 24, loss: 8.462583541870117, time: 190.86 ms, tokens/sec: 85843.87
step 25, loss: 8.405168533325195, time: 190.90 ms, tokens/sec: 85825.96
step 26, loss: 8.30221939086914, time: 190.98 ms, tokens/sec: 85787.61
step 27, loss: 8.149528503417969, time: 190.50 ms, tokens/sec: 86003.63
step 28, loss: 8.056554794311523, time: 191.00 ms, tokens/sec: 85780.97
step 29, loss: 7.898897171020508, time: 190.56 ms, tokens/sec: 85980.06
step 30, loss: 7.821813583374023, time: 190.45 ms, tokens/sec: 86026.88
step 31, loss: 7.720907211303711, time: 190.80 ms, tokens/sec: 85872.19
step 32, loss: 7.626506805419922, time: 191.09 ms, tokens/sec: 85739.76
step 33, loss: 7.547143936157227, time: 190.45 ms, tokens/sec: 86029.36
step 34, loss: 7.512678146362305, time: 191.22 ms, tokens/sec: 85681.71
step 35, loss: 7.381647109985352, time: 190.73 ms, tokens/sec: 85903.43
step 36, loss: 7.32087516784668, time: 190.99 ms, tokens/sec: 85785.68
step 37, loss: 7.25855827331543, time: 191.10 ms, tokens/sec: 85733.02
step 38, loss: 7.1845703125, time: 191.09 ms, tokens/sec: 85740.62
step 39, loss: 7.07542610168457, time: 190.50 ms, tokens/sec: 86007.18
step 40, loss: 7.058006286621094, time: 190.85 ms, tokens/sec: 85848.48
step 41, loss: 6.868047714233398, time: 190.69 ms, tokens/sec: 85918.89
step 42, loss: 6.851631164550781, time: 190.93 ms, tokens/sec: 85813.43
step 43, loss: 6.77703857421875, time: 190.58 ms, tokens/sec: 85968.66
step 44, loss: 6.708353042602539, time: 190.61 ms, tokens/sec: 85956.08
step 45, loss: 6.829179763793945, time: 190.72 ms, tokens/sec: 85906.86
step 46, loss: 6.844999313354492, time: 191.43 ms, tokens/sec: 85589.41
step 47, loss: 6.715143203735352, time: 190.80 ms, tokens/sec: 85868.33
step 48, loss: 6.664312362670898, time: 191.04 ms, tokens/sec: 85762.34
step 49, loss: 6.530029296875, time: 190.87 ms, tokens/sec: 85838.51
```


Added Flash Attention to speed up the model training

```
Using device: cuda
loaded 338025 tokens
1 epoch = 20 batches
step 0, loss: 10.823673248291016, time: 46591.12 ms, tokens/sec: 351.65
step 1, loss: 10.773700714111328, time: 128.15 ms, tokens/sec: 127848.29
step 2, loss: 10.69644546508789, time: 127.33 ms, tokens/sec: 128674.66
step 3, loss: 10.64522933959961, time: 127.65 ms, tokens/sec: 128348.30
step 4, loss: 10.569679260253906, time: 127.26 ms, tokens/sec: 128746.99
step 5, loss: 10.504947662353516, time: 125.81 ms, tokens/sec: 130226.49
step 6, loss: 10.413402557373047, time: 125.73 ms, tokens/sec: 130308.72
step 7, loss: 10.330463409423828, time: 126.44 ms, tokens/sec: 129575.04
step 8, loss: 10.247478485107422, time: 126.36 ms, tokens/sec: 129666.00
step 9, loss: 10.140922546386719, time: 126.01 ms, tokens/sec: 130021.00
step 10, loss: 10.051990509033203, time: 126.14 ms, tokens/sec: 129882.89
step 11, loss: 9.951850891113281, time: 126.32 ms, tokens/sec: 129703.69
step 12, loss: 9.85409164428711, time: 126.28 ms, tokens/sec: 129740.91
step 13, loss: 9.764060974121094, time: 126.56 ms, tokens/sec: 129454.22
step 14, loss: 9.674713134765625, time: 126.82 ms, tokens/sec: 129191.38
step 15, loss: 9.56296157836914, time: 126.14 ms, tokens/sec: 129885.34
step 16, loss: 9.468421936035156, time: 126.62 ms, tokens/sec: 129391.09
step 17, loss: 9.353130340576172, time: 126.10 ms, tokens/sec: 129931.76
step 18, loss: 9.262367248535156, time: 125.88 ms, tokens/sec: 130151.02
step 19, loss: 9.138404846191406, time: 126.20 ms, tokens/sec: 129825.96
step 20, loss: 8.955482482910156, time: 126.01 ms, tokens/sec: 130018.04
step 21, loss: 8.789375305175781, time: 126.16 ms, tokens/sec: 129862.76
step 22, loss: 8.691322326660156, time: 126.36 ms, tokens/sec: 129660.37
step 23, loss: 8.581060409545898, time: 126.91 ms, tokens/sec: 129094.30
step 24, loss: 8.462615966796875, time: 126.10 ms, tokens/sec: 129927.33
step 25, loss: 8.405288696289062, time: 126.40 ms, tokens/sec: 129615.86
step 26, loss: 8.30247688293457, time: 126.56 ms, tokens/sec: 129459.34
step 27, loss: 8.149541854858398, time: 126.38 ms, tokens/sec: 129638.11
step 28, loss: 8.056657791137695, time: 126.46 ms, tokens/sec: 129555.50
step 29, loss: 7.898904800415039, time: 125.99 ms, tokens/sec: 130038.96
step 30, loss: 7.821723937988281, time: 126.48 ms, tokens/sec: 129538.41
step 31, loss: 7.720996856689453, time: 126.42 ms, tokens/sec: 129599.73
step 32, loss: 7.62653923034668, time: 126.11 ms, tokens/sec: 129914.07
step 33, loss: 7.547079086303711, time: 125.95 ms, tokens/sec: 130082.53
step 34, loss: 7.512615203857422, time: 129.07 ms, tokens/sec: 126941.64
step 35, loss: 7.38165283203125, time: 126.37 ms, tokens/sec: 129654.25
step 36, loss: 7.32176399230957, time: 126.20 ms, tokens/sec: 129824.98
step 37, loss: 7.2584075927734375, time: 127.09 ms, tokens/sec: 128920.65
step 38, loss: 7.184680938720703, time: 127.92 ms, tokens/sec: 128081.09
step 39, loss: 7.075347900390625, time: 127.18 ms, tokens/sec: 128825.91
step 40, loss: 7.0579071044921875, time: 128.30 ms, tokens/sec: 127701.70
step 41, loss: 6.867761611938477, time: 126.47 ms, tokens/sec: 129546.22
step 42, loss: 6.852079391479492, time: 126.77 ms, tokens/sec: 129242.89
step 43, loss: 6.77692985534668, time: 126.97 ms, tokens/sec: 129037.58
step 44, loss: 6.708415985107422, time: 127.24 ms, tokens/sec: 128760.25
step 45, loss: 6.82914924621582, time: 126.90 ms, tokens/sec: 129111.28
step 46, loss: 6.844869613647461, time: 126.79 ms, tokens/sec: 129222.47
step 47, loss: 6.715185165405273, time: 126.81 ms, tokens/sec: 129205.71
step 48, loss: 6.664623260498047, time: 126.52 ms, tokens/sec: 129493.49
step 49, loss: 6.530099868774414, time: 126.60 ms, tokens/sec: 129419.84
```

- This is 33% faster than the previous model training without Flash Attention


- any number at the power of 2 is recommended for the model training as cuda is optimized for that. Including the batch size, sequence length, and hidden size.


Overriding the vocab size to 50304 as it is at the power of 2

```
sing device: cuda
loaded 338025 tokens
1 epoch = 20 batches
step 0, loss: 10.826412200927734, time: 24504.52 ms, tokens/sec: 668.61
step 1, loss: 10.751480102539062, time: 111.74 ms, tokens/sec: 146627.83
step 2, loss: 10.686775207519531, time: 110.42 ms, tokens/sec: 148383.74
step 3, loss: 10.61892318725586, time: 110.76 ms, tokens/sec: 147923.16
step 4, loss: 10.536689758300781, time: 110.86 ms, tokens/sec: 147787.95
step 5, loss: 10.460895538330078, time: 110.65 ms, tokens/sec: 148074.88
step 6, loss: 10.367889404296875, time: 110.60 ms, tokens/sec: 148143.51
step 7, loss: 10.266380310058594, time: 110.99 ms, tokens/sec: 147611.77
step 8, loss: 10.181755065917969, time: 110.55 ms, tokens/sec: 148201.33
step 9, loss: 10.069171905517578, time: 110.57 ms, tokens/sec: 148177.05
step 10, loss: 9.966400146484375, time: 110.87 ms, tokens/sec: 147773.97
step 11, loss: 9.851570129394531, time: 110.70 ms, tokens/sec: 148000.25
step 12, loss: 9.74478530883789, time: 110.75 ms, tokens/sec: 147938.12
step 13, loss: 9.654521942138672, time: 110.82 ms, tokens/sec: 147837.55
step 14, loss: 9.56020736694336, time: 111.04 ms, tokens/sec: 147549.33
step 15, loss: 9.448078155517578, time: 111.01 ms, tokens/sec: 147587.99
step 16, loss: 9.349971771240234, time: 111.10 ms, tokens/sec: 147472.70
step 17, loss: 9.237506866455078, time: 111.11 ms, tokens/sec: 147452.77
step 18, loss: 9.140865325927734, time: 128.35 ms, tokens/sec: 127650.46
step 19, loss: 9.00937271118164, time: 112.70 ms, tokens/sec: 145381.74
step 20, loss: 8.83041000366211, time: 110.52 ms, tokens/sec: 148240.66
step 21, loss: 8.65383529663086, time: 111.21 ms, tokens/sec: 147322.84
step 22, loss: 8.554647445678711, time: 110.65 ms, tokens/sec: 148068.81
step 23, loss: 8.435354232788086, time: 110.87 ms, tokens/sec: 147773.97
step 24, loss: 8.316843032836914, time: 110.63 ms, tokens/sec: 148099.45
step 25, loss: 8.274700164794922, time: 110.72 ms, tokens/sec: 147974.76
step 26, loss: 8.176961898803711, time: 111.40 ms, tokens/sec: 147075.33
step 27, loss: 8.029972076416016, time: 110.49 ms, tokens/sec: 148279.68
step 28, loss: 7.945899963378906, time: 110.48 ms, tokens/sec: 148304.00
step 29, loss: 7.786319732666016, time: 110.72 ms, tokens/sec: 147983.04
step 30, loss: 7.708597183227539, time: 110.67 ms, tokens/sec: 148049.67
step 31, loss: 7.617708206176758, time: 110.81 ms, tokens/sec: 147851.86
step 32, loss: 7.534358978271484, time: 110.93 ms, tokens/sec: 147701.87
step 33, loss: 7.451999664306641, time: 110.54 ms, tokens/sec: 148224.03
step 34, loss: 7.433612823486328, time: 110.61 ms, tokens/sec: 148125.31
step 35, loss: 7.308221817016602, time: 110.89 ms, tokens/sec: 147749.19
step 36, loss: 7.245744705200195, time: 110.54 ms, tokens/sec: 148214.12
step 37, loss: 7.190338134765625, time: 110.36 ms, tokens/sec: 148460.35
step 38, loss: 7.132726669311523, time: 110.66 ms, tokens/sec: 148058.29
step 39, loss: 7.008186340332031, time: 111.36 ms, tokens/sec: 147128.86
step 40, loss: 6.993412017822266, time: 110.95 ms, tokens/sec: 147664.74
step 41, loss: 6.795404434204102, time: 110.69 ms, tokens/sec: 148023.20
step 42, loss: 6.790424346923828, time: 110.42 ms, tokens/sec: 148377.01
step 43, loss: 6.722799301147461, time: 111.18 ms, tokens/sec: 147368.65
step 44, loss: 6.65477180480957, time: 110.61 ms, tokens/sec: 148117.96
step 45, loss: 6.778308868408203, time: 110.73 ms, tokens/sec: 147961.37
step 46, loss: 6.809177398681641, time: 111.15 ms, tokens/sec: 147403.11
step 47, loss: 6.682546615600586, time: 111.22 ms, tokens/sec: 147316.53
step 48, loss: 6.640913009643555, time: 111.20 ms, tokens/sec: 147338.95
step 49, loss: 6.501094818115234, time: 111.25 ms, tokens/sec: 147274.54
```


Extra memory is required for the model training with the increased vocab size. The model training time is reduced by 11% compared to the previous model training with Flash Attention.