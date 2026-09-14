# Rule metrics, split = dev

**Status: pipeline check on the development split. These numbers are for debugging the pipeline, not for the paper.**

Primary prominence threshold 0.02; full definition (position, intensity, shape). `LR+ [CI]` is the analytic 95 percent interval; `boot` is the scaffold-cluster bootstrap interval (500 resamples); `LR+ pos` is the same rule scored by position only. Rules with fewer than 10 positives are marked underpowered.

## Stratum: main (n = 384)

| rule | tier | truth group | window | n+ | sens | spec | LR+ [CI] | LR+ boot | LR- [CI] | LR+ pos | FP enriched in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SMITH-BR5-ROH-PRIM-CO | group | alcohol_primary | 1000-1075 | 4 (underpowered) | 0.75 | 0.05 | 0.8 [0.5, 1.4] |  | 4.75 [0.83, 27.34] | 0.8 |  |
| SMITH-BR5-ROH-SEC-CO | group | alcohol_secondary | 1075-1150 | 19 | 0.95 | 0.04 | 1.0 [0.9, 1.1] | [0.8, 1.0] | 1.48 [0.20, 10.71] | 1.0 | aromatics OR=3.5 (n=332); ketone_aromatic OR=2.5 (n=29); nitriles OR=2.2 (n=26) |
| SMITH-BR5-ROH-TERT-CO | group | alcohol_tertiary | 1100-1210 | 1 (underpowered) | 1.00 | 0.01 | 0.8 [0.3, 1.7] |  | 27.43 [2.00, 375.72] | 0.8 |  |
| SMITH-BR5-ROH-OH-WAG | group | alcohols | 600-700 | 42 | 0.79 | 0.16 | 0.9 [0.8, 1.1] | [0.7, 1.1] | 1.33 [0.71, 2.50] | 0.9 | aromatic_mono OR=10.9 (n=66); alkene_vinyl OR=5.0 (n=12); aromatics OR=2.7 (n=274) |
| SMITH-BR5-ROH-OH-STR | group | alcohols | 3300-3400 | 42 | 0.33 | 0.74 | 1.3 [0.8, 2.1] | [0.7, 2.2] | 0.90 [0.72, 1.12] | 1.3 | amine_primary OR=21.3 (n=15); amine_primary_aromatic OR=16.5 (n=12); amines OR=7.0 (n=31) |
| SMITH-ALD17-AR-CO | group | aldehyde_aromatic | 1685-1710 | 19 | 0.32 | 0.90 | 3.2 [1.5, 6.7] | [1.3, 7.6] | 0.76 [0.56, 1.03] | 1.8 | methylene OR=6.7 (n=33); ketone_saturated OR=5.2 (n=4); carbonyl_any OR=5.1 (n=28) |
| SMITH-ALD17-SAT-CO | group | aldehyde_saturated | 1720-1740 | 0 (underpowered) | nan | 0.92 | 6.5 [0.9, 47.8] |  | 0.54 [0.08, 3.85] | 1.9 |  |
| SMITH-ALD17-CH-BEND | group | aldehydes | 1380-1400 | 19 | 0.47 | 0.57 | 1.1 [0.7, 1.8] | [0.7, 1.9] | 0.92 [0.59, 1.42] | 1.1 | alkene_trisubstituted OR=3.8 (n=9); ketone_aromatic OR=2.3 (n=18); alkane OR=2.2 (n=126) |
| SMITH-ALD17-CH-STR | group | aldehydes | 2700-2850 | 19 | 0.42 | 0.69 | 1.4 [0.8, 2.4] | [0.4, 2.2] | 0.84 [0.57, 1.23] | 1.4 | amine_primary OR=4.7 (n=12); amine_primary_aromatic OR=4.6 (n=10); alkene_trisubstituted OR=3.2 (n=7) |
| SMITH-ALK16-CC-STR | class | alkene | 1630-1680 | 71 | 0.39 | 0.56 | 0.9 [0.7, 1.2] | [0.5, 1.3] | 1.09 [0.88, 1.35] | 0.9 | amide_secondary OR=6.9 (n=25); amides OR=4.1 (n=31); ketone_aromatic OR=3.0 (n=14) |
| SMITH-ALK16-CH-STR | class | alkene | 3000-3100 | 71 | 0.58 | 0.36 | 0.9 [0.7, 1.1] | [0.7, 1.1] | 1.18 [0.87, 1.61] | 0.9 | nitro OR=6.6 (n=16); aromatics OR=5.7 (n=196); aromatic_mono OR=3.4 (n=48) |
| SMITH-ALK16-TRISUB-WAG | group | alkene_trisubstituted | 790-840 | 12 | 1.00 | 0.18 | 1.2 [1.1, 1.3] | [1.1, 1.3] | 0.21 [0.01, 3.15] | 1.2 | phenol OR=7.0 (n=14); aromatic_para OR=5.1 (n=125); ester_aromatic OR=3.9 (n=38) |
| SMITH-ALK16-TRISUB-CC | group | alkene_trisubstituted | 1660-1680 | 12 | 0.75 | 0.79 | 3.6 [2.5, 5.3] | [1.8, 5.1] | 0.32 [0.12, 0.84] | 3.6 | ketone_aromatic OR=7.5 (n=15); ketones OR=5.0 (n=19); amide_secondary OR=2.9 (n=14) |
| SMITH-ALK16-VINYL-WAG2 | group | alkene_vinyl | 905-915 | 13 | 0.39 | 0.79 | 1.8 [0.9, 3.7] | [0.4, 3.4] | 0.78 [0.51, 1.21] | 1.8 | ether_saturated OR=5.6 (n=11); ketone_saturated OR=3.8 (n=4); amide_secondary OR=2.0 (n=10) |
| SMITH-ALK16-VINYL-WAG1 | group | alkene_vinyl | 985-995 | 13 | 0.23 | 0.81 | 1.2 [0.4, 3.3] | [0.2, 3.3] | 0.95 [0.70, 1.29] | 1.2 | ketone_saturated OR=2.7 (n=3); ether_saturated OR=2.1 (n=6); ester_saturated OR=2.1 (n=6) |
| SMITH-ALK16-VINYL-CC | group | alkene_vinyl | 1630-1660 | 13 | 0.39 | 0.74 | 1.5 [0.7, 3.0] | [0.4, 2.6] | 0.83 [0.54, 1.29] | 1.5 | amide_secondary OR=4.2 (n=17); amine_primary OR=3.8 (n=10); amine_primary_aromatic OR=3.4 (n=8) |
| SMITH-ALY17-INT-CC | group | alkyne_internal | 2190-2260 | 18 | 0.72 | 0.78 | 3.3 [2.3, 4.7] | [2.2, 4.4] | 0.36 [0.17, 0.75] | 3.3 | nitriles OR=8.4 (n=16); nitrile_aromatic OR=8.4 (n=16); alkene_disubstituted OR=3.4 (n=14) |
| SMITH-ALY17-TERM-CH-BEND | group | alkyne_terminal | 600-700 | 10 | 0.90 | 0.17 | 1.1 [0.9, 1.3] | [0.8, 1.2] | 0.59 [0.09, 3.86] | 1.1 | alkene_vinyl OR=5.7 (n=13); aromatic_mono OR=3.2 (n=72); amide_secondary OR=3.0 (n=33) |
| SMITH-ALY17-TERM-CC | group | alkyne_terminal | 2100-2140 | 10 | 0.70 | 0.75 | 2.9 [1.8, 4.4] | [1.4, 3.9] | 0.40 [0.15, 1.03] | 2.9 | amine_secondary_saturated OR=4.4 (n=3); alkene_trisubstituted OR=3.2 (n=6); alcohol_secondary OR=3.0 (n=9) |
| SMITH-ALY17-TERM-CH | group | alkyne_terminal | 3250-3350 | 10 | 0.80 | 0.73 | 3.0 [2.1, 4.2] | [1.0, 4.1] | 0.27 [0.08, 0.95] | 3.0 | amide_secondary OR=26.8 (n=31); n_h_any OR=14.2 (n=61); amine_primary_aromatic OR=10.8 (n=12) |
| SMITH-BR8-AMD1-WAG | group | amide_primary | 600-750 | 1 (underpowered) | 1.00 | 0.03 | 0.8 [0.3, 1.7] |  | 7.68 [0.66, 90.04] | 0.8 |  |
| SMITH-BR8-AMD1-CN | group | amide_primary | 1390-1430 | 1 (underpowered) | 1.00 | 0.26 | 1.0 [0.5, 2.2] |  | 0.97 [0.09, 10.81] | 1.0 |  |
| SMITH-BR8-AMD1-SCIS | group | amide_primary | 1620-1650 | 1 (underpowered) | 0.00 | 0.69 | 0.8 [0.1, 9.1] |  | 1.08 [0.48, 2.41] | 0.8 |  |
| SMITH-BR8-AMD1-NH-STR | group | amide_primary | 3170-3370 | 1 (underpowered) | 1.00 | 0.64 | 2.1 [0.9, 4.7] |  | 0.39 [0.04, 4.34] | 2.1 |  |
| SMITH-BR8-AMD2-WAG | group | amide_secondary | 680-750 | 35 | 0.91 | 0.07 | 1.0 [0.9, 1.1] | [0.8, 1.1] | 1.25 [0.40, 3.93] | 1.0 | aromatic_mono OR=11.6 (n=62); ester_aromatic OR=6.8 (n=39); alkane OR=6.7 (n=241) |
| SMITH-BR8-AMD2-CN | group | amide_secondary | 1230-1310 | 35 | 0.89 | 0.03 | 0.9 [0.8, 1.0] | [0.7, 1.0] | 3.32 [1.13, 9.76] | 0.9 | ether OR=8.1 (n=82); alkene OR=6.1 (n=66); ether_mixed OR=5.3 (n=59) |
| SMITH-BR8-AMD2-NH-IPB | group | amide_secondary | 1515-1570 | 35 | 0.31 | 0.84 | 2.0 [1.2, 3.5] | [1.0, 3.5] | 0.81 [0.65, 1.02] | 1.4 | nitro OR=15.5 (n=12); aromatics OR=9.0 (n=54); amine_secondary_aromatic OR=3.6 (n=7) |
| SMITH-BR8-AMD2-NH-STR | group | amide_secondary | 3170-3370 | 35 | 0.91 | 0.69 | 3.0 [2.5, 3.6] | [2.4, 3.6] | 0.12 [0.04, 0.37] | 3.0 | alkyne_terminal OR=51.5 (n=10); amine_primary OR=30.7 (n=17); amine_primary_aromatic OR=24.6 (n=14) |
| SMITH-BR8-AMD-CO | group | amides | 1630-1680 | 48 | 0.50 | 0.90 | 4.9 [3.2, 7.6] | [3.0, 7.9] | 0.56 [0.42, 0.74] | 1.9 | ketone_aromatic OR=10.9 (n=13); phenol OR=10.7 (n=7); ketones OR=8.0 (n=15) |
| SMITH-BR8-AMN1-WAG | group | amine_primary | 750-850 | 18 | 0.94 | 0.03 | 1.0 [0.9, 1.1] | [0.8, 1.0] | 1.69 [0.23, 12.33] | 1.0 | aromatic_para OR=14.7 (n=131); aromatics OR=12.6 (n=335); ether_mixed OR=5.1 (n=60) |
| SMITH-BR8-AMN1-SCIS | group | amine_primary | 1580-1650 | 18 | 1.00 | 0.13 | 1.1 [1.0, 1.2] | [1.1, 1.2] | 0.20 [0.01, 3.11] | 1.1 | aromatics OR=23.1 (n=311); ether_mixed OR=22.7 (n=60); aromatic_ortho OR=9.9 (n=29) |
| SMITH-BR8-AMN1-AR-CN | group | amine_primary_aromatic | 1250-1350 | 15 | 0.93 | 0.05 | 1.0 [0.9, 1.1] | [0.8, 1.0] | 1.37 [0.20, 9.57] | 1.0 | aromatics OR=6.6 (n=331); ester_aromatic OR=4.5 (n=38); amines OR=4.2 (n=35) |
| SMITH-BR8-AMN1-AR-SYM | group | amine_primary_aromatic | 3340-3420 | 15 | 0.53 | 0.83 | 3.2 [1.9, 5.5] | [1.4, 5.6] | 0.56 [0.32, 0.96] | 3.2 | amine_secondary_aromatic OR=5.8 (n=10); amine_secondary OR=3.4 (n=10); alcohol_secondary OR=3.3 (n=7) |
| SMITH-BR8-AMN1-AR-ASYM | group | amine_primary_aromatic | 3420-3500 | 15 | 0.67 | 0.90 | 6.8 [4.3, 11.0] | [3.5, 10.1] | 0.37 [0.18, 0.76] | 6.8 | ketone_saturated OR=3.6 (n=3); alcohols OR=3.2 (n=9); alcohol_secondary OR=2.8 (n=4) |
| SMITH-BR8-AMN1-SAT-CN | group | amine_primary_saturated | 1020-1250 | 2 (underpowered) | 1.00 | 0.00 | 0.8 [0.5, 1.4] |  | 127.67 [3.00, 5438.18] | 0.8 |  |
| SMITH-BR8-AMN1-SAT-SYM | group | amine_primary_saturated | 3280-3310 | 2 (underpowered) | 0.00 | 0.89 | 1.5 [0.1, 18.7] |  | 0.94 [0.57, 1.56] | 1.5 |  |
| SMITH-BR8-AMN1-SAT-ASYM | group | amine_primary_saturated | 3350-3380 | 2 (underpowered) | 1.00 | 0.95 | 17.2 [8.8, 33.8] |  | 0.18 [0.01, 2.20] | 17.2 |  |
| SMITH-BR8-AMN2-WAG | group | amine_secondary | 700-750 | 27 | 0.85 | 0.14 | 1.0 [0.8, 1.2] | [0.8, 1.2] | 1.04 [0.41, 2.65] | 1.0 | nitriles OR=9.7 (n=26); nitrile_aromatic OR=8.9 (n=24); aldehydes OR=6.2 (n=17) |
| SMITH-BR8-AMN2-AR-CNC | group | amine_secondary_aromatic | 1250-1350 | 20 | 1.00 | 0.05 | 1.0 [1.0, 1.1] | [1.0, 1.1] | 0.45 [0.03, 7.13] | 1.0 | aromatics OR=6.0 (n=325); methylene_chain_4 OR=3.9 (n=31); ketone_aromatic OR=3.5 (n=28) |
| SMITH-BR8-AMN2-AR-NH | group | amine_secondary_aromatic | 3380-3420 | 20 | 0.25 | 0.90 | 2.5 [1.1, 5.7] | [0.8, 5.0] | 0.83 [0.64, 1.07] | 2.5 | alcohol_secondary OR=5.0 (n=6); amine_primary_aromatic OR=3.8 (n=4); amine_primary OR=3.0 (n=4) |
| SMITH-BR8-AMN2-SAT-CNC | group | amine_secondary_saturated | 1130-1180 | 5 (underpowered) | 1.00 | 0.09 | 1.0 [0.8, 1.3] |  | 0.95 [0.07, 13.70] | 1.0 |  |
| SMITH-BR8-AMN2-SAT-NH | group | amine_secondary_saturated | 3280-3320 | 5 (underpowered) | 0.40 | 0.84 | 2.5 [0.8, 7.5] |  | 0.72 [0.35, 1.46] | 2.5 |  |
| SMITH-BR4-BZ-META-690 | group | aromatic_meta | 680-700 | 13 | 0.77 | 0.46 | 1.4 [1.0, 1.9] | [0.9, 1.9] | 0.50 [0.19, 1.37] | 1.4 | aromatic_mono OR=5.5 (n=64); aromatic_ortho OR=2.7 (n=22); alkene_vinyl OR=2.6 (n=10) |
| SMITH-BR4-BZ-META-OOP | group | aromatic_meta | 750-810 | 13 | 0.92 | 0.13 | 1.1 [0.9, 1.2] | [0.8, 1.1] | 0.59 [0.09, 3.98] | 1.1 | amine_primary_aromatic OR=4.9 (n=15); aromatics OR=4.5 (n=307); phenol OR=4.2 (n=13) |
| SMITH-BR4-BZ-META-BOTH | group | aromatic_meta | 750-810 +680-700 | 13 | 0.77 | 0.53 | 1.6 [1.2, 2.2] | [0.9, 2.1] | 0.43 [0.16, 1.18] | 1.6 | aromatic_mono OR=3.6 (n=55); aromatics OR=3.6 (n=169); alkene_trisubstituted OR=3.2 (n=9) |
| SMITH-BR4-BZ-MONO-690 | group | aromatic_mono | 680-700 | 77 | 0.83 | 0.52 | 1.7 [1.5, 2.0] | [1.4, 2.1] | 0.32 [0.20, 0.54] | 1.7 | aromatic_meta OR=3.4 (n=10); alcohol_secondary OR=3.4 (n=7); alkene_trisubstituted OR=3.1 (n=9) |
| SMITH-BR4-BZ-MONO-OOP | group | aromatic_mono | 710-770 | 77 | 0.99 | 0.07 | 1.1 [1.0, 1.1] | [1.0, 1.1] | 0.17 [0.02, 1.26] | 1.1 | aromatics OR=8.4 (n=267); ester_aromatic OR=6.3 (n=33); nitriles OR=4.8 (n=26) |
| SMITH-BR4-BZ-MONO-BOTH | group | aromatic_mono | 710-770 +680-700 | 77 | 0.82 | 0.54 | 1.8 [1.5, 2.1] | [1.5, 2.2] | 0.33 [0.21, 0.54] | 1.8 | aromatic_meta OR=3.8 (n=10); alcohol_secondary OR=3.7 (n=7); aromatics OR=3.4 (n=135) |
| SMITH-BR4-BZ-ORTHO-OOP | group | aromatic_ortho | 735-770 no 680-700 | 29 | 0.24 | 0.64 | 0.7 [0.3, 1.3] | [0.2, 1.4] | 1.19 [0.95, 1.48] | 0.7 | carboxylic_acid_aromatic OR=12.7 (n=3); alkyne_terminal OR=2.6 (n=6); alkyne OR=2.6 (n=10) |
| SMITH-BR4-BZ-PARA-OOP | group | aromatic_para | 790-860 no 680-700 | 135 | 0.41 | 0.61 | 1.1 [0.8, 1.4] | [0.8, 1.4] | 0.96 [0.81, 1.15] | 1.1 | nitro OR=2.5 (n=5); amine_primary_aromatic OR=2.2 (n=7); aldehydes OR=1.9 (n=5) |
| SMITH-BZ16-OOP | class | aromatics | 700-1000 | 359 | 1.00 | 0.00 | 1.0 [1.0, 1.1] | [1.0, 1.1] | 0.07 [0.00, 3.57] | 1.0 | alkane OR=9.4 (n=23); methyl OR=4.8 (n=21); methylene OR=4.8 (n=21) |
| SMITH-BZ16-RING | class | aromatics | 1400-1620 | 359 | 1.00 | 0.00 | 1.0 [1.0, 1.1] | [1.0, 1.1] | 0.07 [0.00, 3.57] | 1.0 | alkane OR=9.4 (n=23); methyl OR=4.8 (n=21); methylene OR=4.8 (n=21) |
| SMITH-BZ16-ARCH-STR | class | aromatics | 3000-3100 | 359 | 0.65 | 0.68 | 2.0 [1.1, 3.6] | [1.2, 6.0] | 0.51 [0.38, 0.69] | 2.0 | methyl OR=5.7 (n=8); alkene OR=3.9 (n=3); methylene OR=1.2 (n=7) |
| SMITH-BR5-CO-GENERAL | class | c_o_single_any | 1000-1300 | 129 | 0.88 | 0.37 | 1.4 [1.2, 1.6] | [1.2, 1.6] | 0.32 [0.19, 0.52] | 1.0 | ester_aromatic OR=45.6 (n=31); esters OR=15.3 (n=47); amine_secondary_saturated OR=6.6 (n=5) |
| SMITH-BR7-CARB-OCC | group | carbonate_organic | 1000-1060 | 0 (underpowered) | nan | 0.81 | 2.6 [0.4, 18.5] |  | 0.62 [0.09, 4.40] | 0.5 |  |
| SMITH-BR7-CARB-AR-OCO | group | carbonate_organic | 1205-1230 | 0 (underpowered) | nan | 0.85 | 3.3 [0.5, 23.7] |  | 0.59 [0.08, 4.19] | 0.9 |  |
| SMITH-BR7-CARB-MIX-OCO | group | carbonate_organic | 1210-1250 | 0 (underpowered) | nan | 0.74 | 1.9 [0.3, 14.0] |  | 0.67 [0.09, 4.77] | 0.6 |  |
| SMITH-BR7-CARB-SAT-OCO | group | carbonate_organic | 1240-1280 | 0 (underpowered) | nan | 0.77 | 2.2 [0.3, 15.8] |  | 0.65 [0.09, 4.60] | 0.7 |  |
| SMITH-BR7-CARB-SAT-CO | group | carbonate_organic | 1730-1750 | 0 (underpowered) | nan | 0.94 | 8.2 [1.1, 60.5] |  | 0.53 [0.07, 3.78] | 2.0 |  |
| SMITH-BR7-CARB-MIX-CO | group | carbonate_organic | 1760-1790 | 0 (underpowered) | nan | 0.99 | 77.0 [7.6, 781.1] |  | 0.50 [0.07, 3.57] | 7.3 |  |
| SMITH-BR7-CARB-AR-CO | group | carbonate_organic | 1775-1820 | 0 (underpowered) | nan | 1.00 | 385.0 [12.9, 11459.7] |  | 0.50 [0.07, 3.55] | 6.5 |  |
| SMITH-BR6-CO-GENERAL | class | carbonyl_any | 1600-1900 | 177 | 0.81 | 0.84 | 5.1 [3.7, 7.0] | [3.0, 11.1] | 0.22 [0.16, 0.30] | 1.1 | phenol OR=10.5 (n=4); amine_primary_aromatic OR=6.1 (n=6); amine_primary OR=5.5 (n=7) |
| SMITH-BR6-ACID-AR-CO | group | carboxylic_acid_aromatic | 1680-1710 | 3 (underpowered) | 1.00 | 0.87 | 6.9 [4.4, 10.8] |  | 0.14 [0.01, 1.91] | 3.0 |  |
| SMITH-BR6-ACID-SAT-CO | group | carboxylic_acid_saturated | 1700-1730 | 1 (underpowered) | 0.00 | 0.81 | 1.3 [0.1, 14.3] |  | 0.93 [0.42, 2.07] | 2.0 |  |
| SMITH-BR6-ACID-OH-OOP | group | carboxylic_acids | 900-960 | 5 (underpowered) | 1.00 | 0.14 | 1.1 [0.8, 1.4] |  | 0.57 [0.04, 8.20] | 1.1 |  |
| SMITH-BR6-ACID-CO | group | carboxylic_acids | 1210-1320 | 5 (underpowered) | 1.00 | 0.01 | 0.9 [0.7, 1.2] |  | 9.05 [0.52, 156.63] | 0.9 |  |
| SMITH-BR6-ACID-OH-IPB | group | carboxylic_acids | 1395-1440 | 5 (underpowered) | 1.00 | 0.20 | 1.1 [0.9, 1.5] |  | 0.41 [0.03, 5.85] | 1.1 |  |
| SMITH-BR6-ACID-OH-STR | group | carboxylic_acids | 2500-3500 | 5 (underpowered) | 0.20 | 0.93 | 2.9 [0.5, 17.5] |  | 0.86 [0.55, 1.33] | 0.9 |  |
| SMITH-BR7-EST-AR-OCC | group | ester_aromatic | 1100-1130 | 40 | 0.45 | 0.82 | 2.5 [1.7, 3.8] | [1.4, 4.3] | 0.67 [0.50, 0.89] | 1.0 | ether_mixed OR=3.7 (n=21); alkane OR=2.9 (n=53); nitro OR=2.8 (n=5) |
| SMITH-BR7-EST-AR-CCO | group | ester_aromatic | 1250-1310 | 40 | 0.85 | 0.83 | 5.0 [3.9, 6.6] | [3.9, 6.8] | 0.18 [0.09, 0.38] | 1.1 | carboxylic_acids OR=7.2 (n=3); amine_secondary_aromatic OR=4.6 (n=9); aromatic_meta OR=4.0 (n=3) |
| SMITH-BR7-EST-AR-CO | group | ester_aromatic | 1715-1730 | 40 | 0.30 | 0.94 | 5.2 [2.7, 9.8] | [2.3, 10.3] | 0.74 [0.61, 0.91] | 1.6 | ketone_saturated OR=22.0 (n=6); esters OR=21.8 (n=12); ester_saturated OR=15.4 (n=9) |
| SMITH-BR7-EST-SAT-OCC | group | ester_saturated | 1030-1100 | 25 | 0.32 | 0.68 | 1.0 [0.6, 1.8] | [0.3, 2.0] | 1.00 [0.76, 1.33] | 1.0 | ether_saturated OR=26.5 (n=16); alkene_vinyl OR=2.7 (n=4); c_o_single_any OR=2.7 (n=56) |
| SMITH-BR7-EST-SAT-CCO | group | ester_saturated | 1160-1210 | 25 | 0.40 | 0.73 | 1.5 [0.9, 2.5] | [0.5, 2.7] | 0.82 [0.59, 1.13] | 0.9 | alkane OR=5.5 (n=87); methylene OR=4.7 (n=80); ether_mixed OR=4.3 (n=32) |
| SMITH-BR7-EST-SAT-CO | group | ester_saturated | 1735-1755 | 25 | 0.44 | 0.98 | 26.3 [10.6, 65.3] | [9.6, 101.8] | 0.57 [0.40, 0.81] | 3.4 | carbonyl_any OR=18.4 (n=6); methyl OR=7.0 (n=6); esters OR=7.0 (n=3) |
| SMITH-BR5-ETHER-ARYL-CO | group | ether_aryl | 1200-1300 | 2 (underpowered) | 1.00 | 0.01 | 0.8 [0.5, 1.4] |  | 25.53 [1.53, 426.61] | 0.8 |  |
| SMITH-BR5-ETHER-MIX-CO-SAT | group | ether_mixed | 1010-1050 | 62 | 0.87 | 0.19 | 1.1 [1.0, 1.2] | [0.9, 1.2] | 0.69 [0.35, 1.37] | 1.1 | aromatic_mono OR=5.7 (n=67); alkene_vinyl OR=5.5 (n=11); amide_secondary OR=5.4 (n=31) |
| SMITH-BR5-ETHER-MIX-CO-AR | group | ether_mixed | 1200-1300 | 62 | 1.00 | 0.01 | 1.0 [1.0, 1.0] | [1.0, 1.0] | 1.03 [0.05, 21.10] | 1.0 | aromatics OR=12.1 (n=296); aromatic_para OR=2.6 (n=109); alkane OR=2.3 (n=223) |
| SMITH-BR5-ETHER-SAT-CO | group | ether_saturated | 1070-1140 | 26 | 0.89 | 0.04 | 0.9 [0.8, 1.1] | [0.7, 1.1] | 2.58 [0.80, 8.29] | 0.9 | aromatics OR=6.9 (n=330); alcohols OR=3.9 (n=36); ketone_aromatic OR=3.1 (n=29) |
| SMITH-BR6-KET-AR-CCC | group | ketone_aromatic | 1230-1300 | 29 | 0.41 | 0.71 | 1.4 [0.9, 2.3] | [0.7, 2.2] | 0.83 [0.60, 1.13] | 1.1 | ester_aromatic OR=17.2 (n=32); aromatic_meta OR=5.6 (n=9); esters OR=5.0 (n=41) |
| SMITH-BR6-KET-AR-CO | group | ketone_aromatic | 1640-1700 | 29 | 0.48 | 0.83 | 2.9 [1.9, 4.5] | [1.4, 4.7] | 0.62 [0.44, 0.88] | 1.4 | carboxylic_acid_aromatic OR=36.7 (n=3); amides OR=9.7 (n=26); amide_secondary OR=8.2 (n=19) |
| SMITH-BR6-KET-SAT-CCC | group | ketone_saturated | 1100-1230 | 12 | 0.50 | 0.48 | 1.0 [0.5, 1.7] | [0.3, 1.5] | 1.04 [0.58, 1.85] | 1.0 | amine_secondary_saturated OR=10.5 (n=5); phenol OR=4.9 (n=12); ether_mixed OR=4.6 (n=49) |
| SMITH-BR6-KET-SAT-CO | group | ketone_saturated | 1705-1725 | 12 | 0.67 | 0.87 | 5.2 [3.2, 8.3] | [2.2, 9.0] | 0.38 [0.17, 0.85] | 2.4 | ester_aromatic OR=29.5 (n=27); esters OR=22.2 (n=34); alkene_disubstituted OR=7.7 (n=15) |
| SMITH-BR4-CH3-UMBRELLA | group | methyl | 1365-1385 | 261 | 0.63 | 0.58 | 1.5 [1.2, 1.9] | [1.2, 1.9] | 0.64 [0.52, 0.80] | 1.5 | aromatics OR=7.0 (n=52); ketone_aromatic OR=6.6 (n=6); amine_secondary OR=5.4 (n=5) |
| SMITH-BR4-CH3-SYM | group | methyl | 2862-2882 | 261 | 0.27 | 0.91 | 3.0 [1.7, 5.5] | [1.6, 10.1] | 0.80 [0.73, 0.88] | 3.0 | alkene OR=3.0 (n=3); carbonyl_any OR=1.9 (n=4); methylene OR=1.5 (n=6) |
| SMITH-BR4-CH3-ASYM | group | methyl | 2952-2972 | 261 | 0.45 | 0.89 | 3.9 [2.4, 6.6] | [2.4, 9.0] | 0.62 [0.55, 0.71] | 3.9 | carbonyl_any OR=1.8 (n=5); methylene OR=1.7 (n=8); aromatic_mono OR=1.7 (n=5) |
| SMITH-BR4-CH2-SYM | group | methylene | 2845-2865 | 238 | 0.46 | 0.75 | 1.9 [1.4, 2.6] | [1.3, 2.9] | 0.71 [0.61, 0.83] | 1.9 | amine_primary_aromatic OR=5.0 (n=6); amine_primary OR=4.1 (n=6); aromatic_para OR=1.7 (n=16) |
| SMITH-BR4-CH2-ASYM | group | methylene | 2916-2936 | 238 | 0.76 | 0.52 | 1.6 [1.3, 1.9] | [1.3, 1.9] | 0.47 [0.36, 0.61] | 1.6 | amine_primary OR=2.9 (n=8); amine_primary_aromatic OR=2.5 (n=7); alkane OR=2.4 (n=25) |
| SMITH-BR4-CH2-ROCK | group | methylene_chain_4 | 710-730 | 32 | 0.72 | 0.42 | 1.2 [1.0, 1.6] | [0.9, 1.6] | 0.67 [0.38, 1.18] | 1.2 | nitriles OR=5.4 (n=23); nitrile_aromatic OR=4.9 (n=21); aromatic_ortho OR=2.3 (n=22) |
| SMITH-BR8-NH-ANY | class | n_h_any | 3300-3500 | 87 | 0.64 | 0.68 | 2.0 [1.6, 2.6] | [1.5, 2.7] | 0.52 [0.39, 0.70] | 2.0 | alcohol_secondary OR=9.5 (n=13); alkene_disubstituted OR=4.9 (n=21); alkene OR=3.4 (n=34) |
| SMITH-NIT19-AR-CN | group | nitrile_aromatic | 2220-2240 | 24 | 0.04 | 1.00 | 43.3 [1.8, 1036.4] | [9.1, 146.9] | 0.94 [0.85, 1.04] | 10.0 |  |
| SMITH-NIT19-SAT-CN | group | nitrile_saturated | 2240-2260 | 2 (underpowered) | 0.00 | 1.00 | 127.7 [3.0, 5438.2] |  | 0.83 [0.50, 1.38] | 11.2 |  |
| SMITH-NO2-20-SCIS | group | nitro | 835-890 | 18 | 0.94 | 0.46 | 1.7 [1.5, 2.0] | [1.4, 2.0] | 0.12 [0.02, 0.82] | 1.1 | carboxylic_acid_aromatic OR=6.0 (n=3); alkene_disubstituted OR=2.4 (n=25); alkyl_halides OR=2.4 (n=70) |
| SMITH-NO2-20-SYM | group | nitro | 1330-1390 | 18 | 0.83 | 0.85 | 5.8 [4.2, 8.0] | [3.8, 8.1] | 0.19 [0.07, 0.55] | 1.1 | amine_secondary_aromatic OR=3.6 (n=7); alkyne_terminal OR=2.8 (n=3); ketone_aromatic OR=2.5 (n=8) |
| SMITH-NO2-20-ASYM | group | nitro | 1500-1550 | 18 | 0.72 | 0.80 | 3.6 [2.5, 5.2] | [2.1, 6.0] | 0.35 [0.16, 0.73] | 1.5 | n_h_any OR=6.1 (n=39); amine_secondary_aromatic OR=5.5 (n=11); amine_secondary OR=4.6 (n=13) |
| SMITH-BR5-PHENOL-CO | group | phenol | 1200-1260 | 14 | 1.00 | 0.08 | 1.1 [0.9, 1.2] | [1.0, 1.1] | 0.41 [0.03, 6.32] | 1.1 | amine_secondary OR=5.4 (n=27); nitriles OR=5.1 (n=26); ether_saturated OR=5.1 (n=26) |

