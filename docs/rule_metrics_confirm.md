# Rule metrics, split = confirm

**Confirmatory run on the frozen rule table.**

Primary prominence threshold 0.02; full definition (position, intensity, shape). `LR+ [CI]` is the analytic 95 percent interval; `boot` is the scaffold-cluster bootstrap interval (500 resamples); `LR+ pos` is the same rule scored by position only. Rules with fewer than 10 positives are marked underpowered.

## Stratum: main (n = 1539)

| rule | tier | truth group | window | n+ | sens | spec | LR+ [CI] | LR+ boot | LR- [CI] | LR+ pos | FP enriched in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SMITH-BR5-ROH-PRIM-CO | group | alcohol_primary | 1000-1075 | 20 | 0.95 | 0.04 | 1.0 [0.9, 1.1] | [0.9, 1.0] | 1.23 [0.18, 8.40] | 1.0 | ether OR=32.7 (n=302); ether_mixed OR=23.0 (n=226); c_o_single_any OR=19.2 (n=465) |
| SMITH-BR5-ROH-SEC-CO | group | alcohol_secondary | 1075-1150 | 47 | 0.94 | 0.04 | 1.0 [0.9, 1.1] | [0.9, 1.1] | 1.42 [0.46, 4.35] | 1.0 | aromatics OR=5.3 (n=1350); aromatic_para OR=3.6 (n=396); alkane OR=2.5 (n=1080) |
| SMITH-BR5-ROH-TERT-CO | group | alcohol_tertiary | 1100-1210 | 8 (underpowered) | 1.00 | 0.01 | 1.0 [0.8, 1.1] |  | 3.62 [0.24, 55.17] | 1.0 |  |
| SMITH-BR5-ROH-OH-WAG | group | alcohols | 600-700 | 181 | 0.83 | 0.16 | 1.0 [0.9, 1.1] | [0.9, 1.1] | 1.06 [0.75, 1.50] | 1.0 | aromatic_meta OR=14.4 (n=37); aromatic_mono OR=5.8 (n=302); ether_aryl OR=4.7 (n=12) |
| SMITH-BR5-ROH-OH-STR | group | alcohols | 3300-3400 | 181 | 0.34 | 0.74 | 1.3 [1.1, 1.7] | [1.0, 1.7] | 0.88 [0.79, 0.98] | 1.3 | amine_primary OR=14.3 (n=59); amine_primary_saturated OR=13.9 (n=11); amine_primary_aromatic OR=12.4 (n=46) |
| SMITH-ALD17-AR-CO | group | aldehyde_aromatic | 1685-1710 | 64 | 0.16 | 0.89 | 1.5 [0.8, 2.6] | [0.7, 4.0] | 0.94 [0.85, 1.05] | 1.6 | carboxylic_acid_saturated OR=5.9 (n=4); ketone_saturated OR=4.7 (n=14); carbonyl_any OR=4.2 (n=117) |
| SMITH-ALD17-SAT-CO | group | aldehyde_saturated | 1720-1740 | 3 (underpowered) | 0.00 | 0.93 | 1.7 [0.1, 23.2] |  | 0.94 [0.65, 1.37] | 0.5 |  |
| SMITH-ALD17-CH-BEND | group | aldehydes | 1380-1400 | 68 | 0.59 | 0.58 | 1.4 [1.1, 1.7] | [1.1, 2.2] | 0.71 [0.53, 0.95] | 1.4 | nitrile_saturated OR=9.7 (n=3); ketone_aromatic OR=2.2 (n=94); ester_aromatic OR=2.2 (n=68) |
| SMITH-ALD17-CH-STR | group | aldehydes | 2700-2850 | 68 | 0.60 | 0.71 | 2.1 [1.7, 2.6] | [1.6, 3.0] | 0.56 [0.41, 0.75] | 2.1 | ether_mixed OR=4.2 (n=116); ether OR=2.8 (n=133); c_o_single_any OR=2.6 (n=192) |
| SMITH-ALK16-CC-STR | class | alkene | 1630-1680 | 228 | 0.57 | 0.55 | 1.3 [1.1, 1.4] | [1.0, 1.6] | 0.79 [0.67, 0.92] | 1.3 | amide_secondary OR=9.0 (n=107); nitrile_saturated OR=8.7 (n=3); amides OR=5.0 (n=146) |
| SMITH-ALK16-CH-STR | class | alkene | 3000-3100 | 228 | 0.57 | 0.40 | 0.9 [0.8, 1.1] | [0.8, 1.1] | 1.08 [0.91, 1.27] | 0.9 | ether_aryl OR=9.9 (n=7); aromatics OR=6.8 (n=778); aromatic_mono OR=4.8 (n=245) |
| SMITH-ALK16-TRISUB-WAG | group | alkene_trisubstituted | 790-840 | 41 | 0.93 | 0.16 | 1.1 [1.0, 1.2] | [1.0, 1.2] | 0.46 [0.15, 1.37] | 1.1 | aromatic_para OR=8.3 (n=394); ether_aryl OR=5.2 (n=13); ester_aromatic OR=4.1 (n=111) |
| SMITH-ALK16-TRISUB-CC | group | alkene_trisubstituted | 1660-1680 | 41 | 0.41 | 0.81 | 2.1 [1.5, 3.1] | [0.7, 3.3] | 0.73 [0.56, 0.94] | 2.1 | nitrile_saturated OR=29.3 (n=3); amide_primary OR=5.8 (n=3); ketone_aromatic OR=3.6 (n=58) |
| SMITH-ALK16-VINYL-WAG2 | group | alkene_vinyl | 905-915 | 34 | 0.38 | 0.74 | 1.5 [0.9, 2.3] | [0.6, 2.3] | 0.84 [0.64, 1.09] | 1.5 | alcohol_tertiary OR=4.5 (n=5); ether_aryl OR=4.5 (n=8); amine_secondary_saturated OR=4.0 (n=14) |
| SMITH-ALK16-VINYL-WAG1 | group | alkene_vinyl | 985-995 | 34 | 0.35 | 0.84 | 2.2 [1.4, 3.5] | [0.8, 3.8] | 0.77 [0.60, 0.99] | 2.2 | aromatic_meta OR=1.6 (n=9); alkene_trisubstituted OR=1.5 (n=9); ketone_saturated OR=1.5 (n=7) |
| SMITH-ALK16-VINYL-CC | group | alkene_vinyl | 1630-1660 | 34 | 0.77 | 0.69 | 2.5 [2.0, 3.0] | [2.1, 3.0] | 0.34 [0.19, 0.63] | 2.5 | amide_secondary OR=4.0 (n=81); amine_secondary_saturated OR=3.7 (n=15); amides OR=3.4 (n=112) |
| SMITH-ALY17-INT-CC | group | alkyne_internal | 2190-2260 | 79 | 0.79 | 0.77 | 3.4 [3.0, 4.0] | [2.7, 4.2] | 0.28 [0.18, 0.43] | 3.4 | nitriles OR=57.0 (n=62); nitrile_aromatic OR=57.0 (n=62); amine_secondary_saturated OR=2.5 (n=10) |
| SMITH-ALY17-TERM-CH-BEND | group | alkyne_terminal | 600-700 | 23 | 0.91 | 0.16 | 1.1 [1.0, 1.2] | [0.9, 1.2] | 0.55 [0.14, 2.07] | 1.1 | aromatic_meta OR=16.6 (n=42); aromatic_mono OR=6.4 (n=329); ether_aryl OR=5.2 (n=13) |
| SMITH-ALY17-TERM-CC | group | alkyne_terminal | 2100-2140 | 23 | 0.70 | 0.74 | 2.7 [2.0, 3.5] | [1.7, 3.6] | 0.41 [0.22, 0.76] | 2.7 | amine_secondary_saturated OR=4.8 (n=15); alcohol_secondary OR=3.0 (n=23); alcohol_tertiary OR=2.9 (n=4) |
| SMITH-ALY17-TERM-CH | group | alkyne_terminal | 3250-3350 | 23 | 0.87 | 0.77 | 3.8 [3.2, 4.6] | [3.0, 4.6] | 0.17 [0.06, 0.49] | 3.8 | amide_secondary OR=17.6 (n=113); n_h_any OR=11.6 (n=199); amine_primary OR=6.9 (n=49) |
| SMITH-BR8-AMD1-WAG | group | amide_primary | 600-750 | 5 (underpowered) | 1.00 | 0.02 | 0.9 [0.7, 1.2] |  | 3.82 [0.26, 55.41] | 0.9 |  |
| SMITH-BR8-AMD1-CN | group | amide_primary | 1390-1430 | 5 (underpowered) | 0.60 | 0.25 | 0.8 [0.4, 1.6] |  | 1.62 [0.55, 4.77] | 0.8 |  |
| SMITH-BR8-AMD1-SCIS | group | amide_primary | 1620-1650 | 5 (underpowered) | 0.20 | 0.70 | 0.7 [0.1, 3.9] |  | 1.14 [0.73, 1.77] | 0.7 |  |
| SMITH-BR8-AMD1-NH-STR | group | amide_primary | 3170-3370 | 5 (underpowered) | 0.40 | 0.69 | 1.3 [0.4, 3.7] |  | 0.88 [0.43, 1.79] | 1.3 |  |
| SMITH-BR8-AMD2-WAG | group | amide_secondary | 680-750 | 147 | 0.97 | 0.05 | 1.0 [1.0, 1.1] | [1.0, 1.1] | 0.57 [0.21, 1.55] | 1.0 | aromatic_mono OR=37.8 (n=293); ketone_aromatic OR=16.9 (n=149); alkyne OR=10.9 (n=100) |
| SMITH-BR8-AMD2-CN | group | amide_secondary | 1230-1310 | 147 | 0.91 | 0.06 | 1.0 [0.9, 1.0] | [0.9, 1.0] | 1.49 [0.87, 2.55] | 1.0 | alkene_trisubstituted OR=5.3 (n=37); aromatics OR=5.2 (n=1229); ketone_saturated OR=4.6 (n=32) |
| SMITH-BR8-AMD2-NH-IPB | group | amide_secondary | 1515-1570 | 147 | 0.44 | 0.89 | 3.9 [3.1, 4.9] | [2.8, 5.2] | 0.63 [0.54, 0.73] | 1.5 | nitro OR=9.4 (n=25); ketone_aromatic OR=3.2 (n=38); n_h_any OR=2.9 (n=42) |
| SMITH-BR8-AMD2-NH-STR | group | amide_secondary | 3170-3370 | 147 | 0.94 | 0.75 | 3.8 [3.4, 4.2] | [3.2, 4.5] | 0.08 [0.04, 0.15] | 3.8 | alkyne_terminal OR=41.3 (n=19); amine_primary OR=17.1 (n=63); amine_primary_aromatic OR=15.3 (n=50) |
| SMITH-BR8-AMD-CO | group | amides | 1630-1680 | 223 | 0.47 | 0.85 | 3.1 [2.6, 3.8] | [2.3, 4.3] | 0.62 [0.55, 0.71] | 1.9 | ketone_aromatic OR=8.5 (n=75); ketones OR=7.0 (n=83); carbonyl_any OR=6.5 (n=149) |
| SMITH-BR8-AMN1-WAG | group | amine_primary | 750-850 | 76 | 0.95 | 0.02 | 1.0 [0.9, 1.0] | [0.9, 1.0] | 2.96 [1.06, 8.27] | 1.0 | aromatics OR=10.3 (n=1354); ether_mixed OR=9.7 (n=222); alkene_disubstituted OR=4.0 (n=100) |
| SMITH-BR8-AMN1-SCIS | group | amine_primary | 1580-1650 | 76 | 0.90 | 0.13 | 1.0 [0.9, 1.1] | [0.9, 1.1] | 0.81 [0.42, 1.59] | 1.0 | phenol OR=19.9 (n=63); amine_secondary_aromatic OR=18.6 (n=59); aromatics OR=17.3 (n=1241) |
| SMITH-BR8-AMN1-AR-CN | group | amine_primary_aromatic | 1250-1350 | 61 | 0.95 | 0.06 | 1.0 [0.9, 1.1] | [0.9, 1.1] | 0.84 [0.27, 2.57] | 1.0 | ether_mixed OR=33.3 (n=222); ester_aromatic OR=14.2 (n=104); ketone_aromatic OR=7.2 (n=154) |
| SMITH-BR8-AMN1-AR-SYM | group | amine_primary_aromatic | 3340-3420 | 61 | 0.72 | 0.80 | 3.6 [3.0, 4.4] | [2.6, 4.8] | 0.35 [0.23, 0.52] | 3.6 | amine_primary_saturated OR=8.7 (n=9); amine_primary OR=7.9 (n=10); amine_secondary_aromatic OR=7.0 (n=36) |
| SMITH-BR8-AMN1-AR-ASYM | group | amine_primary_aromatic | 3420-3500 | 61 | 0.64 | 0.91 | 6.8 [5.3, 8.7] | [4.6, 10.8] | 0.40 [0.28, 0.56] | 6.8 | alcohol_tertiary OR=9.9 (n=4); carboxylic_acid_saturated OR=6.8 (n=4); alcohol_secondary OR=3.6 (n=12) |
| SMITH-BR8-AMN1-SAT-CN | group | amine_primary_saturated | 1020-1250 | 13 | 1.00 | 0.00 | 1.0 [0.9, 1.1] | [0.9, 1.0] | 15.58 [0.84, 287.79] | 1.0 | methyl OR=15.9 (n=1058); carbonyl_any OR=6.2 (n=717); c_o_single_any OR=3.3 (n=485) |
| SMITH-BR8-AMN1-SAT-SYM | group | amine_primary_saturated | 3280-3310 | 13 | 0.39 | 0.89 | 3.5 [1.7, 7.0] | [0.7, 5.8] | 0.69 [0.45, 1.06] | 3.5 | alkyne_terminal OR=13.2 (n=14); n_h_any OR=6.8 (n=95); amide_secondary OR=6.6 (n=55) |
| SMITH-BR8-AMN1-SAT-ASYM | group | amine_primary_saturated | 3350-3380 | 13 | 0.69 | 0.92 | 8.7 [5.8, 12.9] | [6.0, 13.1] | 0.33 [0.15, 0.76] | 8.7 | amine_primary OR=9.3 (n=25); amine_primary_aromatic OR=9.1 (n=24); amines OR=7.5 (n=48) |
| SMITH-BR8-AMN2-WAG | group | amine_secondary | 700-750 | 85 | 0.96 | 0.11 | 1.1 [1.0, 1.1] | [1.0, 1.1] | 0.33 [0.11, 1.00] | 1.1 | ketone_aromatic OR=6.0 (n=154); aromatics OR=5.0 (n=1234); nitro OR=4.0 (n=48) |
| SMITH-BR8-AMN2-AR-CNC | group | amine_secondary_aromatic | 1250-1350 | 60 | 0.98 | 0.06 | 1.1 [1.0, 1.1] | [1.0, 1.1] | 0.28 [0.04, 1.95] | 1.1 | ether_mixed OR=34.6 (n=225); phenol OR=8.6 (n=63); ketone_aromatic OR=7.5 (n=156) |
| SMITH-BR8-AMN2-AR-NH | group | amine_secondary_aromatic | 3380-3420 | 60 | 0.28 | 0.88 | 2.3 [1.5, 3.6] | [1.2, 3.7] | 0.82 [0.69, 0.96] | 2.3 | alcohol_primary OR=3.3 (n=6); amine_primary_aromatic OR=3.1 (n=17); alkene_trisubstituted OR=2.8 (n=11) |
| SMITH-BR8-AMN2-SAT-CNC | group | amine_secondary_saturated | 1130-1180 | 24 | 1.00 | 0.11 | 1.1 [1.0, 1.2] | [1.0, 1.1] | 0.18 [0.01, 2.84] | 1.1 | alkene_disubstituted OR=8.8 (n=99); amides OR=3.2 (n=199); ether_mixed OR=3.2 (n=218) |
| SMITH-BR8-AMN2-SAT-NH | group | amine_secondary_saturated | 3280-3320 | 24 | 0.12 | 0.86 | 0.9 [0.3, 2.7] | [0.2, 2.2] | 1.01 [0.87, 1.18] | 0.9 | alkyne_terminal OR=10.4 (n=14); amide_secondary OR=7.5 (n=67); n_h_any OR=7.4 (n=113) |
| SMITH-BR4-BZ-META-690 | group | aromatic_meta | 680-700 | 42 | 0.74 | 0.43 | 1.3 [1.1, 1.6] | [1.0, 1.6] | 0.61 [0.37, 1.02] | 1.3 | aromatic_mono OR=11.2 (n=308); ether_aryl OR=5.3 (n=10); alkyne_internal OR=3.0 (n=62) |
| SMITH-BR4-BZ-META-OOP | group | aromatic_meta | 750-810 | 42 | 0.98 | 0.10 | 1.1 [1.0, 1.1] | [1.1, 1.1] | 0.25 [0.04, 1.73] | 1.1 | carboxylic_acid_aromatic OR=6.2 (n=28); aromatics OR=4.5 (n=1281); ester_aromatic OR=2.7 (n=108) |
| SMITH-BR4-BZ-META-BOTH | group | aromatic_meta | 750-810 +680-700 | 42 | 0.74 | 0.47 | 1.4 [1.2, 1.7] | [1.1, 1.7] | 0.55 [0.33, 0.92] | 1.4 | aromatic_mono OR=6.3 (n=281); aromatics OR=3.6 (n=764); ether_aryl OR=3.4 (n=9) |
| SMITH-BR4-BZ-MONO-690 | group | aromatic_mono | 680-700 | 344 | 0.91 | 0.52 | 1.9 [1.8, 2.0] | [1.7, 2.2] | 0.17 [0.12, 0.24] | 1.9 | ether_aryl OR=3.2 (n=7); aromatic_meta OR=2.8 (n=26); alkene_trisubstituted OR=2.5 (n=26) |
| SMITH-BR4-BZ-MONO-OOP | group | aromatic_mono | 710-770 | 344 | 0.97 | 0.07 | 1.1 [1.0, 1.1] | [1.0, 1.1] | 0.38 [0.19, 0.74] | 1.1 | methylene_chain_4 OR=17.3 (n=104); aromatic_ortho OR=14.4 (n=88); nitro OR=6.6 (n=42) |
| SMITH-BR4-BZ-MONO-BOTH | group | aromatic_mono | 710-770 +680-700 | 344 | 0.89 | 0.55 | 2.0 [1.8, 2.1] | [1.7, 2.2] | 0.20 [0.14, 0.27] | 2.0 | ether_aryl OR=3.6 (n=7); alkene_trisubstituted OR=2.8 (n=26); nitro OR=2.4 (n=28) |
| SMITH-BR4-BZ-ORTHO-OOP | group | aromatic_ortho | 735-770 no 680-700 | 145 | 0.26 | 0.69 | 0.8 [0.6, 1.1] | [0.5, 1.3] | 1.08 [0.98, 1.20] | 0.8 | aldehyde_aromatic OR=2.2 (n=31); aldehydes OR=2.1 (n=32); alkyne_terminal OR=1.7 (n=10) |
| SMITH-BR4-BZ-PARA-OOP | group | aromatic_para | 790-860 no 680-700 | 415 | 0.44 | 0.63 | 1.2 [1.0, 1.4] | [0.9, 1.5] | 0.89 [0.81, 0.98] | 1.2 | amine_primary_saturated OR=7.2 (n=10); amide_primary OR=2.4 (n=3); aldehyde_aromatic OR=2.0 (n=31) |
| SMITH-BZ16-OOP | class | aromatics | 700-1000 | 1438 | 1.00 | 0.00 | 1.0 [1.0, 1.0] | [1.0, 1.0] | 0.21 [0.01, 5.19] | 1.0 | alkane OR=21.7 (n=97); methylene OR=11.0 (n=93); methyl OR=6.6 (n=88) |
| SMITH-BZ16-RING | class | aromatics | 1400-1620 | 1438 | 1.00 | 0.00 | 1.0 [1.0, 1.0] | [1.0, 1.0] | 0.07 [0.00, 3.55] | 1.0 | alkane OR=21.7 (n=97); methylene OR=11.0 (n=93); methyl OR=6.6 (n=88) |
| SMITH-BZ16-ARCH-STR | class | aromatics | 3000-3100 | 1438 | 0.63 | 0.78 | 2.9 [2.0, 4.2] | [1.8, 5.1] | 0.48 [0.42, 0.54] | 2.9 | alkene_disubstituted OR=50.0 (n=5); amide_secondary OR=7.5 (n=4); amides OR=3.3 (n=4) |
| SMITH-BR5-CO-GENERAL | class | c_o_single_any | 1000-1300 | 486 | 0.89 | 0.38 | 1.4 [1.4, 1.5] | [1.3, 1.5] | 0.30 [0.23, 0.38] | 1.0 | ester_aromatic OR=39.4 (n=85); amine_secondary_saturated OR=24.2 (n=19); esters OR=16.5 (n=174) |
| SMITH-BR7-CARB-OCC | group | carbonate_organic | 1000-1060 | 2 (underpowered) | 0.50 | 0.77 | 2.1 [0.5, 8.5] |  | 0.65 [0.16, 2.61] | 0.9 |  |
| SMITH-BR7-CARB-AR-OCO | group | carbonate_organic | 1205-1230 | 2 (underpowered) | 1.00 | 0.82 | 4.8 [2.8, 8.0] |  | 0.20 [0.02, 2.54] | 1.5 |  |
| SMITH-BR7-CARB-MIX-OCO | group | carbonate_organic | 1210-1250 | 2 (underpowered) | 1.00 | 0.73 | 3.1 [1.9, 5.2] |  | 0.23 [0.02, 2.85] | 1.1 |  |
| SMITH-BR7-CARB-SAT-OCO | group | carbonate_organic | 1240-1280 | 2 (underpowered) | 0.50 | 0.78 | 2.2 [0.6, 9.0] |  | 0.64 [0.16, 2.57] | 0.7 |  |
| SMITH-BR7-CARB-SAT-CO | group | carbonate_organic | 1730-1750 | 2 (underpowered) | 0.00 | 0.94 | 2.6 [0.2, 33.3] |  | 0.89 [0.54, 1.48] | 0.6 |  |
| SMITH-BR7-CARB-MIX-CO | group | carbonate_organic | 1760-1790 | 2 (underpowered) | 0.00 | 0.99 | 34.2 [2.5, 473.8] |  | 0.84 [0.50, 1.39] | 2.0 |  |
| SMITH-BR7-CARB-AR-CO | group | carbonate_organic | 1775-1820 | 2 (underpowered) | 0.00 | 0.99 | 30.2 [2.2, 413.3] |  | 0.84 [0.51, 1.39] | 1.4 |  |
| SMITH-BR6-CO-GENERAL | class | carbonyl_any | 1600-1900 | 721 | 0.78 | 0.80 | 4.0 [3.4, 4.6] | [2.5, 9.2] | 0.28 [0.24, 0.32] | 1.1 | phenol OR=7.8 (n=22); aromatics OR=5.5 (n=159); methylene_chain_4 OR=3.5 (n=27) |
| SMITH-BR6-ACID-AR-CO | group | carboxylic_acid_aromatic | 1680-1710 | 29 | 0.62 | 0.87 | 4.8 [3.5, 6.5] | [3.1, 7.2] | 0.44 [0.27, 0.70] | 2.4 | carboxylic_acid_saturated OR=6.8 (n=5); ketone_saturated OR=4.6 (n=16); carbonyl_any OR=4.4 (n=149) |
| SMITH-BR6-ACID-SAT-CO | group | carboxylic_acid_saturated | 1700-1730 | 10 | 0.20 | 0.85 | 1.3 [0.4, 4.6] | [0.2, 4.2] | 0.94 [0.69, 1.29] | 1.6 | aldehyde_saturated OR=39.6 (n=3); ester_aromatic OR=15.9 (n=77); ketone_saturated OR=11.8 (n=27) |
| SMITH-BR6-ACID-OH-OOP | group | carboxylic_acids | 900-960 | 48 | 0.88 | 0.14 | 1.0 [0.9, 1.1] | [1.0, 1.1] | 0.93 [0.43, 1.98] | 1.0 | alkyne_terminal OR=7.1 (n=22); ether_aryl OR=3.9 (n=12); methylene OR=3.6 (n=903) |
| SMITH-BR6-ACID-CO | group | carboxylic_acids | 1210-1320 | 48 | 0.94 | 0.02 | 1.0 [0.9, 1.0] | [0.8, 1.0] | 3.33 [1.05, 10.57] | 1.0 | alkene OR=10.1 (n=219); ketones OR=9.4 (n=207); aromatics OR=9.4 (n=1380) |
| SMITH-BR6-ACID-OH-IPB | group | carboxylic_acids | 1395-1440 | 48 | 0.94 | 0.19 | 1.2 [1.1, 1.2] | [1.1, 1.2] | 0.33 [0.11, 0.99] | 1.2 | alkene_vinyl OR=5.2 (n=32); aldehyde_aromatic OR=4.3 (n=61); amine_secondary_aromatic OR=3.0 (n=55) |
| SMITH-BR6-ACID-OH-STR | group | carboxylic_acids | 2500-3500 | 48 | 0.10 | 0.95 | 2.0 [0.8, 4.6] | [0.1, 5.5] | 0.95 [0.86, 1.04] | 1.0 | alcohol_tertiary OR=11.7 (n=3); amine_primary_saturated OR=8.8 (n=4); alcohol_secondary OR=5.5 (n=10) |
| SMITH-BR7-EST-AR-OCC | group | ester_aromatic | 1100-1130 | 116 | 0.41 | 0.83 | 2.5 [1.9, 3.2] | [1.9, 3.3] | 0.70 [0.60, 0.82] | 1.1 | ether_mixed OR=4.6 (n=83); ether OR=3.4 (n=94); alkane OR=3.1 (n=212) |
| SMITH-BR7-EST-AR-CCO | group | ester_aromatic | 1250-1310 | 116 | 0.79 | 0.82 | 4.4 [3.8, 5.1] | [3.2, 6.5] | 0.25 [0.18, 0.36] | 1.1 | carboxylic_acid_aromatic OR=20.3 (n=22); carboxylic_acids OR=6.4 (n=26); ether_aryl OR=6.4 (n=7) |
| SMITH-BR7-EST-AR-CO | group | ester_aromatic | 1715-1730 | 116 | 0.28 | 0.95 | 6.1 [4.2, 8.9] | [3.6, 10.3] | 0.75 [0.67, 0.84] | 2.2 | alcohol_tertiary OR=13.6 (n=3); ketone_saturated OR=13.4 (n=14); esters OR=13.1 (n=36) |
| SMITH-BR7-EST-SAT-OCC | group | ester_saturated | 1030-1100 | 128 | 0.28 | 0.71 | 1.0 [0.7, 1.3] | [0.6, 1.4] | 1.01 [0.90, 1.13] | 1.0 | aldehyde_saturated OR=17.7 (n=3); ether_saturated OR=7.7 (n=40); alcohol_tertiary OR=6.6 (n=6) |
| SMITH-BR7-EST-SAT-CCO | group | ester_saturated | 1160-1210 | 128 | 0.51 | 0.75 | 2.0 [1.6, 2.4] | [1.2, 2.8] | 0.66 [0.55, 0.79] | 0.9 | nitrile_saturated OR=20.7 (n=3); amine_secondary_saturated OR=10.9 (n=5); amide_primary OR=4.1 (n=3) |
| SMITH-BR7-EST-SAT-CO | group | ester_saturated | 1735-1755 | 128 | 0.40 | 0.99 | 43.2 [24.2, 77.3] | [18.4, 116.4] | 0.61 [0.53, 0.70] | 2.9 | ketone_saturated OR=17.3 (n=3); carboxylic_acids OR=15.5 (n=4); esters OR=15.2 (n=8) |
| SMITH-BR5-ETHER-ARYL-CO | group | ether_aryl | 1200-1300 | 13 | 1.00 | 0.01 | 1.0 [0.9, 1.1] | [0.9, 1.0] | 2.42 [0.15, 38.01] | 1.0 | esters OR=9.6 (n=264); aromatics OR=7.2 (n=1410); ketones OR=7.2 (n=207) |
| SMITH-BR5-ETHER-MIX-CO-SAT | group | ether_mixed | 1010-1050 | 229 | 0.94 | 0.17 | 1.1 [1.1, 1.2] | [1.0, 1.2] | 0.36 [0.22, 0.61] | 1.1 | nitriles OR=30.6 (n=70); nitrile_aromatic OR=29.7 (n=68); alkyne_internal OR=9.4 (n=65) |
| SMITH-BR5-ETHER-MIX-CO-AR | group | ether_mixed | 1200-1300 | 229 | 0.99 | 0.01 | 1.0 [1.0, 1.0] | [1.0, 1.0] | 0.57 [0.13, 2.43] | 1.0 | esters OR=8.7 (n=226); aromatics OR=7.0 (n=1196); ketones OR=6.1 (n=166) |
| SMITH-BR5-ETHER-SAT-CO | group | ether_saturated | 1070-1140 | 83 | 0.88 | 0.05 | 0.9 [0.8, 1.0] | [0.8, 1.0] | 2.54 [1.36, 4.75] | 0.9 | aromatics OR=6.5 (n=1329); aromatic_para OR=2.9 (n=400); ketone_saturated OR=2.7 (n=26) |
| SMITH-BR6-KET-AR-CCC | group | ketone_aromatic | 1230-1300 | 159 | 0.45 | 0.70 | 1.5 [1.2, 1.8] | [0.8, 2.3] | 0.79 [0.68, 0.91] | 1.0 | carboxylic_acid_aromatic OR=48.3 (n=28); ester_aromatic OR=18.0 (n=92); carboxylic_acids OR=6.7 (n=35) |
| SMITH-BR6-KET-AR-CO | group | ketone_aromatic | 1640-1700 | 159 | 0.54 | 0.79 | 2.5 [2.1, 3.0] | [1.7, 3.4] | 0.59 [0.50, 0.70] | 1.4 | carboxylic_acid_aromatic OR=17.8 (n=24); carboxylic_acids OR=10.9 (n=35); carbonyl_any OR=8.5 (n=232) |
| SMITH-BR6-KET-SAT-CCC | group | ketone_saturated | 1100-1230 | 41 | 0.41 | 0.51 | 0.8 [0.6, 1.2] | [0.5, 1.3] | 1.16 [0.89, 1.50] | 1.0 | amine_secondary_saturated OR=15.8 (n=22); ester_saturated OR=10.8 (n=105); nitrile_saturated OR=7.2 (n=3) |
| SMITH-BR6-KET-SAT-CO | group | ketone_saturated | 1705-1725 | 41 | 0.58 | 0.90 | 5.9 [4.4, 7.9] | [3.2, 9.6] | 0.46 [0.32, 0.66] | 3.0 | ester_aromatic OR=20.5 (n=66); esters OR=10.2 (n=87); methyl OR=5.1 (n=136) |
| SMITH-BR4-CH3-UMBRELLA | group | methyl | 1365-1385 | 1069 | 0.61 | 0.71 | 2.1 [1.8, 2.4] | [1.8, 2.6] | 0.55 [0.50, 0.60] | 2.1 | esters OR=6.6 (n=6); ether_mixed OR=5.4 (n=9); methylene_chain_4 OR=4.9 (n=10) |
| SMITH-BR4-CH3-SYM | group | methyl | 2862-2882 | 1069 | 0.29 | 0.90 | 2.8 [2.1, 3.7] | [1.9, 4.3] | 0.79 [0.75, 0.83] | 2.8 | aromatic_meta OR=7.5 (n=4); alcohol_primary OR=5.7 (n=3); alcohol_secondary OR=4.2 (n=3) |
| SMITH-BR4-CH3-ASYM | group | methyl | 2952-2972 | 1069 | 0.46 | 0.80 | 2.2 [1.9, 2.7] | [1.7, 3.2] | 0.68 [0.64, 0.73] | 2.2 | ketone_saturated OR=5.7 (n=3); methylene OR=4.0 (n=78); alkane OR=3.2 (n=80) |
| SMITH-BR4-CH2-SYM | group | methylene | 2845-2865 | 1007 | 0.42 | 0.80 | 2.1 [1.7, 2.5] | [1.4, 3.4] | 0.73 [0.68, 0.78] | 2.1 | aromatics OR=4.4 (n=108); aromatic_meta OR=3.3 (n=11); ether_saturated OR=2.5 (n=3) |
| SMITH-BR4-CH2-ASYM | group | methylene | 2916-2936 | 1007 | 0.69 | 0.59 | 1.7 [1.5, 1.9] | [1.4, 2.0] | 0.52 [0.46, 0.59] | 1.7 | aromatics OR=3.5 (n=217); alcohol_secondary OR=3.1 (n=11); alkane OR=2.3 (n=87) |
| SMITH-BR4-CH2-ROCK | group | methylene_chain_4 | 710-730 | 130 | 0.74 | 0.45 | 1.3 [1.2, 1.5] | [1.1, 1.6] | 0.58 [0.43, 0.78] | 1.3 | aromatics OR=4.5 (n=755); nitrile_aromatic OR=3.9 (n=52); nitriles OR=3.8 (n=54) |
| SMITH-BR8-NH-ANY | class | n_h_any | 3300-3500 | 324 | 0.60 | 0.68 | 1.9 [1.7, 2.1] | [1.6, 2.4] | 0.58 [0.51, 0.67] | 1.9 | alcohol_primary OR=24.7 (n=16); alcohol_secondary OR=5.0 (n=31); alcohol_tertiary OR=3.4 (n=5) |
| SMITH-NIT19-AR-CN | group | nitrile_aromatic | 2220-2240 | 69 | 0.06 | 1.00 | 189.1 [10.3, 3478.5] | [28.3, 390.3] | 0.94 [0.88, 1.00] | 10.1 |  |
| SMITH-NIT19-SAT-CN | group | nitrile_saturated | 2240-2260 | 3 (underpowered) | 0.00 | 1.00 | 384.2 [8.6, 17094.1] |  | 0.88 [0.60, 1.27] | 12.9 |  |
| SMITH-NO2-20-SCIS | group | nitro | 835-890 | 50 | 0.90 | 0.43 | 1.6 [1.4, 1.8] | [1.3, 1.8] | 0.23 [0.10, 0.53] | 1.1 | aldehyde_saturated OR=5.3 (n=3); carboxylic_acid_aromatic OR=5.0 (n=22); alcohol_tertiary OR=3.8 (n=7) |
| SMITH-NO2-20-SYM | group | nitro | 1330-1390 | 50 | 0.72 | 0.85 | 4.7 [3.8, 5.8] | [3.5, 6.3] | 0.33 [0.21, 0.52] | 1.1 | nitrile_aromatic OR=3.8 (n=26); nitriles OR=3.5 (n=26); aromatics OR=2.8 (n=224) |
| SMITH-NO2-20-ASYM | group | nitro | 1500-1550 | 50 | 0.82 | 0.84 | 5.3 [4.4, 6.3] | [4.1, 7.1] | 0.21 [0.12, 0.39] | 1.6 | nitrile_saturated OR=38.6 (n=3); amide_secondary OR=5.5 (n=64); n_h_any OR=4.8 (n=113) |
| SMITH-BR5-PHENOL-CO | group | phenol | 1200-1260 | 64 | 0.89 | 0.09 | 1.0 [0.9, 1.1] | [0.9, 1.1] | 1.21 [0.59, 2.49] | 1.0 | alkene_vinyl OR=7.0 (n=34); ketone_aromatic OR=6.7 (n=152); ketones OR=6.5 (n=198) |

