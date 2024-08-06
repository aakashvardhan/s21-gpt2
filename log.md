

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