# Rule metrics, dataset = nist, split = confirm

**Confirmatory run on the frozen rule table.**

Primary prominence threshold 0.02; full definition (position, intensity, shape). `LR+ [CI]` is the analytic 95 percent interval; `boot` is the scaffold-cluster bootstrap interval (500 resamples); `LR+ pos` is the same rule scored by position only. Rules with fewer than 10 positives are marked underpowered.

## Stratum: main (n up to 5124; each rule is scored on the spectra whose measured range covers its windows)

| rule | tier | truth group | window | n+ | sens | spec | LR+ [CI] | LR+ boot | LR- [CI] | LR+ pos | FP enriched in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SMITH-BR5-ROH-PRIM-CO | group | alcohol_primary | 1000-1075 | 232 | 0.97 | 0.14 | 1.1 [1.1, 1.2] | [1.1, 1.2] | 0.18 [0.08, 0.39] | 1.1 | aromatic_ortho OR=5.2 (n=245); alkene_trisubstituted OR=5.1 (n=132); ether_mixed OR=4.7 (n=323) |
| SMITH-BR5-ROH-SEC-CO | group | alcohol_secondary | 1075-1150 | 259 | 0.96 | 0.15 | 1.1 [1.1, 1.2] | [1.1, 1.2] | 0.23 [0.12, 0.44] | 1.1 | ester_aromatic OR=12.4 (n=166); ether_saturated OR=6.6 (n=193); aromatic_para OR=5.1 (n=613) |
| SMITH-BR5-ROH-TERT-CO | group | alcohol_tertiary | 1100-1210 | 94 | 1.00 | 0.07 | 1.1 [1.1, 1.1] | [1.0, 1.1] | 0.08 [0.00, 1.25] | 1.1 | ester_aromatic OR=25.3 (n=169); ether_mixed OR=17.7 (n=343); amine_secondary OR=14.1 (n=278) |
| SMITH-BR5-ROH-OH-WAG | group | alcohols | 600-700 | 391 | 0.59 | 0.42 | 1.0 [0.9, 1.1] | [0.9, 1.1] | 0.97 [0.84, 1.11] | 1.0 | aromatic_meta OR=17.7 (n=34); aromatic_mono OR=11.2 (n=200); aromatics OR=4.7 (n=545) |
| SMITH-BR5-ROH-OH-STR | group | alcohols | 3300-3400 | 1194 | 0.34 | 0.76 | 1.5 [1.3, 1.6] | [1.2, 1.8] | 0.86 [0.82, 0.90] | 1.5 | n_h_any OR=15.5 (n=697); amide_primary OR=14.0 (n=70); amine_primary OR=11.7 (n=283) |
| SMITH-ALD17-AR-CO | group | aldehyde_aromatic | 1685-1710 | 44 | 0.27 | 0.91 | 3.0 [1.8, 4.8] | [0.7, 4.0] | 0.80 [0.67, 0.96] | 2.4 | carbonyl_any OR=10.9 (n=412); carboxylic_acids OR=6.6 (n=113); carboxylic_acid_saturated OR=6.6 (n=77) |
| SMITH-ALD17-SAT-CO | group | aldehyde_saturated | 1720-1740 | 18 | 0.61 | 0.90 | 6.3 [4.3, 9.3] | [2.5, 9.9] | 0.43 [0.24, 0.77] | 5.5 | carbonyl_any OR=64.1 (n=481); esters OR=13.6 (n=271); ester_saturated OR=11.2 (n=191) |
| SMITH-ALD17-CH-BEND | group | aldehydes | 1380-1400 | 72 | 0.60 | 0.57 | 1.4 [1.1, 1.7] | [0.9, 1.7] | 0.71 [0.53, 0.94] | 1.4 | carbonate_organic OR=4.0 (n=16); methyl OR=2.2 (n=1558); alkane OR=1.5 (n=1590) |
| SMITH-ALD17-CH-STR | group | aldehydes | 2700-2850 | 72 | 0.69 | 0.80 | 3.4 [2.9, 4.0] | [2.7, 3.9] | 0.38 [0.27, 0.54] | 3.4 | ammonium_primary OR=35.1 (n=4); amine_secondary_saturated OR=7.2 (n=47); alkyne_internal OR=3.2 (n=4) |
| SMITH-ALK16-CC-STR | class | alkene | 1630-1680 | 618 | 0.60 | 0.72 | 2.1 [2.0, 2.3] | [1.6, 2.5] | 0.56 [0.51, 0.62] | 2.1 | amide_primary OR=21.3 (n=89); amides OR=7.3 (n=384); amide_secondary OR=6.6 (n=211) |
| SMITH-ALK16-CH-STR | class | alkene | 3000-3100 | 618 | 0.45 | 0.64 | 1.2 [1.1, 1.4] | [0.8, 1.7] | 0.86 [0.80, 0.93] | 1.2 | aromatics OR=4.3 (n=1411); ether_aryl OR=3.6 (n=59); aromatic_mono OR=3.1 (n=496) |
| SMITH-ALK16-TRISUB-WAG | group | alkene_trisubstituted | 790-840 | 158 | 0.75 | 0.34 | 1.1 [1.0, 1.2] | [0.9, 1.3] | 0.75 [0.57, 0.98] | 1.1 | aromatic_para OR=4.5 (n=566); ether_mixed OR=4.1 (n=301); aldehyde_aromatic OR=3.7 (n=39) |
| SMITH-ALK16-TRISUB-CC | group | alkene_trisubstituted | 1660-1680 | 158 | 0.36 | 0.88 | 2.9 [2.4, 3.6] | [1.9, 3.9] | 0.73 [0.65, 0.82] | 2.9 | amide_primary OR=7.7 (n=50); aldehyde_aromatic OR=5.6 (n=19); amides OR=4.4 (n=198) |
| SMITH-ALK16-VINYL-WAG2 | group | alkene_vinyl | 905-915 | 91 | 0.26 | 0.83 | 1.6 [1.1, 2.3] | [1.2, 2.4] | 0.88 [0.78, 1.00] | 1.6 | alcohol_tertiary OR=3.5 (n=37); alkyne_terminal OR=2.8 (n=8); alkyne OR=2.1 (n=9) |
| SMITH-ALK16-VINYL-WAG1 | group | alkene_vinyl | 985-995 | 91 | 0.53 | 0.87 | 4.0 [3.3, 5.0] | [2.8, 5.3] | 0.54 [0.44, 0.68] | 4.0 | alcohol_tertiary OR=2.7 (n=26); alkene_trisubstituted OR=2.5 (n=41); alcohol_secondary OR=2.1 (n=59) |
| SMITH-ALK16-VINYL-CC | group | alkene_vinyl | 1630-1660 | 91 | 0.74 | 0.79 | 3.4 [3.0, 3.9] | [1.4, 4.1] | 0.34 [0.24, 0.47] | 3.4 | amide_primary OR=5.5 (n=59); amine_primary_aromatic OR=4.2 (n=181); alkene_trisubstituted OR=3.7 (n=76) |
| SMITH-ALY17-INT-CC | group | alkyne_internal | 2190-2260 | 9 (underpowered) | 0.33 | 0.94 | 5.9 [2.3, 14.9] |  | 0.71 [0.45, 1.12] | 5.9 |  |
| SMITH-ALY17-TERM-CH-BEND | group | alkyne_terminal | 600-700 | 1 (underpowered) | 1.00 | 0.42 | 1.3 [0.6, 2.9] |  | 0.59 [0.05, 6.56] | 1.3 |  |
| SMITH-ALY17-TERM-CC | group | alkyne_terminal | 2100-2140 | 23 | 0.35 | 0.97 | 11.9 [6.7, 21.3] | [4.7, 16.0] | 0.67 [0.50, 0.91] | 11.9 | amine_primary_saturated OR=6.8 (n=17); amine_primary OR=5.0 (n=49); amine_primary_aromatic OR=3.7 (n=31) |
| SMITH-ALY17-TERM-CH | group | alkyne_terminal | 3250-3350 | 23 | 0.96 | 0.79 | 4.5 [4.0, 5.0] | [3.8, 5.1] | 0.06 [0.01, 0.38] | 4.5 | n_h_any OR=10.0 (n=734); amine_secondary_saturated OR=8.4 (n=51); amines OR=7.0 (n=505) |
| SMITH-BR8-AMD1-WAG | group | amide_primary | 600-750 | 39 | 0.95 | 0.16 | 1.1 [1.1, 1.2] | [1.0, 1.2] | 0.32 [0.08, 1.24] | 1.1 | aromatic_mono OR=105.7 (n=229); aromatic_meta OR=18.0 (n=45); carboxylic_acid_aromatic OR=15.2 (n=38) |
| SMITH-BR8-AMD1-CN | group | amide_primary | 1390-1430 | 100 | 0.78 | 0.42 | 1.4 [1.2, 1.5] | [1.1, 1.5] | 0.52 [0.36, 0.76] | 1.4 | ammonium_primary OR=6.6 (n=4); carboxylic_acid_saturated OR=3.8 (n=173); alkene_vinyl OR=3.4 (n=75) |
| SMITH-BR8-AMD1-SCIS | group | amide_primary | 1620-1650 | 100 | 0.54 | 0.74 | 2.1 [1.8, 2.6] | [1.4, 2.7] | 0.62 [0.50, 0.76] | 2.1 | alkene_vinyl OR=10.7 (n=71); amine_primary_aromatic OR=6.5 (n=230); amine_primary OR=4.3 (n=264) |
| SMITH-BR8-AMD1-NH-STR | group | amide_primary | 3170-3370 | 100 | 0.93 | 0.68 | 2.9 [2.8, 3.1] | [2.6, 3.2] | 0.10 [0.05, 0.21] | 2.9 | alkyne_terminal OR=103.0 (n=23); n_h_any OR=11.8 (n=943); amines OR=8.6 (n=660) |
| SMITH-BR8-AMD2-WAG | group | amide_secondary | 680-750 | 354 | 0.86 | 0.21 | 1.1 [1.0, 1.1] | [1.0, 1.2] | 0.70 [0.54, 0.91] | 1.1 | aromatic_mono OR=43.3 (n=845); ether_aryl OR=9.3 (n=87); aromatic_ortho OR=5.5 (n=231) |
| SMITH-BR8-AMD2-CN | group | amide_secondary | 1230-1310 | 356 | 0.95 | 0.11 | 1.1 [1.0, 1.1] | [1.0, 1.1] | 0.45 [0.28, 0.71] | 1.1 | ester_aromatic OR=44.0 (n=166); ketone_aromatic OR=7.7 (n=203); ether_aryl OR=7.6 (n=88) |
| SMITH-BR8-AMD2-NH-IPB | group | amide_secondary | 1515-1570 | 356 | 0.39 | 0.85 | 2.6 [2.2, 3.0] | [1.5, 3.9] | 0.72 [0.66, 0.78] | 1.6 | nitro OR=10.7 (n=208); aromatics OR=7.4 (n=662); n_h_any OR=3.8 (n=330) |
| SMITH-BR8-AMD2-NH-STR | group | amide_secondary | 3170-3370 | 356 | 0.77 | 0.70 | 2.6 [2.4, 2.8] | [2.1, 3.0] | 0.33 [0.27, 0.40] | 2.6 | alkyne_terminal OR=113.9 (n=23); amide_primary OR=30.7 (n=90); n_h_any OR=11.9 (n=762) |
| SMITH-BR8-AMD-CO | group | amides | 1630-1680 | 635 | 0.51 | 0.87 | 4.0 [3.6, 4.4] | [2.2, 5.6] | 0.57 [0.52, 0.61] | 2.4 | ketone_aromatic OR=6.5 (n=92); ketones OR=6.5 (n=175); alkene_trisubstituted OR=6.3 (n=67) |
| SMITH-BR8-AMN1-WAG | group | amine_primary | 750-850 | 490 | 0.96 | 0.12 | 1.1 [1.1, 1.1] | [1.0, 1.2] | 0.35 [0.23, 0.53] | 1.1 | aromatic_para OR=64.0 (n=583); ether_aryl OR=24.7 (n=85); carboxylic_acid_aromatic OR=23.2 (n=80) |
| SMITH-BR8-AMN1-SCIS | group | amine_primary | 1580-1650 | 490 | 0.96 | 0.34 | 1.4 [1.4, 1.5] | [1.2, 1.9] | 0.11 [0.07, 0.17] | 1.4 | amine_secondary_aromatic OR=36.1 (n=167); ether_aryl OR=29.5 (n=84); aromatics OR=16.5 (n=2592) |
| SMITH-BR8-AMN1-AR-CN | group | amine_primary_aromatic | 1250-1350 | 361 | 0.98 | 0.09 | 1.1 [1.1, 1.1] | [1.0, 1.1] | 0.24 [0.12, 0.48] | 1.1 | ketone_aromatic OR=42.2 (n=197); ether_mixed OR=14.2 (n=323); ester_aromatic OR=11.0 (n=156) |
| SMITH-BR8-AMN1-AR-SYM | group | amine_primary_aromatic | 3340-3420 | 361 | 0.63 | 0.79 | 3.0 [2.8, 3.3] | [2.3, 3.5] | 0.46 [0.40, 0.53] | 3.0 | amide_primary OR=8.9 (n=63); n_h_any OR=3.7 (n=426); alcohol_primary OR=3.5 (n=103) |
| SMITH-BR8-AMN1-AR-ASYM | group | amine_primary_aromatic | 3420-3500 | 361 | 0.48 | 0.84 | 3.0 [2.7, 3.4] | [1.8, 4.1] | 0.61 [0.55, 0.68] | 3.0 | aldehyde_saturated OR=5.3 (n=9); ketone_saturated OR=3.1 (n=62); alcohol_tertiary OR=3.0 (n=33) |
| SMITH-BR8-AMN1-SAT-CN | group | amine_primary_saturated | 1020-1250 | 111 | 1.00 | 0.01 | 1.0 [1.0, 1.0] | [1.0, 1.0] | 0.43 [0.03, 6.86] | 1.0 | aromatic_mono OR=23.9 (n=918); esters OR=15.8 (n=650); aromatics OR=14.8 (n=3345) |
| SMITH-BR8-AMN1-SAT-SYM | group | amine_primary_saturated | 3280-3310 | 111 | 0.20 | 0.93 | 2.7 [1.9, 4.0] | [0.7, 4.0] | 0.86 [0.79, 0.95] | 2.7 | alkyne_terminal OR=8.6 (n=9); alkyne OR=8.0 (n=12); alkyne_internal OR=6.9 (n=3) |
| SMITH-BR8-AMN1-SAT-ASYM | group | amine_primary_saturated | 3350-3380 | 111 | 0.21 | 0.91 | 2.3 [1.6, 3.4] | [0.8, 3.6] | 0.87 [0.79, 0.96] | 2.3 | amide_primary OR=7.4 (n=38); n_h_any OR=4.9 (n=265); amine_primary_aromatic OR=4.1 (n=91) |
| SMITH-BR8-AMN2-WAG | group | amine_secondary | 700-750 | 281 | 0.72 | 0.30 | 1.0 [1.0, 1.1] | [0.9, 1.1] | 0.91 [0.75, 1.11] | 1.0 | aromatic_ortho OR=3.9 (n=211); ketone_aromatic OR=3.5 (n=186); nitro OR=3.4 (n=330) |
| SMITH-BR8-AMN2-AR-CNC | group | amine_secondary_aromatic | 1250-1350 | 191 | 0.98 | 0.09 | 1.1 [1.1, 1.1] | [1.0, 1.2] | 0.17 [0.06, 0.54] | 1.1 | ketone_aromatic OR=43.8 (n=210); ether_mixed OR=14.5 (n=339); ester_aromatic OR=11.2 (n=163) |
| SMITH-BR8-AMN2-AR-NH | group | amine_secondary_aromatic | 3380-3420 | 191 | 0.24 | 0.88 | 1.9 [1.5, 2.5] | [1.2, 2.5] | 0.87 [0.80, 0.94] | 1.9 | amine_primary_aromatic OR=4.7 (n=123); amine_primary OR=4.0 (n=148); amide_primary OR=2.9 (n=28) |
| SMITH-BR8-AMN2-SAT-CNC | group | amine_secondary_saturated | 1130-1180 | 74 | 0.73 | 0.26 | 1.0 [0.9, 1.1] | [0.9, 1.1] | 1.03 [0.71, 1.51] | 1.0 | ether_aryl OR=5.6 (n=84); ketone_saturated OR=3.7 (n=158); alcohol_tertiary OR=3.6 (n=84) |
| SMITH-BR8-AMN2-SAT-NH | group | amine_secondary_saturated | 3280-3320 | 74 | 0.41 | 0.91 | 4.3 [3.2, 5.7] | [2.9, 5.4] | 0.66 [0.54, 0.79] | 4.3 | alkyne_terminal OR=12.5 (n=13); alkyne OR=9.8 (n=16); n_h_any OR=5.8 (n=304) |
| SMITH-BR4-BZ-META-690 | group | aromatic_meta | 680-700 | 141 | 0.67 | 0.61 | 1.7 [1.5, 1.9] | [1.4, 2.8] | 0.54 [0.43, 0.69] | 1.7 | aromatic_mono OR=22.0 (n=811); aromatics OR=3.9 (n=1583); ether_aryl OR=3.0 (n=51) |
| SMITH-BR4-BZ-META-OOP | group | aromatic_meta | 750-810 | 141 | 0.96 | 0.25 | 1.3 [1.2, 1.3] | [1.2, 1.5] | 0.14 [0.06, 0.33] | 1.3 | carboxylic_acid_aromatic OR=19.1 (n=82); ketone_aromatic OR=4.8 (n=196); carbonate_organic OR=4.7 (n=20) |
| SMITH-BR4-BZ-META-BOTH | group | aromatic_meta | 750-810 +680-700 | 141 | 0.65 | 0.68 | 2.0 [1.8, 2.3] | [1.6, 3.3] | 0.51 [0.41, 0.64] | 2.0 | aromatic_mono OR=11.0 (n=689); aromatics OR=4.5 (n=1355); ether_aryl OR=3.4 (n=48) |
| SMITH-BR4-BZ-MONO-690 | group | aromatic_mono | 680-700 | 924 | 0.89 | 0.71 | 3.1 [3.0, 3.3] | [2.6, 3.9] | 0.15 [0.12, 0.18] | 3.1 | aromatic_meta OR=4.5 (n=79); ester_aromatic OR=2.6 (n=62); carboxylic_acid_aromatic OR=2.4 (n=41) |
| SMITH-BR4-BZ-MONO-OOP | group | aromatic_mono | 710-770 | 928 | 0.93 | 0.25 | 1.2 [1.2, 1.3] | [1.1, 1.3] | 0.27 [0.21, 0.34] | 1.2 | aromatic_ortho OR=21.9 (n=217); nitro OR=7.1 (n=340); carboxylic_acid_aromatic OR=5.0 (n=81) |
| SMITH-BR4-BZ-MONO-BOTH | group | aromatic_mono | 710-770 +680-700 | 924 | 0.84 | 0.77 | 3.7 [3.5, 3.9] | [2.9, 4.8] | 0.21 [0.18, 0.24] | 3.7 | aromatic_meta OR=4.1 (n=67); ester_aromatic OR=3.1 (n=58); carboxylic_acid_aromatic OR=2.8 (n=38) |
| SMITH-BR4-BZ-ORTHO-OOP | group | aromatic_ortho | 735-770 no 680-700 | 258 | 0.50 | 0.70 | 1.7 [1.5, 1.9] | [1.0, 1.9] | 0.71 [0.63, 0.81] | 1.7 | ammonium_primary OR=5.4 (n=3); aldehyde_aromatic OR=2.3 (n=19); nitro OR=1.9 (n=156) |
| SMITH-BR4-BZ-PARA-OOP | group | aromatic_para | 790-860 no 680-700 | 645 | 0.52 | 0.53 | 1.1 [1.0, 1.2] | [0.7, 1.4] | 0.90 [0.83, 0.98] | 1.1 | carbonate_organic OR=3.2 (n=15); aldehyde_aromatic OR=2.6 (n=28); amine_primary_saturated OR=2.1 (n=66) |
| SMITH-BZ16-OOP | class | aromatics | 700-1000 | 3387 | 1.00 | 0.01 | 1.0 [1.0, 1.0] | [1.0, 1.0] | 0.09 [0.02, 0.38] | 1.0 | alkene OR=7.5 (n=396); ketones OR=3.3 (n=202); alkane OR=3.1 (n=1604) |
| SMITH-BZ16-RING | class | aromatics | 1400-1620 | 3387 | 1.00 | 0.02 | 1.0 [1.0, 1.0] | [1.0, 1.0] | 0.06 [0.02, 0.16] | 1.0 | methylene OR=15.1 (n=1437); methyl OR=7.4 (n=1237); ether OR=7.3 (n=158) |
| SMITH-BZ16-ARCH-STR | class | aromatics | 3000-3100 | 3387 | 0.45 | 0.79 | 2.1 [1.9, 2.3] | [1.7, 2.4] | 0.70 [0.67, 0.73] | 2.1 | alkene_vinyl OR=19.0 (n=47); amide_secondary OR=4.9 (n=60); alkene OR=3.6 (n=159) |
| SMITH-BR5-CO-GENERAL | class | c_o_single_any | 1000-1300 | 1623 | 0.72 | 0.54 | 1.6 [1.5, 1.6] | [1.4, 1.7] | 0.52 [0.47, 0.56] | 1.0 | carbonate_organic OR=14.7 (n=18); ester_aromatic OR=6.7 (n=99); esters OR=4.5 (n=354) |
| SMITH-BR7-CARB-OCC | group | carbonate_organic | 1000-1060 | 21 | 0.19 | 0.88 | 1.6 [0.6, 3.8] | [0.5, 2.3] | 0.92 [0.75, 1.13] | 1.1 | alcohol_primary OR=6.7 (n=103); alcohol_secondary OR=4.1 (n=87); alkyne_terminal OR=4.0 (n=8) |
| SMITH-BR7-CARB-AR-OCO | group | carbonate_organic | 1205-1230 | 21 | 0.19 | 0.90 | 1.9 [0.8, 4.5] | [0.2, 6.0] | 0.90 [0.73, 1.11] | 0.8 | ether_aryl OR=8.8 (n=43); phenol OR=3.3 (n=103); esters OR=2.5 (n=127) |
| SMITH-BR7-CARB-MIX-OCO | group | carbonate_organic | 1210-1250 | 21 | 0.29 | 0.82 | 1.6 [0.8, 3.1] | [0.3, 3.2] | 0.87 [0.67, 1.15] | 0.8 | ether_aryl OR=6.3 (n=51); ether_mixed OR=4.4 (n=159); ether OR=3.1 (n=244) |
| SMITH-BR7-CARB-SAT-OCO | group | carbonate_organic | 1240-1280 | 21 | 0.71 | 0.81 | 3.7 [2.8, 4.9] | [1.3, 5.6] | 0.35 [0.18, 0.70] | 1.1 | ester_aromatic OR=5.8 (n=94); ether_mixed OR=5.4 (n=181); ketone_aromatic OR=3.7 (n=98) |
| SMITH-BR7-CARB-SAT-CO | group | carbonate_organic | 1730-1750 | 21 | 0.48 | 0.92 | 5.7 [3.6, 9.0] | [1.4, 9.0] | 0.57 [0.38, 0.86] | 3.9 | carbonyl_any OR=58.7 (n=416); ester_saturated OR=19.6 (n=213); esters OR=17.5 (n=262) |
| SMITH-BR7-CARB-MIX-CO | group | carbonate_organic | 1760-1790 | 21 | 0.19 | 0.97 | 7.4 [3.0, 18.2] | [1.4, 20.1] | 0.83 [0.68, 1.02] | 5.2 | carbonyl_any OR=47.3 (n=128); acyl_halides OR=20.9 (n=10); esters OR=12.9 (n=82) |
| SMITH-BR7-CARB-AR-CO | group | carbonate_organic | 1775-1820 | 21 | 0.14 | 0.98 | 9.6 [3.3, 28.0] | [1.2, 30.4] | 0.87 [0.73, 1.04] | 3.2 | acyl_halides OR=81.5 (n=15); carbonyl_any OR=37.5 (n=74); ester_saturated OR=10.3 (n=36) |
| SMITH-BR6-CO-GENERAL | class | carbonyl_any | 1600-1900 | 2322 | 0.86 | 0.79 | 4.1 [3.8, 4.4] | [3.1, 6.0] | 0.17 [0.15, 0.19] | 1.4 | aromatics OR=8.3 (n=554); amine_primary_aromatic OR=7.2 (n=164); amine_primary OR=5.1 (n=178) |
| SMITH-BR6-ACID-AR-CO | group | carboxylic_acid_aromatic | 1680-1710 | 91 | 0.41 | 0.89 | 3.7 [2.9, 4.8] | [2.5, 4.5] | 0.67 [0.56, 0.79] | 3.5 | carbonyl_any OR=10.5 (n=482); carboxylic_acids OR=6.2 (n=93); carboxylic_acid_saturated OR=6.1 (n=83) |
| SMITH-BR6-ACID-SAT-CO | group | carboxylic_acid_saturated | 1700-1730 | 211 | 0.49 | 0.88 | 4.2 [3.6, 4.9] | [3.6, 5.1] | 0.58 [0.50, 0.66] | 3.0 | carbonyl_any OR=28.1 (n=547); ketone_saturated OR=9.5 (n=88); ester_aromatic OR=5.9 (n=70) |
| SMITH-BR6-ACID-OH-OOP | group | carboxylic_acids | 900-960 | 325 | 0.88 | 0.28 | 1.2 [1.2, 1.3] | [1.1, 1.3] | 0.44 [0.33, 0.59] | 1.2 | alkene_vinyl OR=23.5 (n=87); alcohol_tertiary OR=14.1 (n=87); alkene_trisubstituted OR=4.5 (n=138) |
| SMITH-BR6-ACID-CO | group | carboxylic_acids | 1210-1320 | 325 | 0.97 | 0.07 | 1.0 [1.0, 1.1] | [1.0, 1.1] | 0.42 [0.22, 0.81] | 1.0 | ester_aromatic OR=24.6 (n=168); ether_mixed OR=16.1 (n=320); ether_aryl OR=12.4 (n=86) |
| SMITH-BR6-ACID-OH-IPB | group | carboxylic_acids | 1395-1440 | 325 | 0.86 | 0.38 | 1.4 [1.3, 1.5] | [1.2, 1.5] | 0.36 [0.27, 0.47] | 1.4 | ammonium_primary OR=5.5 (n=4); alkene_vinyl OR=5.3 (n=79); amide_primary OR=3.1 (n=80) |
| SMITH-BR6-ACID-OH-STR | group | carboxylic_acids | 2500-3500 | 325 | 0.44 | 0.62 | 1.2 [1.0, 1.3] | [1.0, 1.4] | 0.90 [0.82, 0.99] | 1.0 | methylene_chain_4 OR=4.3 (n=409); ammonium_primary OR=3.8 (n=3); amine_secondary_saturated OR=3.4 (n=47) |
| SMITH-BR7-EST-AR-OCC | group | ester_aromatic | 1100-1130 | 169 | 0.24 | 0.92 | 2.9 [2.1, 3.8] | [1.9, 4.1] | 0.83 [0.76, 0.91] | 1.4 | ether_saturated OR=12.8 (n=106); ether OR=4.9 (n=153); c_o_single_any OR=2.8 (n=223) |
| SMITH-BR7-EST-AR-CCO | group | ester_aromatic | 1250-1310 | 169 | 0.69 | 0.80 | 3.4 [3.1, 3.9] | [2.6, 4.0] | 0.39 [0.31, 0.49] | 1.2 | carbonate_organic OR=9.1 (n=14); ketone_aromatic OR=5.6 (n=116); carboxylic_acid_aromatic OR=5.2 (n=50) |
| SMITH-BR7-EST-AR-CO | group | ester_aromatic | 1715-1730 | 169 | 0.29 | 0.93 | 4.4 [3.4, 5.7] | [2.3, 6.6] | 0.76 [0.69, 0.84] | 3.4 | carbonyl_any OR=51.4 (n=320); ketone_saturated OR=6.5 (n=49); esters OR=6.4 (n=117) |
| SMITH-BR7-EST-SAT-OCC | group | ester_saturated | 1030-1100 | 440 | 0.18 | 0.85 | 1.2 [1.0, 1.5] | [0.9, 2.0] | 0.97 [0.92, 1.01] | 1.0 | alcohol_primary OR=6.7 (n=108); ether_saturated OR=4.7 (n=87); alcohol_secondary OR=4.5 (n=92) |
| SMITH-BR7-EST-SAT-CCO | group | ester_saturated | 1160-1210 | 440 | 0.38 | 0.84 | 2.4 [2.1, 2.7] | [1.8, 2.8] | 0.74 [0.69, 0.80] | 1.1 | ether_aryl OR=11.1 (n=59); phenol OR=2.9 (n=135); esters OR=2.6 (n=67) |
| SMITH-BR7-EST-SAT-CO | group | ester_saturated | 1735-1755 | 440 | 0.42 | 0.97 | 12.4 [10.3, 15.0] | [7.0, 16.0] | 0.60 [0.55, 0.65] | 6.9 | carbonate_organic OR=33.3 (n=11); carbonyl_any OR=28.8 (n=151); aldehyde_saturated OR=7.0 (n=3) |
| SMITH-BR5-ETHER-ARYL-CO | group | ether_aryl | 1200-1300 | 89 | 1.00 | 0.08 | 1.1 [1.1, 1.1] | [1.0, 1.1] | 0.07 [0.00, 1.14] | 1.1 | ester_aromatic OR=29.7 (n=169); ketone_aromatic OR=12.6 (n=214); phenol OR=10.9 (n=415) |
| SMITH-BR5-ETHER-MIX-CO-SAT | group | ether_mixed | 1010-1050 | 346 | 0.89 | 0.31 | 1.3 [1.2, 1.4] | [1.2, 1.5] | 0.35 [0.26, 0.48] | 1.3 | ether_aryl OR=4.8 (n=78); aromatic_mono OR=4.7 (n=781); alkene_trisubstituted OR=3.4 (n=135) |
| SMITH-BR5-ETHER-MIX-CO-AR | group | ether_mixed | 1200-1300 | 346 | 0.98 | 0.08 | 1.1 [1.1, 1.1] | [1.0, 1.1] | 0.22 [0.10, 0.48] | 1.1 | ester_aromatic OR=28.3 (n=155); ether_aryl OR=15.3 (n=85); ketone_aromatic OR=11.6 (n=189) |
| SMITH-BR5-ETHER-SAT-CO | group | ether_saturated | 1070-1140 | 242 | 0.97 | 0.15 | 1.1 [1.1, 1.2] | [1.1, 1.2] | 0.19 [0.09, 0.39] | 1.1 | ether_aryl OR=6.4 (n=85); ester_aromatic OR=6.3 (n=150); aromatic_para OR=6.3 (n=612) |
| SMITH-BR6-KET-AR-CCC | group | ketone_aromatic | 1230-1300 | 219 | 0.61 | 0.74 | 2.4 [2.1, 2.6] | [1.5, 3.2] | 0.53 [0.45, 0.62] | 1.1 | ester_aromatic OR=8.6 (n=116); carbonate_organic OR=6.9 (n=15); ether_mixed OR=6.0 (n=204) |
| SMITH-BR6-KET-AR-CO | group | ketone_aromatic | 1640-1700 | 219 | 0.53 | 0.81 | 2.8 [2.4, 3.2] | [2.0, 3.7] | 0.58 [0.51, 0.67] | 2.3 | amide_primary OR=23.8 (n=82); amides OR=8.0 (n=342); carbonyl_any OR=7.8 (n=737) |
| SMITH-BR6-KET-SAT-CCC | group | ketone_saturated | 1100-1230 | 173 | 0.21 | 0.67 | 0.6 [0.5, 0.8] | [0.4, 0.8] | 1.19 [1.10, 1.29] | 1.1 | ether_aryl OR=5.5 (n=65); ether_saturated OR=3.3 (n=146); esters OR=3.3 (n=363) |
| SMITH-BR6-KET-SAT-CO | group | ketone_saturated | 1705-1725 | 173 | 0.39 | 0.93 | 5.2 [4.2, 6.5] | [3.6, 6.4] | 0.66 [0.59, 0.74] | 4.5 | carbonyl_any OR=19.6 (n=339); carboxylic_acid_saturated OR=6.3 (n=62); carboxylic_acids OR=4.8 (n=77) |
| SMITH-BR4-CH3-UMBRELLA | group | methyl | 1365-1385 | 3136 | 0.63 | 0.62 | 1.6 [1.6, 1.8] | [1.5, 1.8] | 0.60 [0.56, 0.63] | 1.6 | carbonate_organic OR=2.2 (n=3); ether_aryl OR=2.0 (n=16); amide_secondary OR=2.0 (n=70) |
| SMITH-BR4-CH3-SYM | group | methyl | 2862-2882 | 3136 | 0.23 | 0.87 | 1.7 [1.5, 2.0] | [1.4, 1.9] | 0.89 [0.87, 0.91] | 1.7 | methylene_chain_4 OR=4.0 (n=49); ether_saturated OR=3.2 (n=25); alcohol_primary OR=2.9 (n=30) |
| SMITH-BR4-CH3-ASYM | group | methyl | 2952-2972 | 3136 | 0.32 | 0.87 | 2.5 [2.2, 2.8] | [2.0, 2.8] | 0.78 [0.76, 0.80] | 2.5 | ketone_saturated OR=3.6 (n=5); alcohol_tertiary OR=3.3 (n=5); methylene OR=3.1 (n=174) |
| SMITH-BR4-CH2-SYM | group | methylene | 2845-2865 | 3017 | 0.21 | 0.90 | 2.0 [1.7, 2.3] | [1.6, 2.6] | 0.89 [0.87, 0.91] | 2.0 | aldehyde_aromatic OR=3.4 (n=10); ether_mixed OR=3.4 (n=30); ether OR=3.3 (n=44) |
| SMITH-BR4-CH2-ASYM | group | methylene | 2916-2936 | 3017 | 0.32 | 0.83 | 1.8 [1.6, 2.0] | [1.6, 2.1] | 0.83 [0.80, 0.85] | 1.8 | alkyne_internal OR=4.8 (n=3); alkyne OR=2.6 (n=3); ketone_saturated OR=2.6 (n=3) |
| SMITH-BR4-CH2-ROCK | group | methylene_chain_4 | 710-730 | 632 | 0.59 | 0.66 | 1.7 [1.6, 1.9] | [0.9, 2.3] | 0.62 [0.56, 0.68] | 1.7 | ketone_aromatic OR=2.4 (n=113); aromatics OR=2.3 (n=1227); nitrile_aromatic OR=2.1 (n=17) |
| SMITH-BR8-NH-ANY | class | n_h_any | 3300-3500 | 1420 | 0.76 | 0.66 | 2.2 [2.1, 2.4] | [1.7, 2.6] | 0.36 [0.33, 0.40] | 2.2 | aldehyde_saturated OR=12.3 (n=15); alcohol_secondary OR=11.3 (n=187); alcohol_primary OR=8.2 (n=148) |
| SMITH-NIT19-AR-CN | group | nitrile_aromatic | 2220-2240 | 33 | 0.06 | 1.00 | 61.7 [12.4, 306.8] | [13.7, 337.7] | 0.94 [0.86, 1.03] | 28.2 | nitriles OR=486.4 (n=5); nitrile_saturated OR=76.4 (n=3); alkene OR=10.2 (n=3) |
| SMITH-NIT19-SAT-CN | group | nitrile_saturated | 2240-2260 | 94 | 0.03 | 1.00 | 160.5 [16.9, 1529.2] | [16.0, 603.1] | 0.97 [0.93, 1.00] | 31.9 |  |
| SMITH-NO2-20-SCIS | group | nitro | 835-890 | 388 | 0.55 | 0.69 | 1.8 [1.6, 1.9] | [1.2, 2.0] | 0.66 [0.59, 0.74] | 1.2 | ether_aryl OR=7.5 (n=67); aromatic_meta OR=3.1 (n=61); phenol OR=2.7 (n=207) |
| SMITH-NO2-20-SYM | group | nitro | 1330-1390 | 388 | 0.75 | 0.85 | 5.1 [4.7, 5.6] | [3.7, 6.1] | 0.29 [0.24, 0.35] | 1.2 | ether_aryl OR=3.3 (n=31); phenol OR=1.6 (n=82); aromatics OR=1.6 (n=504) |
| SMITH-NO2-20-ASYM | group | nitro | 1500-1550 | 388 | 0.61 | 0.85 | 4.1 [3.7, 4.6] | [3.0, 6.8] | 0.46 [0.41, 0.52] | 2.2 | ether_aryl OR=5.6 (n=42); aromatics OR=5.4 (n=622); amine_secondary_aromatic OR=4.3 (n=73) |
| SMITH-BR5-PHENOL-CO | group | phenol | 1200-1260 | 422 | 0.95 | 0.22 | 1.2 [1.2, 1.2] | [1.1, 1.3] | 0.23 [0.15, 0.35] | 1.2 | ether_aryl OR=6.7 (n=82); alkene_trisubstituted OR=3.6 (n=144); ether_mixed OR=3.5 (n=277) |

