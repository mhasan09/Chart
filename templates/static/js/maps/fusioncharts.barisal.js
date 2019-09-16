(function(factory){if(typeof module==="object"&&typeof module.exports!=="undefined"){module.exports=factory}else{factory(FusionCharts)}})(function(FusionCharts){(function(modules){var installedModules={};function __webpack_require__(moduleId){if(installedModules[moduleId]){return installedModules[moduleId].exports}var module=installedModules[moduleId]={i:moduleId,l:false,exports:{}};modules[moduleId].call(module.exports,module,module.exports,__webpack_require__);module.l=true;return module.exports}__webpack_require__.m=modules;__webpack_require__.c=installedModules;__webpack_require__.d=function(exports,name,getter){if(!__webpack_require__.o(exports,name)){Object.defineProperty(exports,name,{configurable:false,enumerable:true,get:getter})}};__webpack_require__.r=function(exports){Object.defineProperty(exports,"__esModule",{value:true})};__webpack_require__.n=function(module){var getter=module&&module.__esModule?function getDefault(){return module["default"]}:function getModuleExports(){return module};__webpack_require__.d(getter,"a",getter);return getter};__webpack_require__.o=function(object,property){return Object.prototype.hasOwnProperty.call(object,property)};__webpack_require__.p="";return __webpack_require__(__webpack_require__.s=294)})({294:function(module,exports,__webpack_require__){"use strict";var _fusioncharts=__webpack_require__(295);var _fusioncharts2=_interopRequireDefault(_fusioncharts);function _interopRequireDefault(obj){return obj&&obj.__esModule?obj:{"default":obj}}FusionCharts.addDep(_fusioncharts2["default"])},295:function(module,exports,__webpack_require__){"use strict";exports.__esModule=true;
/**!
 * @license FusionCharts JavaScript Library
 * Copyright FusionCharts Technologies LLP
 * License Information at <http://www.fusioncharts.com/license>
 *
 * @author FusionCharts Technologies LLP
 * @meta package_map_pack
 * @id fusionmaps.Barisal.17.11-26-2015 08:30:20
 */var M="M",L="L",Z="Z",Q="Q",LFT="left",RGT="right",CEN="center",MID="middle",TOP="top",BTM="bottom",geodefinitions=[{name:"Barisal",revision:17,standaloneInit:true,baseWidth:405,baseHeight:500,baseScaleFactor:10,entities:{"BD.BA.BG":{outlines:[[M,1541,2286,L,1505,2286,1505,2305,Q,1501,2308,1488,2308,L,1455,2304,Q,1447,2304,1442,2313,1436,2323,1424,2324,L,1368,2324,1368,2344,1356,2344,Q,1346,2331,1350,2261,L,1350,2240,1155,2240,1155,2292,1139,2292,1139,2389,Q,1139,2458,1106,2537,1104,2541,1088,2575,1078,2581,1047,2588,1025,2597,991,2636,988,2653,958,2676,945,2684,921,2723,906,2746,886,2765,885,2768,877,2795,872,2810,853,2805,847,2789,822,2789,794,2793,784,2792,771,2778,759,2779,L,721,2779,718,2752,691,2749,Q,691,2755,690,2772,688,2794,684,2836,684,2854,700,2929,700,2972,697,2990,680,3006,680,3012,680,3036,678,3047,676,3051,657,3077,655,3087,655,3112,652,3122,638,3139,627,3152,631,3165,590,3247,583,3274,581,3282,570,3298,559,3310,560,3323,527,3352,531,3372,L,482,3372,Q,482,3352,442,3352,359,3451,328,3475,297,3496,244,3517,233,3526,203,3529,174,3534,162,3541,L,162,3561,Q,136,3566,137,3624,138,3654,144,3690,L,144,3777,Q,144,3815,166,3851,177,3886,172,3935,171,3949,180,3965,189,3983,187,4003,183,4037,266,4136,284,4184,343,4257,L,365,4257,Q,365,4236,403,4195,441,4155,441,4148,441,4133,439,4132,425,4131,408,4120,399,4113,399,4099,398,4084,395,4081,L,395,3962,431,3962,433,3941,Q,453,3940,502,3940,L,502,3907,Q,523,3913,526,3894,529,3871,533,3861,545,3834,545,3795,L,563,3795,Q,563,3817,613,3895,614,3914,599,3919,580,3927,571,3950,559,3977,524,4012,524,4020,525,4053,525,4077,508,4090,L,508,4208,Q,577,4191,650,4223,733,4261,785,4258,L,785,4277,727,4307,Q,705,4318,663,4323,596,4365,506,4355,L,506,4391,Q,502,4413,488,4425,488,4461,504,4490,511,4550,519,4559,528,4570,554,4612,595,4652,595,4668,595,4689,573,4704,552,4718,552,4745,552,4762,595,4763,645,4763,651,4766,690,4788,753,4800,772,4809,809,4814,824,4820,846,4848,855,4854,926,4926,L,982,4926,Q,1e3,4955,1027,4954,1082,4950,1085,4970,L,1113,4970,Q,1114,4942,1134,4931,1158,4923,1169,4914,1217,4878,1258,4860,1313,4838,1344,4836,1383,4834,1418,4810,L,1420,4804,Q,1422,4745,1410,4714,1397,4679,1396,4644,1397,4589,1444,4547,1517,4482,1533,4454,1599,4386,1601,4351,1611,4253,1606,4202,1594,4083,1675,3987,1730,3926,1750,3898,1784,3852,1796,3799,L,1808,3801,Q,1823,3672,1825,3665,L,1825,3596,Q,1796,3591,1752,3568,1713,3547,1688,3545,L,1688,3525,Q,1734,3526,1761,3456,1778,3440,1825,3378,1829,3372,1900,3307,1912,3295,1951,3271,1960,3266,1960,3233,1960,3217,1951,3205,1941,3190,1939,3172,1939,3121,1937,3099,1858,3087,1697,3096,1568,3100,1557,3052,L,1527,3052,Q,1526,3062,1474,3099,1435,3126,1416,3127,1399,3127,1384,3147,1368,3172,1362,3174,1356,3177,1330,3180,1332,3207,1312,3199,1313,3231,1290,3230,L,1290,3242,1271,3242,Q,1226,3187,1225,3171,1225,3127,1237,3112,1252,3088,1252,3058,L,1252,2926,Q,1262,2925,1298,2925,1329,2921,1315,2893,L,1382,2893,Q,1369,2867,1418,2865,1445,2866,1497,2865,1515,2861,1514,2847,L,1513,2818,Q,1536,2794,1538,2792,1542,2785,1541,2762,1541,2736,1532,2724,1517,2700,1513,2692,L,1513,2675,Q,1513,2658,1492,2630,1471,2601,1471,2586,1471,2582,1500,2543,1533,2498,1557,2473,1592,2453,1607,2425,1621,2398,1658,2400,1701,2402,1731,2394,1734,2374,1737,2364,1742,2362,1759,2347,1759,2310,1778,2292,1795,2276,1797,2240,1796,2238,1794,2235,1780,2219,1741,2201,1690,2177,1681,2168,L,1626,2168,Q,1625,2173,1625,2189,1624,2202,1611,2197,L,1611,2215,1595,2215,1595,2186,1573,2186,1573,2208,1541,2208,Z]],label:"Barguna District",shortLabel:"BG",labelPosition:[104.8,378.4],labelAlignment:[CEN,MID]},"BD.BA.BS":{outlines:[[M,2023,290,Q,2011,277,1974,283,L,1974,279,Q,1913,294,1895,297,1845,324,1806,325,1765,325,1746,370,1743,377,1733,404,1713,427,1715,441,1717,441,1719,444,L,1719,479,1705,479,1705,493,1687,493,Q,1695,470,1685,464,1668,458,1658,448,1634,424,1624,419,L,1548,418,1548,439,1509,439,Q,1491,437,1467,437,L,1467,469,1432,469,Q,1387,451,1381,450,1367,451,1352,435,1336,419,1331,418,1300,393,1280,391,1243,388,1243,362,1242,271,1269,193,L,1269,52,Q,1232,52,1238,31,L,1218,31,Q,1208,46,1187,81,1171,98,1137,111,1128,123,1070,122,1039,122,1016,122,965,122,958,122,L,958,181,Q,965,189,973,204,L,973,264,846,264,846,353,777,353,Q,754,373,750,373,L,704,373,Q,704,453,693,464,689,467,687,503,L,659,530,Q,561,618,561,651,561,659,576,714,577,739,566,751,L,566,762,Q,591,817,610,829,618,834,640,865,660,895,660,900,660,912,651,917,642,923,640,938,L,640,1019,734,1019,Q,744,1053,758,1071,771,1086,787,1124,822,1156,853,1153,885,1150,889,1198,891,1228,941,1229,1001,1230,1013,1247,1018,1254,1098,1254,1108,1262,1116,1265,L,1116,1242,Q,1140,1229,1177,1196,1210,1176,1209,1172,1216,1161,1252,1165,L,1252,1147,1287,1147,Q,1278,1170,1294,1190,1312,1214,1312,1228,1330,1228,1334,1230,L,1373,1230,Q,1372,1217,1374,1212,L,1444,1212,Q,1479,1276,1553,1352,L,1553,1368,1514,1368,1514,1382,1495,1382,1495,1473,Q,1501,1479,1586,1498,1592,1499,1622,1525,1627,1530,1656,1565,1741,1568,1870,1578,L,1870,1642,1808,1642,1808,1681,1790,1681,1790,1726,1837,1726,1837,1746,1939,1746,1939,1811,1905,1811,1905,1830,1851,1830,1851,1885,Q,1843,1885,1830,1894,L,1830,1923,1797,1923,1797,1907,1709,1907,1709,1885,1696,1885,1696,1869,1667,1869,1667,1903,1642,1903,Q,1650,1923,1621,1923,1584,1919,1570,1920,1566,1920,1537,1970,1511,2009,1511,2036,1511,2055,1462,2069,1446,2082,1433,2092,1425,2098,1388,2108,1355,2130,1323,2156,1303,2170,1278,2181,1262,2187,1240,2190,1225,2215,1219,2215,1206,2215,1199,2226,1193,2234,1193,2240,L,1350,2240,1350,2261,Q,1346,2331,1356,2344,L,1368,2344,1368,2324,1424,2324,Q,1436,2323,1442,2313,1447,2304,1455,2304,L,1488,2308,Q,1501,2308,1505,2305,L,1505,2286,1541,2286,1541,2208,1573,2208,1573,2186,1595,2186,1595,2215,1611,2215,1611,2197,Q,1624,2202,1625,2189,1625,2173,1626,2168,L,1681,2168,Q,1690,2177,1741,2201,1780,2219,1794,2235,1796,2238,1797,2240,1817,2272,1966,2259,1985,2256,1986,2239,1985,2218,1986,2208,1987,2197,2002,2179,2015,2164,2013,2156,L,2014,2120,Q,2014,2107,2031,2102,2025,2078,2040,2074,2049,2073,2069,2074,L,2069,2056,Q,2094,2067,2104,2049,2116,2027,2129,2026,2143,2025,2165,2012,2181,2003,2225,2007,2269,2010,2275,1993,2281,1977,2286,1917,L,2286,1863,Q,2255,1839,2255,1823,2255,1804,2266,1792,2280,1776,2283,1765,2277,1748,2289,1733,2303,1716,2303,1705,2303,1684,2290,1671,2263,1647,2253,1631,2249,1627,2241,1588,2235,1562,2210,1561,L,2210,1544,Q,2267,1544,2368,1524,2388,1512,2395,1476,2398,1436,2401,1423,2424,1383,2459,1348,2485,1320,2542,1267,2573,1259,2585,1249,2611,1221,2622,1212,2695,1170,2710,1158,2737,1134,2803,1107,2828,1096,2906,1044,2938,1032,2948,1026,2966,1013,2972,993,2938,853,2848,761,2822,728,2806,712,2781,686,2730,664,2639,633,2589,612,2359,512,2314,454,2273,400,2190,370,2113,342,2086,306,2084,304,2083,303,L,2060,305,Q,2037,305,2023,290,Z]],label:"Barisal District",shortLabel:"BS",labelPosition:[176.7,93],labelAlignment:[CEN,MID]},"BD.BA.BL":{outlines:[[M,2713,4307,Q,2720,4334,2703,4347,2680,4366,2675,4379,2665,4408,2648,4413,2637,4418,2637,4444,2637,4450,2662,4471,2685,4490,2692,4493,2736,4511,2738,4550,L,2773,4550,2773,4535,2805,4502,Q,2856,4472,2843,4462,L,2825,4462,Q,2828,4434,2776,4391,2727,4350,2738,4307,Z],[M,2905,4196,Q,2905,4210,2885,4229,2873,4240,2879,4273,2872,4293,2860,4294,2852,4295,2852,4305,2852,4324,2879,4326,2895,4326,2943,4326,3044,4322,3048,4319,L,3048,4298,3023,4298,Q,2960,4164,2917,4186,L,2917,4152,2905,4152,Z],[M,3857,2823,Q,3843,2853,3833,2901,3789,3002,3773,3065,3750,3169,3712,3247,L,3708,3452,Q,3708,3541,3712,3553,3719,3577,3772,3637,3790,3659,3829,3695,3849,3714,3854,3727,3864,3748,3870,3748,L,3883,3748,Q,3890,3748,3893,3329,3917,3319,3917,3284,3912,3244,3913,3230,3920,3170,3941,3137,3997,3069,4008,3052,4022,3033,4022,2966,4022,2907,4020,2903,4016,2893,3970,2851,3963,2846,3936,2798,3919,2764,3888,2764,3865,2764,3865,2781,Q,3865,2810,3857,2823,Z],[M,3218,1734,Q,3209,1692,3175,1599,3145,1515,3138,1463,3107,1372,3093,1322,3091,1314,3081,1249,3076,1218,3060,1205,L,3060,1182,3059,1182,Q,3030,1174,3016,1174,2979,1174,2902,1198,2833,1219,2780,1214,2787,1260,2737,1280,2666,1308,2656,1319,2647,1329,2582,1358,2541,1387,2513,1415,2515,1458,2494,1488,2481,1506,2445,1550,2432,1569,2431,1637,2408,1700,2408,1709,2409,1763,2464,1820,2496,1853,2570,1923,2598,1953,2654,2004,2692,2056,2676,2142,2673,2167,2676,2218,2675,2246,2710,2283,2747,2419,2750,2426,2754,2436,2780,2479,2802,2515,2808,2549,2811,2574,2825,2615,2837,2646,2841,2673,2841,2676,2841,2679,L,2841,2785,Q,2856,2838,2864,2864,2866,2873,2865,2930,2866,2991,2846,3032,2831,3060,2841,3145,2851,3216,2829,3255,2817,3278,2783,3320,L,2781,3321,Q,2746,3349,2655,3489,2620,3525,2612,3529,2587,3541,2581,3575,2568,3590,2538,3612,2516,3632,2516,3658,2516,3672,2587,3729,2657,3785,2657,3805,2657,3825,2613,3870,2599,3880,2571,3941,2571,3946,2601,4013,2631,4086,2631,4122,2632,4140,2628,4150,2628,4155,2645,4171,2653,4179,2663,4204,2668,4215,2681,4212,2684,4212,2687,4211,2704,4202,2729,4176,2761,4143,2781,4132,2820,4103,2848,4087,2869,4075,2911,4062,2959,4044,2957,4001,2956,3992,2974,3969,2990,3952,2983,3938,2996,3914,3007,3912,3016,3909,3050,3910,3060,3909,3072,3890,3079,3886,3104,3888,3193,3877,3221,3820,3237,3778,3244,3757,3259,3719,3279,3701,3333,3671,3344,3661,3373,3631,3392,3622,3420,3608,3426,3568,3427,3563,3428,3503,3428,3499,3428,3494,3412,3165,3534,2921,3527,2896,3549,2858,3574,2814,3573,2790,L,3573,2628,Q,3574,2564,3577,2558,3617,2535,3631,2521,L,3631,2445,Q,3650,2418,3654,2410,L,3654,2372,Q,3667,2319,3600,2237,3532,2156,3530,2151,3403,2022,3358,1956,3303,1886,3276,1851,Q,3228,1789,3218,1734,Z]],label:"Bhola District",shortLabel:"BL",labelPosition:[317.2,286.2],labelAlignment:[CEN,MID]},"BD.BA.JK":{outlines:[[M,1374,1212,Q,1372,1217,1373,1230,L,1334,1230,Q,1330,1228,1312,1228,1312,1214,1294,1190,1278,1170,1287,1147,L,1252,1147,1252,1165,Q,1216,1161,1209,1172,1210,1176,1177,1196,1140,1229,1116,1242,L,1116,1265,Q,1121,1267,1125,1267,L,1162,1267,Q,1187,1308,1202,1308,L,1202,1357,Q,1179,1348,1171,1355,1155,1372,1144,1376,1144,1438,1126,1445,1073,1467,1069,1470,L,1026,1501,Q,1024,1513,1024,1571,1023,1589,1008,1599,999,1605,979,1616,968,1624,927,1662,918,1671,890,1671,873,1670,876,1693,L,849,1693,849,1709,869,1709,Q,862,1737,892,1740,909,1741,912,1767,915,1771,954,1808,957,1812,957,1845,957,1875,948,1883,933,1894,909,1897,902,1905,819,1919,L,820,2184,Q,851,2180,874,2206,890,2223,944,2217,977,2231,1004,2234,1050,2234,1050,2264,1050,2299,1038,2316,1032,2329,992,2363,964,2388,934,2404,931,2418,907,2419,891,2419,893,2441,L,871,2441,870,2431,850,2431,Q,848,2422,848,2404,L,827,2404,827,2383,800,2383,Q,802,2398,780,2411,756,2426,753,2441,745,2442,741,2444,L,711,2444,711,2426,693,2426,Q,701,2400,668,2402,L,666,2374,651,2374,651,2354,632,2354,632,2394,654,2397,Q,654,2441,668,2472,669,2486,666,2520,669,2547,690,2543,L,690,2568,675,2568,Q,675,2572,660,2580,646,2587,652,2599,651,2620,619,2625,626,2645,603,2664,597,2667,597,2716,597,2779,609,2801,L,613,2802,623,2802,Q,624,2789,655,2748,L,681,2748,681,2772,690,2772,Q,691,2755,691,2749,L,718,2752,721,2779,759,2779,Q,771,2778,784,2792,794,2793,822,2789,847,2789,853,2805,872,2810,877,2795,885,2768,886,2765,906,2746,921,2723,945,2684,958,2676,988,2653,991,2636,1025,2597,1047,2588,1078,2581,1088,2575,1104,2541,1106,2537,1139,2458,1139,2389,L,1139,2292,1155,2292,1155,2240,1193,2240,Q,1193,2234,1199,2226,1206,2215,1219,2215,1225,2215,1240,2190,1262,2187,1278,2181,1303,2170,1323,2156,1355,2130,1388,2108,1425,2098,1433,2092,1446,2082,1462,2069,1511,2055,1511,2036,1511,2009,1537,1970,1566,1920,1570,1920,1584,1919,1621,1923,1650,1923,1642,1903,L,1667,1903,1667,1869,1696,1869,1696,1885,1709,1885,1709,1907,1797,1907,1797,1923,1830,1923,1830,1894,Q,1843,1885,1851,1885,L,1851,1830,1905,1830,1905,1811,1939,1811,1939,1746,1837,1746,1837,1726,1790,1726,1790,1681,1808,1681,1808,1642,1870,1642,1870,1578,Q,1741,1568,1656,1565,1627,1530,1622,1525,1592,1499,1586,1498,1501,1479,1495,1473,L,1495,1382,1514,1382,1514,1368,1553,1368,1553,1352,Q,1479,1276,1444,1212,Z]],label:"Jhalokati District",shortLabel:"JK",labelPosition:[126.8,180.5],labelAlignment:[CEN,MID]},"BD.BA.PT":{outlines:[[M,2301,4463,Q,2267,4487,2261,4544,2256,4590,2240,4598,2227,4605,2227,4640,2227,4665,2250,4673,2288,4687,2298,4696,2303,4700,2320,4704,L,2333,4719,Q,2342,4728,2390,4730,2395,4700,2426,4663,2473,4606,2479,4595,L,2479,4544,2464,4544,2464,4311,2435,4311,Q,2441,4328,2418,4351,2406,4365,2379,4392,Q,2354,4421,2301,4463,Z],[M,2147,4123,Q,2144,4099,2112,4062,2073,4018,2063,4010,2020,3970,2008,3969,2e3,3967,1972,3962,1950,3934,1938,3934,1908,3917,1904,3916,1883,3911,1872,3908,1853,3902,1858,3889,L,1845,3889,Q,1847,3925,1828,3941,1816,3952,1812,3965,1807,3993,1806,3997,1797,4019,1778,4053,1763,4104,1755,4113,1741,4125,1730,4164,1719,4202,1707,4213,1689,4230,1677,4267,1657,4291,1657,4332,L,1657,4465,Q,1654,4470,1626,4518,1624,4551,1597,4578,1577,4616,1576,4631,1572,4687,1564,4696,1550,4709,1550,4761,1552,4808,1527,4819,L,1527,4841,1551,4841,Q,1585,4822,1612,4804,1646,4791,1665,4776,1694,4752,1693,4719,1692,4703,1703,4688,1714,4675,1715,4662,1715,4660,1715,4658,1717,4642,1740,4608,1739,4556,1750,4547,1758,4541,1758,4519,1759,4498,1768,4493,1790,4483,1790,4443,L,1818,4443,1818,4477,Q,1863,4479,1889,4491,1895,4494,1919,4503,1936,4520,1946,4515,L,1970,4515,Q,1970,4542,1998,4542,2039,4542,2035,4528,2033,4515,2033,4509,2033,4496,2047,4485,2067,4472,2079,4462,2102,4442,2097,4425,2124,4391,2124,4351,2150,4326,2152,4319,L,2150,4277,Q,2166,4252,2165,4224,2151,4204,2147,4176,Q,2149,4141,2147,4123,Z],[M,2455,3945,L,2436,3945,2436,3898,2417,3895,2417,3871,2389,3871,Q,2384,3896,2357,3907,2319,3923,2311,3929,2259,3974,2221,3987,L,2221,4354,2225,4356,2238,4356,2238,4345,Q,2277,4348,2302,4292,2329,4270,2340,4257,L,2371,4214,Q,2378,4203,2408,4178,2417,4148,2432,4137,2458,4115,2458,4038,Q,2458,3975,2455,3945,Z],[M,2464,2026,Q,2347,1913,2329,1895,L,2317,1895,Q,2319,1941,2305,2020,L,2265,2020,Q,2262,2024,2262,2048,2239,2047,2224,2047,2202,2047,2188,2056,L,2140,2056,Q,2122,2065,2119,2074,L,2069,2074,Q,2049,2073,2040,2074,2025,2078,2031,2102,2014,2107,2014,2120,L,2013,2156,Q,2015,2164,2002,2179,1987,2197,1986,2208,1985,2218,1986,2239,1985,2256,1966,2259,1817,2272,1797,2240,1795,2276,1778,2292,1759,2310,1759,2347,1742,2362,1737,2364,1734,2374,1731,2394,1701,2402,1658,2400,1621,2398,1607,2425,1592,2453,1557,2473,1533,2498,1500,2543,1471,2582,1471,2586,1471,2601,1492,2630,1513,2658,1513,2675,L,1513,2692,Q,1517,2700,1532,2724,1541,2736,1541,2762,1542,2785,1538,2792,1536,2794,1513,2818,L,1514,2847,Q,1515,2861,1497,2865,1445,2866,1418,2865,1369,2867,1382,2893,L,1315,2893,Q,1329,2921,1298,2925,1262,2925,1252,2926,L,1252,3058,Q,1252,3088,1237,3112,1225,3127,1225,3171,1226,3187,1271,3242,L,1290,3242,1290,3230,Q,1313,3231,1312,3199,1332,3207,1330,3180,1356,3177,1362,3174,1368,3172,1384,3147,1399,3127,1416,3127,1435,3126,1474,3099,1526,3062,1527,3052,L,1557,3052,Q,1568,3100,1697,3096,1858,3087,1937,3099,1939,3121,1939,3172,1941,3190,1951,3205,1960,3217,1960,3233,1960,3266,1951,3271,1912,3295,1900,3307,1829,3372,1825,3378,1778,3440,1761,3456,1734,3526,1688,3525,L,1688,3545,Q,1713,3547,1752,3568,1796,3591,1825,3596,L,1825,3665,Q,1823,3672,1808,3801,L,1825,3801,Q,1825,3825,1858,3827,1899,3828,1912,3848,L,1963,3848,Q,2001,3876,2137,3876,2233,3876,2324,3820,2351,3804,2423,3792,2463,3784,2463,3738,2463,3699,2445,3667,2427,3635,2426,3568,2426,3493,2440,3475,2468,3440,2494,3345,2513,3273,2541,3227,2564,3134,2580,3117,2632,3055,2645,3018,2661,2973,2650,2888,2638,2795,2688,2767,2759,2750,2793,2735,2796,2727,2796,2701,2752,2606,2741,2581,2722,2500,2710,2456,L,2710,2418,Q,2695,2397,2660,2388,2621,2381,2603,2374,2555,2363,2550,2358,2545,2355,2545,2305,2546,2265,2559,2251,2572,2238,2572,2211,Q,2572,2142,2464,2026,Z]],label:"Patuakhali District",shortLabel:"PT",labelPosition:[201.1,272.3],labelAlignment:[CEN,MID]},"BD.BA.PR":{outlines:[[M,610,829,Q,591,817,566,762,L,566,751,Q,560,758,552,761,543,773,526,810,501,840,474,845,463,847,394,847,313,848,306,819,L,259,819,Q,261,914,228,942,229,946,229,949,229,970,237,1012,237,1043,229,1096,229,1141,254,1193,L,254,1282,Q,210,1271,147,1292,63,1321,42,1323,42,1328,36,1342,L,36,1491,169,1491,Q,189,1491,219,1513,249,1535,273,1532,276,1540,290,1556,301,1571,301,1588,301,1606,291,1624,281,1643,281,1683,281,1721,291,1746,298,1765,306,1810,325,1828,329,1870,329,1876,355,1890,357,1894,357,1928,358,1962,329,2004,301,2048,301,2068,301,2125,327,2158,330,2175,329,2208,332,2236,355,2249,L,355,2330,337,2330,337,2308,Q,288,2262,273,2252,262,2244,217,2189,213,2169,189,2155,184,2152,148,2148,140,2147,128,2123,117,2106,91,2114,L,91,2086,64,2086,64,2148,Q,78,2155,95,2155,82,2201,116,2234,136,2253,179,2287,253,2379,311,2407,L,311,2432,255,2432,Q,253,2432,213,2460,154,2496,141,2529,123,2566,125,2631,126,2669,129,2744,129,2747,129,2749,L,129,2755,Q,151,2789,151,2817,151,2845,147,2849,134,2860,122,2892,117,2904,103,2932,98,2949,75,2967,46,3022,44,3043,35,3092,38,3130,L,38,3236,Q,106,3308,119,3378,123,3403,114,3478,115,3542,162,3540,L,162,3541,Q,174,3534,203,3529,233,3526,244,3517,297,3496,328,3475,359,3451,442,3352,482,3352,482,3372,L,531,3372,Q,527,3352,560,3323,559,3310,570,3298,581,3282,583,3274,590,3247,631,3165,627,3152,638,3139,652,3122,655,3112,655,3087,657,3077,676,3051,678,3047,680,3036,680,3012,680,3006,697,2990,700,2972,700,2929,684,2854,684,2836,688,2794,690,2772,L,681,2772,681,2748,655,2748,Q,624,2789,623,2802,L,613,2802,609,2801,Q,597,2779,597,2716,597,2667,603,2664,626,2645,619,2625,651,2620,652,2599,646,2587,660,2580,675,2572,675,2568,L,690,2568,690,2543,Q,669,2547,666,2520,669,2486,668,2472,654,2441,654,2397,L,632,2394,632,2354,651,2354,651,2374,666,2374,668,2402,Q,701,2400,693,2426,L,711,2426,711,2444,741,2444,Q,745,2442,753,2441,756,2426,780,2411,802,2398,800,2383,L,827,2383,827,2404,848,2404,Q,848,2422,850,2431,L,870,2431,871,2441,893,2441,Q,891,2419,907,2419,931,2418,934,2404,964,2388,992,2363,1032,2329,1038,2316,1050,2299,1050,2264,1050,2234,1004,2234,977,2231,944,2217,890,2223,874,2206,851,2180,820,2184,L,819,1919,Q,902,1905,909,1897,933,1894,948,1883,957,1875,957,1845,957,1812,954,1808,915,1771,912,1767,909,1741,892,1740,862,1737,869,1709,L,849,1709,849,1693,876,1693,Q,873,1670,890,1671,918,1671,927,1662,968,1624,979,1616,999,1605,1008,1599,1023,1589,1024,1571,1024,1513,1026,1501,L,1069,1470,Q,1073,1467,1126,1445,1144,1438,1144,1376,1155,1372,1171,1355,1179,1348,1202,1357,L,1202,1308,Q,1187,1308,1162,1267,L,1125,1267,Q,1121,1267,1116,1265,1108,1262,1098,1254,1018,1254,1013,1247,1001,1230,941,1229,891,1228,889,1198,885,1150,853,1153,822,1156,787,1124,771,1086,758,1071,744,1053,734,1019,L,640,1019,640,938,Q,642,923,651,917,660,912,660,900,660,895,640,865,Q,618,834,610,829,Z]],label:"Pirojpur District",shortLabel:"PR",labelPosition:[53.3,210.3],labelAlignment:[CEN,MID]}}}];exports["default"]={extension:geodefinitions,name:"barisal",type:"maps"}}})});