## Stratum: salt (n = 35)

| rule | tier | truth group | window | n+ | sens | spec | LR+ [CI] | LR+ boot | LR- [CI] | LR+ pos | FP enriched in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SMITH-SALT19-NH3-SYM | group | ammonium_primary | 1500-1550 | 6 (underpowered) | 0.83 | 0.38 | 1.3 [0.8, 2.1] |  | 0.44 [0.07, 2.79] | 1.3 |  |
| SMITH-SALT19-NH3-ASYM | group | ammonium_primary | 1560-1625 | 6 (underpowered) | 1.00 | 0.10 | 1.1 [0.8, 1.3] |  | 0.61 [0.04, 10.55] | 1.1 |  |
| SMITH-SALT19-NH3-STR | group | ammonium_primary | 2800-3200 | 6 (underpowered) | 1.00 | 0.00 | 0.9 [0.8, 1.2] |  | 4.29 [0.09, 197.94] | 0.9 |  |
| SMITH-SALT19-NH2-BEND | group | ammonium_secondary | 1560-1620 | 0 (underpowered) | nan | 0.11 | 0.6 [0.1, 4.1] |  | 4.00 [0.47, 34.07] | 0.6 |  |
| SMITH-SALT19-NH2-STR | group | ammonium_secondary | 2700-3000 | 0 (underpowered) | nan | 0.06 | 0.5 [0.1, 3.8] |  | 7.20 [0.72, 71.53] | 0.5 |  |
| SMITH-SALT19-NH-STR | group | ammonium_tertiary | 2300-2700 | 0 (underpowered) | nan | 0.37 | 0.8 [0.1, 5.8] |  | 1.33 [0.18, 9.90] | 0.8 |  |