## Stratum: salt (n up to 314; each rule is scored on the spectra whose measured range covers its windows)

| rule | tier | truth group | window | n+ | sens | spec | LR+ [CI] | LR+ boot | LR- [CI] | LR+ pos | FP enriched in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SMITH-SALT19-NH3-SYM | group | ammonium_primary | 1500-1550 | 11 | 0.82 | 0.53 | 1.8 [1.3, 2.4] | [1.3, 2.3] | 0.34 [0.10, 1.20] | 1.8 | nitro OR=17.9 (n=7); amine_primary_aromatic OR=13.9 (n=33); aromatic_para OR=9.4 (n=24) |
| SMITH-SALT19-NH3-ASYM | group | ammonium_primary | 1560-1625 | 11 | 1.00 | 0.18 | 1.2 [1.0, 1.3] | [0.9, 1.3] | 0.23 [0.02, 3.54] | 1.2 | amine_primary_saturated OR=24.3 (n=45); amine_secondary_saturated OR=18.0 (n=35); amines OR=15.4 (n=144) |
| SMITH-SALT19-NH3-STR | group | ammonium_primary | 2800-3200 | 11 | 1.00 | 0.03 | 1.0 [0.9, 1.1] | [0.8, 1.0] | 1.21 [0.08, 19.40] | 1.0 | alkyl_halides OR=2.6 (n=32); aromatic_para OR=2.2 (n=27); c_o_single_any OR=2.1 (n=74) |
| SMITH-SALT19-NH2-BEND | group | ammonium_secondary | 1560-1620 | 6 (underpowered) | 0.83 | 0.18 | 1.0 [0.7, 1.5] |  | 0.92 [0.15, 5.57] | 1.0 |  |
| SMITH-SALT19-NH2-STR | group | ammonium_secondary | 2700-3000 | 6 (underpowered) | 0.83 | 0.09 | 0.9 [0.6, 1.3] |  | 1.77 [0.29, 10.95] | 0.9 |  |
| SMITH-SALT19-NH-STR | group | ammonium_tertiary | 2300-2700 | 5 (underpowered) | 1.00 | 0.22 | 1.2 [0.9, 1.5] |  | 0.38 [0.03, 5.48] | 1.2 |  |