## Stratum: salt (n = 5)

| rule | tier | truth group | window | n+ | sens | spec | LR+ [CI] | LR+ boot | LR- [CI] | LR+ pos | FP enriched in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SMITH-SALT19-NH3-SYM | group | ammonium_primary | 1500-1550 | 0 (underpowered) | nan | 0.20 | 0.7 [0.1, 5.0] |  | 2.00 [0.18, 22.06] | 0.7 |  |
| SMITH-SALT19-NH3-ASYM | group | ammonium_primary | 1560-1625 | 0 (underpowered) | nan | 0.00 | 0.6 [0.1, 3.9] |  | 6.00 [0.22, 162.54] | 0.6 |  |
| SMITH-SALT19-NH3-STR | group | ammonium_primary | 2800-3200 | 0 (underpowered) | nan | 0.00 | 0.6 [0.1, 3.9] |  | 6.00 [0.22, 162.54] | 0.6 |  |
| SMITH-SALT19-NH2-BEND | group | ammonium_secondary | 1560-1620 | 0 (underpowered) | nan | 0.00 | 0.6 [0.1, 3.9] |  | 6.00 [0.22, 162.54] | 0.6 |  |
| SMITH-SALT19-NH2-STR | group | ammonium_secondary | 2700-3000 | 0 (underpowered) | nan | 0.00 | 0.6 [0.1, 3.9] |  | 6.00 [0.22, 162.54] | 0.6 |  |
| SMITH-SALT19-NH-STR | group | ammonium_tertiary | 2300-2700 | 0 (underpowered) | nan | 0.40 | 0.9 [0.1, 6.8] |  | 1.20 [0.14, 10.58] | 0.9 |  |