## Prominence sweep (LR+, full definition, main stratum)

| rule | p>=0.01 | p>=0.02 | p>=0.05 | p>=0.1 |
| --- | --- | --- | --- | --- |
| SMITH-ALD17-AR-CO | 1.4 | 1.5 | 1.5 | 1.5 |
| SMITH-ALD17-CH-BEND | 1.3 | 1.4 | 1.3 | 1.3 |
| SMITH-ALD17-CH-STR | 1.9 | 2.1 | 2.1 | 2.5 |
| SMITH-ALD17-SAT-CO | 1.7 | 1.7 | 1.8 | 1.8 |
| SMITH-ALK16-CC-STR | 1.1 | 1.3 | 1.4 | 1.5 |
| SMITH-ALK16-CH-STR | 1.0 | 0.9 | 0.6 | 0.7 |
| SMITH-ALK16-TRISUB-CC | 2.2 | 2.1 | 2.3 | 2.2 |
| SMITH-ALK16-TRISUB-WAG | 1.1 | 1.1 | 1.1 | 1.2 |
| SMITH-ALK16-VINYL-CC | 2.2 | 2.5 | 2.3 | 2.5 |
| SMITH-ALK16-VINYL-WAG1 | 2.1 | 2.2 | 2.5 | 3.1 |
| SMITH-ALK16-VINYL-WAG2 | 1.3 | 1.5 | 1.5 | 0.7 |
| SMITH-ALY17-INT-CC | 1.7 | 3.4 | 7.3 | 6.8 |
| SMITH-ALY17-TERM-CC | 1.5 | 2.7 | 14.5 | 15.8 |
| SMITH-ALY17-TERM-CH | 2.5 | 3.8 | 4.5 | 5.7 |
| SMITH-ALY17-TERM-CH-BEND | 1.0 | 1.1 | 1.1 | 1.1 |
| SMITH-BR4-BZ-META-690 | 1.2 | 1.3 | 1.5 | 1.8 |
| SMITH-BR4-BZ-META-BOTH | 1.3 | 1.4 | 1.7 | 2.2 |
| SMITH-BR4-BZ-META-OOP | 1.1 | 1.1 | 1.1 | 1.2 |
| SMITH-BR4-BZ-MONO-690 | 1.7 | 1.9 | 2.4 | 3.2 |
| SMITH-BR4-BZ-MONO-BOTH | 1.8 | 2.0 | 2.6 | 3.6 |
| SMITH-BR4-BZ-MONO-OOP | 1.0 | 1.1 | 1.1 | 1.1 |
| SMITH-BR4-BZ-ORTHO-OOP | 0.8 | 0.8 | 0.8 | 1.0 |
| SMITH-BR4-BZ-PARA-OOP | 1.2 | 1.2 | 1.3 | 1.4 |
| SMITH-BR4-CH2-ASYM | 1.4 | 1.7 | 2.4 | 3.3 |
| SMITH-BR4-CH2-ROCK | 1.3 | 1.3 | 1.4 | 1.4 |
| SMITH-BR4-CH2-SYM | 1.4 | 2.1 | 6.0 | 8.7 |
| SMITH-BR4-CH3-ASYM | 1.9 | 2.2 | 4.1 | 6.8 |
| SMITH-BR4-CH3-SYM | 2.8 | 2.8 | 2.8 | 1.9 |
| SMITH-BR4-CH3-UMBRELLA | 1.9 | 2.1 | 2.3 | 2.5 |
| SMITH-BR5-CO-GENERAL | 1.4 | 1.4 | 1.4 | 1.4 |
| SMITH-BR5-ETHER-ARYL-CO | 1.0 | 1.0 | 1.0 | 1.1 |
| SMITH-BR5-ETHER-MIX-CO-AR | 1.0 | 1.0 | 1.0 | 1.1 |
| SMITH-BR5-ETHER-MIX-CO-SAT | 1.1 | 1.1 | 1.2 | 1.4 |
| SMITH-BR5-ETHER-SAT-CO | 0.9 | 0.9 | 0.9 | 0.9 |
| SMITH-BR5-PHENOL-CO | 1.0 | 1.0 | 1.1 | 1.1 |
| SMITH-BR5-ROH-OH-STR | 1.0 | 1.3 | 2.0 | 2.6 |
| SMITH-BR5-ROH-OH-WAG | 1.0 | 1.0 | 0.9 | 1.0 |
| SMITH-BR5-ROH-PRIM-CO | 1.0 | 1.0 | 1.0 | 1.1 |
| SMITH-BR5-ROH-SEC-CO | 1.0 | 1.0 | 1.0 | 0.9 |
| SMITH-BR5-ROH-TERT-CO | 0.9 | 1.0 | 1.0 | 1.0 |
| SMITH-BR6-ACID-AR-CO | 4.7 | 4.8 | 4.8 | 4.9 |
| SMITH-BR6-ACID-CO | 1.0 | 1.0 | 1.0 | 1.0 |
| SMITH-BR6-ACID-OH-IPB | 1.1 | 1.2 | 1.1 | 1.1 |
| SMITH-BR6-ACID-OH-OOP | 1.0 | 1.0 | 1.0 | 1.0 |
| SMITH-BR6-ACID-OH-STR | 2.0 | 2.0 | 2.0 | 2.0 |
| SMITH-BR6-ACID-SAT-CO | 1.3 | 1.3 | 1.3 | 1.4 |
| SMITH-BR6-CO-GENERAL | 4.0 | 4.0 | 4.0 | 4.0 |
| SMITH-BR6-KET-AR-CCC | 1.5 | 1.5 | 1.5 | 1.4 |
| SMITH-BR6-KET-AR-CO | 2.5 | 2.5 | 2.5 | 2.5 |
| SMITH-BR6-KET-SAT-CCC | 0.8 | 0.8 | 0.8 | 0.8 |
| SMITH-BR6-KET-SAT-CO | 5.9 | 5.9 | 5.9 | 5.7 |
| SMITH-BR7-CARB-AR-CO | 30.2 | 30.2 | 30.2 | 30.2 |
| SMITH-BR7-CARB-AR-OCO | 4.8 | 4.8 | 5.0 | 5.3 |
| SMITH-BR7-CARB-MIX-CO | 34.2 | 34.2 | 34.2 | 34.2 |
| SMITH-BR7-CARB-MIX-OCO | 3.1 | 3.1 | 3.3 | 3.4 |
| SMITH-BR7-CARB-OCC | 2.1 | 2.1 | 2.1 | 2.1 |
| SMITH-BR7-CARB-SAT-CO | 2.6 | 2.6 | 2.7 | 2.7 |
| SMITH-BR7-CARB-SAT-OCO | 2.2 | 2.2 | 2.2 | 2.3 |
| SMITH-BR7-EST-AR-CCO | 4.4 | 4.4 | 4.4 | 4.4 |
| SMITH-BR7-EST-AR-CO | 6.3 | 6.1 | 6.2 | 6.4 |
| SMITH-BR7-EST-AR-OCC | 2.5 | 2.5 | 2.2 | 2.2 |
| SMITH-BR7-EST-SAT-CCO | 2.0 | 2.0 | 2.0 | 2.0 |
| SMITH-BR7-EST-SAT-CO | 44.1 | 43.2 | 45.9 | 49.1 |
| SMITH-BR7-EST-SAT-OCC | 1.0 | 1.0 | 1.0 | 1.0 |
| SMITH-BR8-AMD-CO | 3.1 | 3.1 | 3.2 | 3.2 |
| SMITH-BR8-AMD1-CN | 0.8 | 0.8 | 0.9 | 0.8 |
| SMITH-BR8-AMD1-NH-STR | 1.3 | 1.3 | 0.8 | 1.1 |
| SMITH-BR8-AMD1-SCIS | 1.1 | 0.7 | 1.1 | 1.3 |
| SMITH-BR8-AMD1-WAG | 0.9 | 0.9 | 1.0 | 1.0 |
| SMITH-BR8-AMD2-CN | 1.0 | 1.0 | 1.0 | 1.0 |
| SMITH-BR8-AMD2-NH-IPB | 3.9 | 3.9 | 3.8 | 3.8 |
| SMITH-BR8-AMD2-NH-STR | 2.4 | 3.8 | 5.2 | 5.6 |
| SMITH-BR8-AMD2-WAG | 1.0 | 1.0 | 1.1 | 1.1 |
| SMITH-BR8-AMN1-AR-ASYM | 2.6 | 6.8 | 14.0 | 21.5 |
| SMITH-BR8-AMN1-AR-CN | 1.0 | 1.0 | 1.0 | 1.0 |
| SMITH-BR8-AMN1-AR-SYM | 2.1 | 3.6 | 6.7 | 7.9 |
| SMITH-BR8-AMN1-SAT-ASYM | 5.7 | 8.7 | 8.4 | 4.1 |
| SMITH-BR8-AMN1-SAT-CN | 1.0 | 1.0 | 0.8 | 0.8 |
| SMITH-BR8-AMN1-SAT-SYM | 2.6 | 3.5 | 1.8 | 0.6 |
| SMITH-BR8-AMN1-SCIS | 1.1 | 1.0 | 1.1 | 1.2 |
| SMITH-BR8-AMN1-WAG | 1.0 | 1.0 | 1.0 | 1.0 |
| SMITH-BR8-AMN2-AR-CNC | 1.0 | 1.1 | 1.1 | 1.2 |
| SMITH-BR8-AMN2-AR-NH | 1.1 | 2.3 | 4.8 | 4.3 |
| SMITH-BR8-AMN2-SAT-CNC | 1.1 | 1.1 | 1.2 | 1.4 |
| SMITH-BR8-AMN2-SAT-NH | 2.5 | 0.9 | 0.2 | 0.3 |
| SMITH-BR8-AMN2-WAG | 1.1 | 1.1 | 1.1 | 1.1 |
| SMITH-BR8-NH-ANY | 1.1 | 1.9 | 3.4 | 4.4 |
| SMITH-BZ16-ARCH-STR | 2.6 | 2.9 | 2.5 | 1.3 |
| SMITH-BZ16-OOP | 1.0 | 1.0 | 1.0 | 1.0 |
| SMITH-BZ16-RING | 1.0 | 1.0 | 1.1 | 1.1 |
| SMITH-NIT19-AR-CN | 189.1 | 189.1 | 189.1 | 189.1 |
| SMITH-NIT19-SAT-CN | 384.2 | 384.2 | 384.2 | 384.2 |
| SMITH-NO2-20-ASYM | 5.3 | 5.3 | 5.3 | 5.3 |
| SMITH-NO2-20-SCIS | 1.6 | 1.6 | 1.6 | 1.6 |
| SMITH-NO2-20-SYM | 4.7 | 4.7 | 4.7 | 4.7 |

## Not evaluable (5 rules)

- SMITH-ALK16-CIS-CC: cis alkene.  NOT EVALUABLE: cis/trans needs stereo marks that most depositor SMILES lack (decision D6)
- SMITH-ALK16-CIS-WAG: cis alkene. Wide tolerance in the source (+-50) NOT EVALUABLE: cis/trans needs stereo marks that most depositor SMILES lack (decision D6)
- SMITH-ALK16-TRANS-CC: trans alkene.  NOT EVALUABLE: cis/trans needs stereo marks that most depositor SMILES lack (decision D6)
- SMITH-ALK16-TRANS-WAG: trans alkene.  NOT EVALUABLE: cis/trans needs stereo marks that most depositor SMILES lack (decision D6)
- SMITH-SALT19-COMB: amine salt. All three salt types. This is the window where salts mimic alkynes and nitriles (an IR trap for the analysis)