## Prominence sweep (LR+, full definition, main stratum)

| rule | p>=0.01 | p>=0.02 | p>=0.05 | p>=0.1 |
| --- | --- | --- | --- | --- |
| SMITH-ALD17-AR-CO | 3.0 | 3.0 | 3.0 | 2.8 |
| SMITH-ALD17-CH-BEND | 1.5 | 1.4 | 1.3 | 1.2 |
| SMITH-ALD17-CH-STR | 2.7 | 3.4 | 4.1 | 4.3 |
| SMITH-ALD17-SAT-CO | 6.3 | 6.3 | 6.6 | 6.7 |
| SMITH-ALK16-CC-STR | 1.9 | 2.1 | 2.2 | 2.1 |
| SMITH-ALK16-CH-STR | 1.2 | 1.2 | 1.4 | 1.5 |
| SMITH-ALK16-TRISUB-CC | 2.7 | 2.9 | 2.8 | 2.9 |
| SMITH-ALK16-TRISUB-WAG | 1.2 | 1.1 | 1.0 | 0.8 |
| SMITH-ALK16-VINYL-CC | 3.1 | 3.4 | 3.7 | 3.5 |
| SMITH-ALK16-VINYL-WAG1 | 3.4 | 4.0 | 5.3 | 7.4 |
| SMITH-ALK16-VINYL-WAG2 | 1.4 | 1.6 | 2.1 | 3.0 |
| SMITH-ALY17-INT-CC | 4.2 | 5.9 | 12.2 | 11.2 |
| SMITH-ALY17-TERM-CC | 9.9 | 11.9 | 5.0 | 4.5 |
| SMITH-ALY17-TERM-CH | 4.0 | 4.5 | 5.0 | 5.7 |
| SMITH-ALY17-TERM-CH-BEND | 1.2 | 1.3 | 1.6 | 2.1 |
| SMITH-BR4-BZ-META-690 | 1.7 | 1.7 | 1.8 | 2.1 |
| SMITH-BR4-BZ-META-BOTH | 1.9 | 2.0 | 2.3 | 2.9 |
| SMITH-BR4-BZ-META-OOP | 1.2 | 1.3 | 1.5 | 1.8 |
| SMITH-BR4-BZ-MONO-690 | 2.8 | 3.1 | 4.0 | 5.6 |
| SMITH-BR4-BZ-MONO-BOTH | 3.1 | 3.7 | 5.3 | 8.4 |
| SMITH-BR4-BZ-MONO-OOP | 1.2 | 1.2 | 1.4 | 1.7 |
| SMITH-BR4-BZ-ORTHO-OOP | 1.5 | 1.7 | 2.1 | 2.8 |
| SMITH-BR4-BZ-PARA-OOP | 1.0 | 1.1 | 1.3 | 1.7 |
| SMITH-BR4-CH2-ASYM | 1.7 | 1.8 | 1.9 | 2.0 |
| SMITH-BR4-CH2-ROCK | 1.6 | 1.7 | 1.7 | 1.4 |
| SMITH-BR4-CH2-SYM | 1.8 | 2.0 | 2.7 | 4.6 |
| SMITH-BR4-CH3-ASYM | 2.4 | 2.5 | 2.9 | 3.3 |
| SMITH-BR4-CH3-SYM | 1.7 | 1.7 | 1.7 | 1.8 |
| SMITH-BR4-CH3-UMBRELLA | 1.6 | 1.6 | 1.7 | 1.8 |
| SMITH-BR5-CO-GENERAL | 1.6 | 1.6 | 1.6 | 1.6 |
| SMITH-BR5-ETHER-ARYL-CO | 1.0 | 1.1 | 1.2 | 1.3 |
| SMITH-BR5-ETHER-MIX-CO-AR | 1.1 | 1.1 | 1.1 | 1.3 |
| SMITH-BR5-ETHER-MIX-CO-SAT | 1.3 | 1.3 | 1.5 | 1.9 |
| SMITH-BR5-ETHER-SAT-CO | 1.1 | 1.1 | 1.3 | 1.5 |
| SMITH-BR5-PHENOL-CO | 1.2 | 1.2 | 1.3 | 1.5 |
| SMITH-BR5-ROH-OH-STR | 1.3 | 1.5 | 1.6 | 1.7 |
| SMITH-BR5-ROH-OH-WAG | 1.1 | 1.0 | 1.0 | 0.8 |
| SMITH-BR5-ROH-PRIM-CO | 1.1 | 1.1 | 1.3 | 1.5 |
| SMITH-BR5-ROH-SEC-CO | 1.1 | 1.1 | 1.2 | 1.3 |
| SMITH-BR5-ROH-TERT-CO | 1.0 | 1.1 | 1.1 | 1.2 |
| SMITH-BR6-ACID-AR-CO | 3.7 | 3.7 | 3.8 | 3.9 |
| SMITH-BR6-ACID-CO | 1.0 | 1.0 | 1.1 | 1.2 |
| SMITH-BR6-ACID-OH-IPB | 1.3 | 1.4 | 1.5 | 1.6 |
| SMITH-BR6-ACID-OH-OOP | 1.1 | 1.2 | 1.4 | 1.5 |
| SMITH-BR6-ACID-OH-STR | 1.2 | 1.2 | 1.2 | 1.2 |
| SMITH-BR6-ACID-SAT-CO | 4.2 | 4.2 | 4.1 | 4.2 |
| SMITH-BR6-CO-GENERAL | 4.1 | 4.1 | 4.1 | 4.1 |
| SMITH-BR6-KET-AR-CCC | 2.4 | 2.4 | 2.3 | 2.3 |
| SMITH-BR6-KET-AR-CO | 2.8 | 2.8 | 2.8 | 2.9 |
| SMITH-BR6-KET-SAT-CCC | 0.6 | 0.6 | 0.6 | 0.6 |
| SMITH-BR6-KET-SAT-CO | 5.2 | 5.2 | 5.3 | 5.2 |
| SMITH-BR7-CARB-AR-CO | 9.5 | 9.6 | 9.7 | 9.7 |
| SMITH-BR7-CARB-AR-OCO | 1.8 | 1.9 | 1.9 | 1.9 |
| SMITH-BR7-CARB-MIX-CO | 7.3 | 7.4 | 7.5 | 7.6 |
| SMITH-BR7-CARB-MIX-OCO | 1.6 | 1.6 | 1.3 | 1.1 |
| SMITH-BR7-CARB-OCC | 1.6 | 1.6 | 1.6 | 1.6 |
| SMITH-BR7-CARB-SAT-CO | 5.7 | 5.7 | 5.8 | 5.9 |
| SMITH-BR7-CARB-SAT-OCO | 3.7 | 3.7 | 3.5 | 3.3 |
| SMITH-BR7-EST-AR-CCO | 3.4 | 3.4 | 3.5 | 3.5 |
| SMITH-BR7-EST-AR-CO | 4.5 | 4.4 | 4.4 | 4.5 |
| SMITH-BR7-EST-AR-OCC | 2.8 | 2.9 | 2.8 | 2.9 |
| SMITH-BR7-EST-SAT-CCO | 2.4 | 2.4 | 2.4 | 2.3 |
| SMITH-BR7-EST-SAT-CO | 12.4 | 12.4 | 12.7 | 12.9 |
| SMITH-BR7-EST-SAT-OCC | 1.2 | 1.2 | 1.2 | 1.2 |
| SMITH-BR8-AMD-CO | 4.0 | 4.0 | 4.0 | 4.0 |
| SMITH-BR8-AMD1-CN | 1.2 | 1.4 | 1.6 | 1.8 |
| SMITH-BR8-AMD1-NH-STR | 2.7 | 2.9 | 3.0 | 2.8 |
| SMITH-BR8-AMD1-SCIS | 1.9 | 2.1 | 2.2 | 2.5 |
| SMITH-BR8-AMD1-WAG | 1.1 | 1.1 | 1.2 | 1.3 |
| SMITH-BR8-AMD2-CN | 1.0 | 1.1 | 1.1 | 1.1 |
| SMITH-BR8-AMD2-NH-IPB | 2.6 | 2.6 | 2.6 | 2.5 |
| SMITH-BR8-AMD2-NH-STR | 2.4 | 2.6 | 2.8 | 2.9 |
| SMITH-BR8-AMD2-WAG | 1.1 | 1.1 | 1.1 | 1.1 |
| SMITH-BR8-AMN1-AR-ASYM | 2.3 | 3.0 | 3.9 | 5.2 |
| SMITH-BR8-AMN1-AR-CN | 1.1 | 1.1 | 1.2 | 1.2 |
| SMITH-BR8-AMN1-AR-SYM | 2.6 | 3.0 | 3.5 | 4.0 |
| SMITH-BR8-AMN1-SAT-ASYM | 2.0 | 2.3 | 2.2 | 1.7 |
| SMITH-BR8-AMN1-SAT-CN | 1.0 | 1.0 | 1.0 | 0.9 |
| SMITH-BR8-AMN1-SAT-SYM | 2.7 | 2.7 | 1.5 | 1.1 |
| SMITH-BR8-AMN1-SCIS | 1.4 | 1.4 | 1.6 | 1.8 |
| SMITH-BR8-AMN1-WAG | 1.1 | 1.1 | 1.1 | 1.1 |
| SMITH-BR8-AMN2-AR-CNC | 1.1 | 1.1 | 1.2 | 1.3 |
| SMITH-BR8-AMN2-AR-NH | 1.7 | 1.9 | 2.3 | 2.4 |
| SMITH-BR8-AMN2-SAT-CNC | 1.0 | 1.0 | 1.1 | 1.0 |
| SMITH-BR8-AMN2-SAT-NH | 4.1 | 4.3 | 3.7 | 2.5 |
| SMITH-BR8-AMN2-WAG | 1.0 | 1.0 | 1.1 | 1.2 |
| SMITH-BR8-NH-ANY | 1.8 | 2.2 | 3.0 | 3.9 |
| SMITH-BZ16-ARCH-STR | 2.1 | 2.1 | 1.9 | 1.6 |
| SMITH-BZ16-OOP | 1.0 | 1.0 | 1.1 | 1.2 |
| SMITH-BZ16-RING | 1.0 | 1.0 | 1.0 | 1.1 |
| SMITH-NIT19-AR-CN | 61.7 | 61.7 | 61.7 | 61.7 |
| SMITH-NIT19-SAT-CN | 160.5 | 160.5 | 160.5 | 160.5 |
| SMITH-NO2-20-ASYM | 4.1 | 4.1 | 4.1 | 4.1 |
| SMITH-NO2-20-SCIS | 1.7 | 1.8 | 1.8 | 1.8 |
| SMITH-NO2-20-SYM | 5.1 | 5.1 | 5.1 | 5.1 |

## Not evaluable (5 rules)

- SMITH-ALK16-CIS-CC: cis alkene.  NOT EVALUABLE: cis/trans needs stereo marks that most depositor SMILES lack (decision D6)
- SMITH-ALK16-CIS-WAG: cis alkene. Wide tolerance in the source (+-50) NOT EVALUABLE: cis/trans needs stereo marks that most depositor SMILES lack (decision D6)
- SMITH-ALK16-TRANS-CC: trans alkene.  NOT EVALUABLE: cis/trans needs stereo marks that most depositor SMILES lack (decision D6)
- SMITH-ALK16-TRANS-WAG: trans alkene.  NOT EVALUABLE: cis/trans needs stereo marks that most depositor SMILES lack (decision D6)
- SMITH-SALT19-COMB: amine salt. All three salt types. This is the window where salts mimic alkynes and nitriles (an IR trap for the analysis)