## Prominence sweep (LR+, full definition, main stratum)

| rule | p>=0.01 | p>=0.02 | p>=0.05 | p>=0.1 |
| --- | --- | --- | --- | --- |
| SMITH-ALD17-AR-CO | 3.2 | 3.2 | 3.2 | 2.7 |
| SMITH-ALD17-CH-BEND | 1.1 | 1.1 | 1.5 | 1.1 |
| SMITH-ALD17-CH-STR | 1.4 | 1.4 | 1.8 | 1.2 |
| SMITH-ALD17-SAT-CO | 6.5 | 6.5 | 6.5 | 6.8 |
| SMITH-ALK16-CC-STR | 0.8 | 0.9 | 0.9 | 0.8 |
| SMITH-ALK16-CH-STR | 1.0 | 0.9 | 1.0 | 0.5 |
| SMITH-ALK16-TRISUB-CC | 2.9 | 3.6 | 4.0 | 3.8 |
| SMITH-ALK16-TRISUB-WAG | 1.1 | 1.2 | 1.3 | 1.4 |
| SMITH-ALK16-VINYL-CC | 1.2 | 1.5 | 1.9 | 1.7 |
| SMITH-ALK16-VINYL-WAG1 | 1.1 | 1.2 | 0.5 | 0.7 |
| SMITH-ALK16-VINYL-WAG2 | 1.9 | 1.8 | 2.2 | 2.5 |
| SMITH-ALY17-INT-CC | 1.5 | 3.3 | 6.8 | 8.1 |
| SMITH-ALY17-TERM-CC | 1.6 | 2.9 | 5.0 | 1.8 |
| SMITH-ALY17-TERM-CH | 2.2 | 3.0 | 3.9 | 5.4 |
| SMITH-ALY17-TERM-CH-BEND | 1.1 | 1.1 | 1.0 | 0.7 |
| SMITH-BR4-BZ-META-690 | 1.3 | 1.4 | 1.8 | 2.1 |
| SMITH-BR4-BZ-META-BOTH | 1.4 | 1.6 | 2.1 | 2.6 |
| SMITH-BR4-BZ-META-OOP | 1.1 | 1.1 | 1.2 | 1.3 |
| SMITH-BR4-BZ-MONO-690 | 1.6 | 1.7 | 2.3 | 3.4 |
| SMITH-BR4-BZ-MONO-BOTH | 1.6 | 1.8 | 2.5 | 3.8 |
| SMITH-BR4-BZ-MONO-OOP | 1.0 | 1.1 | 1.1 | 1.1 |
| SMITH-BR4-BZ-ORTHO-OOP | 0.5 | 0.7 | 0.8 | 1.2 |
| SMITH-BR4-BZ-PARA-OOP | 1.1 | 1.1 | 1.1 | 1.3 |
| SMITH-BR4-CH2-ASYM | 1.4 | 1.6 | 2.6 | 4.0 |
| SMITH-BR4-CH2-ROCK | 1.1 | 1.2 | 1.3 | 1.5 |
| SMITH-BR4-CH2-SYM | 1.4 | 1.9 | 4.2 | 8.0 |
| SMITH-BR4-CH3-ASYM | 2.7 | 3.9 | 4.9 | 7.0 |
| SMITH-BR4-CH3-SYM | 3.0 | 3.0 | 2.1 | 0.9 |
| SMITH-BR4-CH3-UMBRELLA | 1.5 | 1.5 | 1.6 | 2.1 |
| SMITH-BR5-CO-GENERAL | 1.4 | 1.4 | 1.4 | 1.4 |
| SMITH-BR5-ETHER-ARYL-CO | 0.8 | 0.8 | 0.9 | 0.9 |
| SMITH-BR5-ETHER-MIX-CO-AR | 1.0 | 1.0 | 1.0 | 1.0 |
| SMITH-BR5-ETHER-MIX-CO-SAT | 1.0 | 1.1 | 1.2 | 1.3 |
| SMITH-BR5-ETHER-SAT-CO | 0.9 | 0.9 | 1.0 | 1.0 |
| SMITH-BR5-PHENOL-CO | 1.0 | 1.1 | 1.2 | 1.2 |
| SMITH-BR5-ROH-OH-STR | 0.9 | 1.3 | 1.9 | 2.8 |
| SMITH-BR5-ROH-OH-WAG | 0.9 | 0.9 | 1.0 | 0.9 |
| SMITH-BR5-ROH-PRIM-CO | 0.8 | 0.8 | 0.8 | 0.9 |
| SMITH-BR5-ROH-SEC-CO | 1.0 | 1.0 | 0.9 | 0.9 |
| SMITH-BR5-ROH-TERT-CO | 0.8 | 0.8 | 0.8 | 0.3 |
| SMITH-BR6-ACID-AR-CO | 6.9 | 6.9 | 6.9 | 7.0 |
| SMITH-BR6-ACID-CO | 0.9 | 0.9 | 1.0 | 1.0 |
| SMITH-BR6-ACID-OH-IPB | 1.1 | 1.1 | 1.1 | 1.3 |
| SMITH-BR6-ACID-OH-OOP | 1.0 | 1.1 | 1.1 | 0.7 |
| SMITH-BR6-ACID-OH-STR | 2.9 | 2.9 | 2.9 | 2.9 |
| SMITH-BR6-ACID-SAT-CO | 1.3 | 1.3 | 1.3 | 1.3 |
| SMITH-BR6-CO-GENERAL | 5.1 | 5.1 | 5.1 | 5.1 |
| SMITH-BR6-KET-AR-CCC | 1.4 | 1.4 | 1.4 | 1.4 |
| SMITH-BR6-KET-AR-CO | 2.9 | 2.9 | 2.9 | 3.0 |
| SMITH-BR6-KET-SAT-CCC | 0.9 | 1.0 | 1.0 | 1.0 |
| SMITH-BR6-KET-SAT-CO | 5.2 | 5.2 | 5.3 | 4.7 |
| SMITH-BR7-CARB-AR-CO | 385.0 | 385.0 | 385.0 | 385.0 |
| SMITH-BR7-CARB-AR-OCO | 3.2 | 3.3 | 3.4 | 3.4 |
| SMITH-BR7-CARB-MIX-CO | 77.0 | 77.0 | 77.0 | 77.0 |
| SMITH-BR7-CARB-MIX-OCO | 1.9 | 1.9 | 2.0 | 2.1 |
| SMITH-BR7-CARB-OCC | 2.6 | 2.6 | 2.6 | 2.6 |
| SMITH-BR7-CARB-SAT-CO | 8.2 | 8.2 | 8.2 | 8.2 |
| SMITH-BR7-CARB-SAT-OCO | 2.2 | 2.2 | 2.2 | 2.3 |
| SMITH-BR7-EST-AR-CCO | 5.0 | 5.0 | 5.2 | 5.2 |
| SMITH-BR7-EST-AR-CO | 5.2 | 5.2 | 5.2 | 5.7 |
| SMITH-BR7-EST-AR-OCC | 2.8 | 2.5 | 2.4 | 2.5 |
| SMITH-BR7-EST-SAT-CCO | 1.5 | 1.5 | 1.5 | 1.5 |
| SMITH-BR7-EST-SAT-CO | 26.3 | 26.3 | 26.3 | 26.3 |
| SMITH-BR7-EST-SAT-OCC | 1.0 | 1.0 | 1.0 | 1.0 |
| SMITH-BR8-AMD-CO | 4.7 | 4.9 | 5.4 | 5.2 |
| SMITH-BR8-AMD1-CN | 1.0 | 1.0 | 1.2 | 1.4 |
| SMITH-BR8-AMD1-NH-STR | 1.6 | 2.1 | 0.9 | 1.2 |
| SMITH-BR8-AMD1-SCIS | 0.7 | 0.8 | 1.3 | 1.7 |
| SMITH-BR8-AMD1-WAG | 0.8 | 0.8 | 0.8 | 0.9 |
| SMITH-BR8-AMD2-CN | 0.9 | 0.9 | 1.0 | 0.9 |
| SMITH-BR8-AMD2-NH-IPB | 2.2 | 2.0 | 2.0 | 2.1 |
| SMITH-BR8-AMD2-NH-STR | 2.3 | 3.0 | 4.2 | 4.2 |
| SMITH-BR8-AMD2-WAG | 1.0 | 1.0 | 1.0 | 1.0 |
| SMITH-BR8-AMN1-AR-ASYM | 2.9 | 6.8 | 10.5 | 14.1 |
| SMITH-BR8-AMN1-AR-CN | 1.0 | 1.0 | 1.0 | 1.1 |
| SMITH-BR8-AMN1-AR-SYM | 1.5 | 3.2 | 5.3 | 6.7 |
| SMITH-BR8-AMN1-SAT-ASYM | 7.2 | 17.2 | 7.5 | 7.5 |
| SMITH-BR8-AMN1-SAT-CN | 0.8 | 0.8 | 0.8 | 0.8 |
| SMITH-BR8-AMN1-SAT-SYM | 1.0 | 1.5 | 2.0 | 2.8 |
| SMITH-BR8-AMN1-SCIS | 1.1 | 1.1 | 1.2 | 1.4 |
| SMITH-BR8-AMN1-WAG | 1.0 | 1.0 | 1.0 | 1.1 |
| SMITH-BR8-AMN2-AR-CNC | 1.0 | 1.0 | 1.1 | 1.2 |
| SMITH-BR8-AMN2-AR-NH | 1.5 | 2.5 | 5.7 | 6.6 |
| SMITH-BR8-AMN2-SAT-CNC | 1.0 | 1.0 | 1.1 | 1.3 |
| SMITH-BR8-AMN2-SAT-NH | 3.9 | 2.5 | 0.6 | 0.9 |
| SMITH-BR8-AMN2-WAG | 1.1 | 1.0 | 1.0 | 1.0 |
| SMITH-BR8-NH-ANY | 1.3 | 2.0 | 3.7 | 4.5 |
| SMITH-BZ16-ARCH-STR | 2.3 | 2.0 | 1.1 | 1.4 |
| SMITH-BZ16-OOP | 1.0 | 1.0 | 1.1 | 1.1 |
| SMITH-BZ16-RING | 1.0 | 1.0 | 1.1 | 1.0 |
| SMITH-NIT19-AR-CN | 43.3 | 43.3 | 43.3 | 43.3 |
| SMITH-NIT19-SAT-CN | 127.7 | 127.7 | 127.7 | 127.7 |
| SMITH-NO2-20-ASYM | 3.6 | 3.6 | 3.6 | 3.7 |
| SMITH-NO2-20-SCIS | 1.7 | 1.7 | 1.8 | 1.9 |
| SMITH-NO2-20-SYM | 5.7 | 5.8 | 5.9 | 6.0 |

## Not evaluable (5 rules)

- SMITH-ALK16-CIS-CC: cis alkene.  NOT EVALUABLE: cis/trans needs stereo marks that most depositor SMILES lack (decision D6)
- SMITH-ALK16-CIS-WAG: cis alkene. Wide tolerance in the source (+-50) NOT EVALUABLE: cis/trans needs stereo marks that most depositor SMILES lack (decision D6)
- SMITH-ALK16-TRANS-CC: trans alkene.  NOT EVALUABLE: cis/trans needs stereo marks that most depositor SMILES lack (decision D6)
- SMITH-ALK16-TRANS-WAG: trans alkene.  NOT EVALUABLE: cis/trans needs stereo marks that most depositor SMILES lack (decision D6)
- SMITH-SALT19-COMB: amine salt. All three salt types. This is the window where salts mimic alkynes and nitriles (an IR trap for the analysis)
