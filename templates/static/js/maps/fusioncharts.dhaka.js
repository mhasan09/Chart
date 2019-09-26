(function(factory){if(typeof module==="object"&&typeof module.exports!=="undefined"){module.exports=factory}else{factory(FusionCharts)}})(function(FusionCharts){(function(modules){var installedModules={};function __webpack_require__(moduleId){if(installedModules[moduleId]){return installedModules[moduleId].exports}var module=installedModules[moduleId]={i:moduleId,l:false,exports:{}};modules[moduleId].call(module.exports,module,module.exports,__webpack_require__);module.l=true;return module.exports}__webpack_require__.m=modules;__webpack_require__.c=installedModules;__webpack_require__.d=function(exports,name,getter){if(!__webpack_require__.o(exports,name)){Object.defineProperty(exports,name,{configurable:false,enumerable:true,get:getter})}};__webpack_require__.r=function(exports){Object.defineProperty(exports,"__esModule",{value:true})};__webpack_require__.n=function(module){var getter=module&&module.__esModule?function getDefault(){return module["default"]}:function getModuleExports(){return module};__webpack_require__.d(getter,"a",getter);return getter};__webpack_require__.o=function(object,property){return Object.prototype.hasOwnProperty.call(object,property)};__webpack_require__.p="";return __webpack_require__(__webpack_require__.s=302)})({302:function(module,exports,__webpack_require__){"use strict";var _fusioncharts=__webpack_require__(303);var _fusioncharts2=_interopRequireDefault(_fusioncharts);function _interopRequireDefault(obj){return obj&&obj.__esModule?obj:{"default":obj}}FusionCharts.addDep(_fusioncharts2["default"])},303:function(module,exports,__webpack_require__){"use strict";exports.__esModule=true;
/**!
 * @license FusionCharts JavaScript Library
 * Copyright FusionCharts Technologies LLP
 * License Information at <http://www.fusioncharts.com/license>
 *
 * @author FusionCharts Technologies LLP
 * @meta package_map_pack
 * @id fusionmaps.Dhaka.17.11-26-2015 08:30:21
 */var M="M",L="L",Z="Z",Q="Q",LFT="left",RGT="right",CEN="center",MID="middle",TOP="top",BTM="bottom",geodefinitions=[{name:"Dhaka",revision:17,standaloneInit:true,baseWidth:430,baseHeight:457,baseScaleFactor:10,entities:{"BD.DA.DH":{outlines:[[M,2526,2107,L,2514,2107,Q,2523,2122,2510,2124,2490,2126,2484,2140,2479,2151,2441,2150,2409,2151,2405,2148,2403,2146,2377,2111,L,2319,2111,2319,2126,2306,2126,2306,1960,Q,2238,1967,2188,1955,2136,1944,2114,1946,2115,1941,2134,1933,2134,1933,2144,1914,2149,1904,2165,1897,2178,1891,2179,1879,L,2189,1879,2189,1863,2174,1863,Q,2143,1820,2134,1796,L,2119,1796,Q,2120,1813,2102,1836,2084,1861,2082,1877,2076,1879,2071,1879,2063,1879,2052,1865,2040,1851,2044,1841,L,2027,1841,Q,2031,1862,1980,1864,1973,1896,1929,1895,1906,1895,1893,1883,1868,1860,1867,1860,1806,1835,1806,1832,1806,1832,1806,1831,1799,1834,1798,1844,L,1779,1844,1779,1835,Q,1774,1834,1758,1834,1757,1822,1751,1821,1741,1820,1730,1817,1721,1802,1715,1802,L,1695,1801,1695,1783,1685,1781,1685,1796,1678,1796,1678,1815,Q,1661,1811,1651,1830,1649,1834,1638,1837,1630,1840,1629,1854,L,1612,1854,1612,1845,1602,1845,1602,1835,Q,1589,1838,1581,1824,1572,1810,1560,1812,L,1560,1804,Q,1561,1801,1561,1796,L,1551,1796,1551,1883,Q,1536,1883,1529,1884,L,1528,1884,1528,1899,1548,1899,1548,1905,1689,1905,1689,1914,Q,1660,1905,1669,1935,1658,1935,1653,1935,1643,1935,1640,1940,1637,1948,1629,1952,1623,1955,1623,1961,L,1624,1971,Q,1645,1966,1658,1985,1672,1989,1692,2010,1713,2033,1714,2035,L,1714,2062,Q,1714,2065,1726,2082,1727,2083,1727,2104,1727,2116,1739,2120,1749,2123,1774,2137,1809,2155,1810,2159,1811,2165,1811,2179,1812,2184,1820,2198,1823,2208,1837,2232,1841,2249,1853,2262,1860,2269,1870,2292,1883,2311,1904,2312,1947,2315,1986,2326,1998,2326,2028,2339,2030,2339,2044,2347,2057,2354,2070,2350,L,2070,2363,2057,2361,2057,2372,Q,2045,2371,2041,2382,2038,2391,2020,2390,1988,2414,1985,2426,L,1985,2455,Q,1985,2469,1995,2496,1996,2509,2002,2517,2006,2521,2014,2530,L,2014,2573,2001,2573,Q,2003,2558,1981,2557,1955,2558,1949,2558,1925,2558,1920,2548,1916,2539,1902,2539,1889,2539,1883,2541,L,1865,2541,Q,1867,2535,1858,2526,L,1830,2526,1830,2540,Q,1823,2540,1813,2550,1806,2559,1796,2555,1782,2570,1766,2570,L,1713,2570,Q,1704,2570,1694,2578,1690,2581,1673,2581,1657,2581,1650,2580,L,1650,2666,Q,1643,2670,1641,2678,1640,2686,1634,2689,1613,2696,1615,2709,1622,2713,1635,2724,1650,2724,1665,2731,1676,2730,1687,2740,1702,2753,1712,2754,1742,2761,1773,2778,1806,2796,1818,2799,L,1819,2809,Q,1818,2813,1818,2821,1818,2822,1845,2902,1846,2906,1846,2924,1847,2942,1854,2946,1895,2973,1898,2974,1913,2981,1926,3001,1929,3005,1932,3008,L,1932,2977,Q,1943,2966,1944,2952,L,1945,2919,Q,1965,2906,1959,2894,L,1980,2894,Q,1982,2896,1983,2901,1986,2905,1995,2906,2005,2906,2010,2924,L,2017,2924,Q,2027,2921,2033,2918,2036,2903,2040,2900,2070,2875,2070,2867,2070,2782,2072,2771,2085,2749,2086,2734,2086,2718,2103,2696,2107,2670,2114,2659,2125,2657,2127,2651,L,2127,2630,2140,2630,Q,2140,2632,2144,2648,L,2186,2648,Q,2190,2648,2196,2660,2198,2663,2206,2669,L,2214,2669,Q,2215,2669,2215,2669,2236,2668,2258,2680,2269,2687,2295,2709,2309,2719,2340,2735,2364,2750,2364,2769,2365,2780,2356,2787,2349,2793,2350,2812,2351,2823,2341,2833,2336,2837,2336,2855,L,2336,2871,Q,2368,2871,2392,2881,2404,2881,2405,2877,2405,2867,2405,2855,2414,2826,2414,2821,2415,2816,2412,2812,L,2412,2782,Q,2420,2784,2416,2763,2428,2763,2429,2751,2429,2737,2431,2731,L,2450,2731,2483,2760,Q,2508,2780,2520,2791,2523,2752,2523,2730,2524,2690,2513,2679,2490,2648,2480,2640,2474,2634,2467,2619,2463,2608,2451,2603,L,2451,2593,2459,2593,Q,2461,2591,2461,2581,2503,2590,2553,2554,2589,2555,2605,2541,2614,2532,2630,2532,2641,2531,2640,2520,2641,2514,2616,2472,2608,2459,2601,2422,2591,2383,2566,2353,2545,2328,2545,2288,2545,2266,2551,2258,2558,2247,2561,2217,2559,2194,2559,2182,2559,2163,2575,2160,L,2575,2140,Q,2559,2146,2544,2131,Q,2530,2112,2526,2107,Z]],label:"Dhaka District",shortLabel:"DH",labelPosition:[223.5,239.5],labelAlignment:[CEN,MID]},"BD.DA.FR":{outlines:[[M,1170,2603,L,1170,2603,1158,2603,1158,2593,1151,2593,1151,2604,1141,2604,1141,2635,1066,2635,Q,1070,2656,1052,2651,1050,2653,1050,2670,1050,2685,1046,2687,L,1034,2687,1034,2680,1021,2680,Q,1026,2663,1007,2668,L,1007,2662,988,2662,987,2768,Q,987,2790,992,2795,998,2799,1015,2801,L,1053,2825,1052,2842,Q,1040,2839,1040,2846,1039,2851,1040,2861,L,980,2859,Q,979,2852,979,2836,L,967,2836,967,2823,954,2823,954,2836,943,2836,Q,945,2840,946,2846,L,946,2855,879,2856,Q,871,2856,872,2846,L,859,2846,Q,854,2826,855,2821,L,846,2821,846,2753,832,2753,832,2771,Q,815,2773,788,2809,762,2843,735,2842,L,705,2842,705,2812,Q,700,2813,689,2814,L,689,2803,694,2790,694,2770,661,2770,661,2784,654,2784,654,2803,626,2803,Q,624,2796,625,2784,L,589,2784,Q,589,2772,584,2769,L,551,2769,551,2785,536,2785,536,2797,Q,556,2793,554,2811,L,569,2811,Q,566,2823,593,2823,L,593,2835,581,2835,581,2842,559,2842,559,2860,535,2860,Q,530,2852,531,2848,L,517,2848,517,2827,505,2827,505,2818,Q,509,2815,509,2808,L,508,2797,459,2797,459,2784,436,2784,Q,439,2800,446,2819,445,2833,456,2845,464,2855,467,2872,470,2875,542,2947,L,542,2958,Q,511,2961,502,2961,495,2961,488,2970,480,2979,473,2978,L,470,3031,587,3031,Q,605,3031,622,3051,628,3058,658,3077,670,3087,678,3116,694,3143,691,3160,686,3185,698,3205,717,3238,719,3240,L,719,3248,Q,746,3282,745,3298,L,760,3298,760,3321,759,3323,751,3323,751,3309,741,3309,741,3301,724,3301,Q,728,3285,704,3287,L,704,3274,Q,696,3272,695,3280,692,3289,689,3290,676,3294,674,3308,L,661,3308,661,3317,Q,671,3317,679,3328,687,3342,693,3345,704,3349,704,3392,704,3424,698,3427,693,3429,693,3450,693,3452,693,3454,692,3481,702,3497,703,3507,712,3520,718,3529,715,3538,L,803,3538,803,3549,792,3549,792,3563,Q,779,3561,769,3564,756,3569,762,3579,750,3581,745,3581,L,745,3644,Q,756,3652,760,3662,761,3665,776,3665,779,3665,802,3654,810,3649,838,3650,850,3649,865,3665,874,3675,890,3686,L,890,3696,Q,952,3696,985,3659,1012,3643,1023,3631,1029,3624,1044,3614,1046,3612,1047,3589,1047,3571,1046,3568,1043,3563,1030,3556,1011,3545,992,3538,L,992,3518,1005,3518,1005,3504,Q,1007,3504,1085,3505,1128,3505,1140,3485,1142,3479,1177,3448,1216,3413,1234,3413,1245,3413,1253,3419,1261,3425,1276,3425,1281,3450,1311,3445,L,1311,3453,1332,3453,1332,3436,Q,1342,3436,1347,3438,L,1347,3422,1397,3422,1397,3495,1413,3495,1413,3476,Q,1420,3474,1435,3474,1449,3473,1443,3461,1447,3458,1483,3458,L,1483,3445,1508,3445,1508,3454,1520,3454,1520,3436,1506,3436,1506,3414,1491,3414,1491,3403,1483,3403,1483,3393,1503,3393,Q,1505,3399,1528,3396,L,1528,3413,1543,3413,1543,3439,1560,3439,Q,1559,3450,1562,3467,L,1601,3467,1601,3496,1616,3496,1616,3518,1625,3518,Q,1626,3513,1627,3500,1642,3504,1646,3482,1649,3458,1666,3461,1674,3446,1672,3431,L,1683,3431,1683,3445,1698,3445,Q,1694,3460,1721,3468,1736,3472,1764,3476,L,1764,3486,1773,3486,Q,1773,3470,1785,3466,1796,3462,1796,3450,L,1796,3403,Q,1805,3399,1805,3386,1803,3370,1805,3363,1817,3356,1817,3323,1817,3302,1816,3300,L,1801,3285,Q,1798,3270,1794,3268,1782,3261,1782,3259,1782,3253,1792,3250,1803,3246,1805,3238,1806,3227,1815,3224,1825,3221,1826,3213,L,1826,3124,Q,1864,3131,1873,3116,1867,3101,1868,3073,1869,3054,1852,3012,1835,2968,1794,2921,1783,2909,1710,2853,1702,2847,1680,2848,1649,2850,1629,2849,1611,2837,1603,2836,L,1537,2836,Q,1531,2835,1526,2826,1523,2817,1522,2816,1500,2796,1505,2767,L,1463,2767,Q,1427,2742,1406,2712,1395,2697,1373,2687,1345,2675,1340,2674,1282,2669,1251,2667,1232,2666,1222,2638,1192,2622,1203,2605,Q,1178,2605,1170,2603,Z]],label:"Faridpur District",shortLabel:"FR",labelPosition:[115.4,314.5],labelAlignment:[CEN,MID]},"BD.DA.GZ":{outlines:[[M,2533,1101,Q,2525,1102,2510,1102,L,2510,1129,2495,1129,2495,1182,Q,2487,1182,2484,1180,L,2484,1238,2471,1238,Q,2466,1223,2467,1219,L,2452,1219,Q,2452,1215,2454,1213,L,2454,1206,2436,1206,2436,1224,2413,1224,Q,2387,1223,2395,1206,2379,1199,2373,1193,2361,1182,2367,1163,L,2355,1163,2355,1182,2342,1182,Q,2340,1191,2340,1213,L,2326,1213,2326,1224,2277,1223,Q,2260,1223,2260,1224,2255,1234,2248,1241,L,2205,1241,Q,2224,1246,2245,1253,L,2245,1258,Q,2243,1258,2243,1268,2235,1265,2231,1266,L,2231,1272,Q,2217,1280,2205,1284,L,2168,1284,2168,1332,Q,2171,1338,2192,1359,L,2192,1373,Q,2164,1372,2128,1395,2117,1401,2091,1406,2072,1410,2065,1420,2065,1446,2053,1492,L,2053,1614,Q,2053,1628,2044,1638,2036,1647,2037,1654,L,1992,1654,Q,1966,1618,1966,1604,L,1958,1604,Q,1956,1611,1959,1634,1959,1655,1938,1657,L,1938,1724,1891,1757,Q,1873,1771,1846,1797,1808,1819,1806,1831,1806,1832,1806,1832,1806,1835,1867,1861,1868,1860,1893,1883,1906,1895,1930,1896,1973,1896,1980,1865,2031,1862,2027,1841,L,2045,1841,Q,2040,1851,2052,1866,2063,1879,2071,1879,2076,1879,2082,1877,2084,1861,2103,1836,2120,1813,2120,1797,L,2134,1797,Q,2143,1820,2175,1864,L,2189,1864,2189,1879,2179,1879,Q,2178,1891,2166,1897,2149,1904,2144,1914,2134,1933,2134,1933,2115,1941,2114,1946,2136,1944,2188,1956,2238,1967,2306,1961,L,2306,2126,2319,2126,2319,2111,2377,2111,Q,2403,2146,2406,2149,2409,2151,2441,2151,2479,2151,2484,2140,2490,2126,2510,2124,2523,2122,2514,2107,L,2527,2107,Q,2530,2112,2544,2131,2559,2146,2575,2141,L,2575,2143,Q,2580,2126,2581,2110,2580,2108,2591,2099,2601,2090,2599,2082,2599,2060,2607,2047,2614,2035,2614,2017,L,2630,2017,2630,2003,2639,2003,2639,2017,2658,2017,2658,2023,2679,2023,Q,2678,2014,2686,1998,2693,1984,2689,1971,L,2697,1971,2697,1993,2705,1993,Q,2705,2016,2746,2046,2755,2059,2764,2066,2764,2069,2766,2080,2769,2082,2774,2104,L,2797,2104,2805,2102,2829,2102,Q,2833,2089,2875,2047,2914,2008,2914,1992,2914,1979,2914,1978,2909,1975,2901,1967,L,2901,1937,Q,2908,1933,2934,1937,2954,1937,2944,1910,2965,1908,2965,1903,2962,1893,2962,1890,2962,1882,2964,1883,2968,1883,2973,1874,L,2973,1726,2952,1665,2927,1665,Q,2929,1659,2912,1657,L,2912,1649,Q,2916,1647,2929,1647,2925,1626,2944,1632,L,2942,1623,2945,1621,2955,1621,Q,2954,1626,2957,1639,2979,1648,2985,1670,L,3013,1670,Q,3051,1667,3073,1668,L,3073,1660,Q,3070,1660,3071,1656,L,3082,1656,3082,1643,Q,3068,1643,3058,1627,3044,1608,3036,1605,L,3036,1568,Q,3049,1561,3050,1537,3069,1524,3069,1505,3042,1452,3041,1450,3042,1427,3036,1419,3028,1409,3028,1389,3028,1363,3041,1357,3053,1352,3053,1336,3053,1328,3051,1325,3050,1323,3049,1322,3040,1319,3032,1309,3013,1294,3006,1288,2988,1275,2980,1268,2969,1260,2965,1249,L,2911,1249,Q,2908,1261,2875,1263,2874,1267,2874,1276,L,2786,1276,Q,2773,1263,2772,1263,2754,1265,2751,1262,2735,1243,2729,1236,2715,1222,2716,1207,2716,1181,2712,1168,2703,1172,2689,1165,2673,1156,2671,1156,2644,1153,2639,1145,2601,1151,2595,1101,Z]],label:"Gazipur District",shortLabel:"GZ",labelPosition:[244.4,162.6],labelAlignment:[CEN,MID]},"BD.DA.GG":{outlines:[[M,1311,3444,Q,1281,3450,1276,3425,1261,3425,1253,3419,1245,3413,1234,3413,1216,3413,1177,3448,1142,3479,1140,3485,1128,3505,1085,3504,1007,3504,1005,3504,L,1005,3517,991,3517,991,3538,Q,1011,3545,1030,3556,1043,3563,1045,3568,1047,3571,1047,3588,1046,3612,1043,3614,1029,3624,1023,3631,1012,3643,984,3659,952,3696,890,3696,L,890,3780,876,3780,876,3790,896,3790,896,3777,909,3777,Q,907,3765,928,3755,948,3745,965,3745,979,3745,992,3752,1004,3760,1028,3760,L,1028,3781,Q,1017,3800,995,3858,995,3858,991,3876,989,3881,972,3893,L,963,3937,Q,913,3937,890,3936,L,890,3945,Q,892,3951,931,3983,L,931,3983,Q,954,4008,979,4044,983,4049,1010,4076,1014,4082,1014,4099,1014,4116,1017,4121,1027,4133,1028,4138,1031,4143,1045,4148,1053,4153,1079,4169,1091,4176,1117,4184,1118,4185,1124,4189,1128,4192,1135,4196,1141,4200,1141,4214,1141,4221,1126,4261,1124,4284,1117,4285,1110,4288,1110,4301,1110,4312,1122,4317,1138,4326,1143,4334,L,1188,4355,1188,4371,Q,1183,4377,1168,4385,1158,4393,1160,4411,L,1151,4411,1151,4426,Q,1164,4447,1163,4457,1161,4476,1176,4489,1185,4497,1202,4516,1219,4532,1234,4532,1249,4532,1253,4527,1263,4514,1275,4506,1296,4502,1299,4501,1306,4497,1310,4491,1312,4487,1320,4487,1330,4487,1370,4516,1383,4526,1386,4533,1406,4516,1404,4459,L,1433,4459,Q,1437,4476,1486,4476,1527,4476,1534,4474,1551,4471,1565,4454,1576,4431,1581,4424,1584,4423,1586,4421,1588,4420,1589,4418,1596,4411,1596,4396,1586,4363,1586,4358,1587,4338,1645,4285,L,1662,4269,Q,1664,4247,1666,4245,1673,4238,1673,4190,L,1700,4190,Q,1703,4190,1717,4178,L,1758,4178,1758,4124,1835,4124,1835,4089,Q,1829,4079,1825,4075,L,1825,4039,Q,1830,4039,1860,4039,L,1860,4023,Q,1825,4030,1820,4014,1815,4e3,1784,4e3,L,1784,3955,1794,3955,1794,3947,1821,3948,1821,3932,Q,1809,3931,1804,3924,1790,3920,1784,3917,1765,3898,1758,3891,L,1739,3891,Q,1739,3900,1715,3922,L,1689,3947,Q,1677,3947,1658,3928,1637,3907,1636,3907,1624,3880,1578,3880,1555,3880,1552,3887,1544,3904,1541,3906,1512,3930,1516,3949,L,1498,3949,Q,1499,3934,1483,3937,1474,3939,1462,3925,1445,3906,1427,3907,L,1427,3891,Q,1441,3887,1442,3866,1454,3848,1456,3844,1451,3829,1466,3815,1479,3802,1474,3788,L,1584,3788,1584,3776,1572,3776,1572,3760,1559,3760,1559,3749,Q,1552,3749,1552,3743,L,1554,3732,Q,1570,3740,1573,3730,1578,3716,1589,3715,1613,3711,1615,3709,1629,3701,1634,3697,1635,3689,1635,3668,1633,3662,1639,3657,1646,3651,1646,3649,1644,3633,1644,3623,1646,3607,1660,3609,L,1660,3590,Q,1654,3590,1649,3570,1643,3562,1641,3558,1627,3530,1623,3528,L,1623,3517,1616,3517,1616,3496,1601,3496,1601,3466,1561,3466,Q,1559,3450,1559,3439,L,1543,3439,1543,3413,1528,3413,1528,3396,Q,1505,3399,1503,3393,L,1483,3393,1483,3403,1491,3403,1491,3414,1506,3414,1506,3436,1520,3436,1520,3454,1508,3454,1508,3444,1483,3444,1483,3457,Q,1447,3458,1442,3461,1449,3473,1435,3474,1420,3474,1413,3476,L,1413,3495,1396,3495,1396,3422,1346,3422,1346,3438,Q,1342,3436,1331,3436,L,1331,3453,1311,3453,Z]],label:"Gopalganj District",shortLabel:"GG",labelPosition:[121.8,396.3],labelAlignment:[CEN,MID]},"BD.DA.KS":{outlines:[[M,4015,495,Q,3986,504,3980,510,3961,529,3949,525,L,3944,544,3934,544,Q,3928,534,3926,532,3923,529,3918,531,3918,510,3912,504,3905,495,3881,496,3873,496,3858,484,3845,472,3823,476,L,3800,476,Q,3797,487,3791,488,3787,487,3780,499,3775,503,3763,504,3751,505,3746,510,3735,523,3702,522,3658,520,3644,520,L,3645,521,3641,521,Q,3642,520,3644,520,3639,517,3525,518,3472,518,3469,522,3462,529,3451,530,3439,531,3434,537,3426,543,3417,544,3414,543,3398,556,3376,567,3367,576,L,3367,600,Q,3356,611,3355,616,3355,625,3347,637,3345,646,3329,654,3318,658,3325,676,3296,697,3286,701,3253,725,3247,725,3232,722,3223,723,3225,712,3216,708,3207,702,3207,701,3206,678,3185,677,L,3185,661,3172,661,3172,690,3158,690,Q,3158,715,3151,732,L,3127,732,3127,723,3112,723,Q,3110,716,3110,703,L,3098,703,3098,690,3090,690,3090,713,Q,3075,715,3073,723,3072,742,3067,749,3063,753,3055,755,3048,757,3049,762,L,3052,778,3050,787,2977,787,Q,2981,776,2970,774,2956,769,2955,765,2949,751,2930,751,2930,740,2925,735,L,2846,735,2846,757,Q,2847,765,2837,772,2836,777,2836,793,2834,806,2819,799,L,2819,809,2839,809,Q,2858,835,2899,858,2919,868,2942,885,2960,900,2977,907,L,2977,927,Q,2977,976,2975,998,2972,1027,2970,1028,L,2951,1028,Q,2942,1029,2944,1037,L,2927,1037,2928,1059,Q,2928,1074,2925,1107,2925,1111,2931,1142,2929,1156,2949,1170,L,2964,1241,Q,2964,1245,2965,1249,2969,1260,2980,1268,2988,1275,3006,1288,3013,1294,3032,1309,3040,1319,3049,1322,3050,1323,3051,1325,L,3106,1325,3108,1333,3132,1333,Q,3128,1320,3141,1315,3155,1309,3153,1297,L,3170,1297,3170,1288,3183,1288,Q,3187,1309,3221,1360,3227,1370,3244,1399,3260,1424,3277,1425,3301,1425,3314,1442,L,3338,1477,Q,3358,1507,3359,1510,L,3417,1520,3417,1531,3437,1531,3437,1563,Q,3432,1568,3410,1568,L,3408,1578,3396,1576,3396,1590,Q,3402,1592,3410,1603,3416,1611,3428,1612,L,3428,1636,3382,1636,3382,1643,Q,3400,1644,3434,1642,3461,1642,3468,1649,3480,1655,3495,1668,3512,1683,3510,1694,L,3527,1694,3527,1686,3568,1686,3568,1675,3586,1675,Q,3579,1689,3588,1695,3599,1705,3600,1716,3600,1755,3607,1756,L,3613,1756,3614,1745,3625,1745,Q,3615,1761,3632,1765,3654,1769,3654,1784,3662,1777,3665,1776,3676,1776,3690,1768,3701,1762,3721,1762,3732,1762,3752,1763,3750,1742,3750,1741,L,3750,1717,Q,3751,1707,3780,1682,3792,1670,3793,1633,3792,1598,3777,1593,3745,1585,3725,1563,3707,1537,3693,1526,3665,1501,3665,1492,3665,1485,3693,1464,3708,1454,3727,1441,3738,1429,3752,1404,3757,1395,3784,1395,3809,1395,3814,1404,3819,1412,3838,1412,3858,1412,3869,1404,3871,1403,3894,1377,3897,1373,3900,1361,3902,1350,3908,1348,3917,1344,3933,1333,3947,1329,3980,1331,4011,1332,4025,1325,4041,1315,4094,1317,4093,1316,4092,1316,4083,1293,4119,1278,L,4119,1241,Q,4111,1243,4102,1235,4092,1226,4089,1223,L,4070,1214,Q,4062,1211,4062,1204,4062,1198,4068,1197,4074,1194,4077,1189,4079,1185,4079,1164,L,4126,1164,Q,4132,1170,4140,1185,4142,1189,4160,1189,4178,1189,4180,1183,4182,1174,4199,1169,4240,1155,4245,1155,L,4245,1122,Q,4222,1072,4199,1065,L,4199,1045,4267,1045,4267,1024,4198,910,4198,899,Q,4204,897,4221,882,4239,868,4239,864,4239,855,4220,821,4200,785,4187,775,L,4165,775,4165,791,Q,4146,790,4136,789,4119,788,4122,809,L,4115,809,Q,4102,809,4092,796,4081,783,4069,783,4069,778,4068,775,4098,777,4103,760,4141,751,4194,717,4196,715,4199,688,4200,681,4206,677,4215,671,4217,668,4218,666,4217,654,4217,643,4224,641,4232,637,4232,629,L,4232,616,4245,616,4245,603,4244,603,Q,4226,605,4214,591,4208,583,4189,564,4170,545,4171,536,L,4171,490,Q,4171,446,4174,437,L,4154,436,Q,4149,435,4148,441,4145,446,4139,448,4112,456,4094,453,4072,448,4071,448,4053,448,4038,464,Q,4024,486,4015,495,Z]],label:"Kishoreganj District",shortLabel:"KS",labelPosition:[354.3,111],labelAlignment:[CEN,MID]},"BD.DA.MD":{outlines:[[M,1826,3124,L,1826,3212,Q,1825,3221,1814,3224,1806,3227,1804,3238,1803,3246,1792,3250,1782,3253,1782,3259,1782,3261,1794,3268,1798,3270,1801,3284,L,1815,3300,Q,1817,3302,1816,3323,1817,3356,1804,3363,1803,3370,1805,3385,1805,3399,1796,3403,L,1796,3449,Q,1796,3462,1785,3466,1773,3470,1773,3486,L,1763,3486,1763,3476,Q,1736,3472,1721,3468,1694,3460,1698,3444,L,1683,3444,1683,3431,1672,3431,Q,1674,3446,1666,3461,1649,3458,1645,3482,1642,3504,1626,3500,1626,3513,1625,3517,L,1623,3517,1623,3528,Q,1627,3530,1641,3558,1643,3562,1649,3570,1654,3590,1660,3590,L,1660,3609,Q,1646,3607,1644,3623,1644,3633,1646,3649,1646,3651,1639,3657,1633,3662,1635,3668,1635,3689,1634,3697,1629,3701,1615,3709,1613,3711,1589,3715,1578,3716,1573,3730,1570,3740,1554,3732,L,1552,3743,Q,1552,3749,1559,3749,L,1559,3760,1572,3760,1572,3776,1584,3776,1584,3788,1474,3788,Q,1479,3802,1466,3815,1451,3829,1456,3844,1454,3848,1442,3866,1441,3887,1427,3891,L,1427,3907,Q,1445,3906,1462,3925,1474,3939,1483,3937,1499,3934,1498,3949,L,1516,3949,Q,1512,3930,1541,3906,1544,3904,1552,3887,1555,3880,1578,3880,1624,3880,1636,3907,1637,3907,1658,3928,1677,3947,1689,3947,L,1715,3922,Q,1739,3900,1739,3891,L,1758,3891,Q,1765,3898,1784,3917,1790,3920,1804,3924,1809,3931,1821,3932,L,1821,3948,1794,3947,1794,3955,1784,3955,1784,4e3,Q,1815,4e3,1820,4014,1825,4030,1860,4023,L,1860,4039,Q,1874,4039,1893,4039,1928,4040,1933,4033,1954,4025,1964,4014,1976,3993,1982,3984,L,1994,3984,Q,1991,3997,2013,3997,L,2013,4082,Q,1997,4129,1997,4183,1997,4199,2019,4201,2031,4202,2050,4218,2053,4218,2063,4227,2072,4237,2080,4237,2084,4237,2111,4248,L,2132,4248,2132,4229,Q,2147,4229,2157,4230,L,2181,4230,2181,4218,2226,4218,Q,2233,4221,2247,4235,2253,4242,2263,4245,2263,4227,2256,4218,2246,4210,2240,4203,2221,4176,2211,4164,2173,4117,2145,4104,L,2145,4091,Q,2158,4089,2168,4070,2181,4045,2192,4036,2231,4003,2231,3977,2231,3972,2204,3947,2177,3923,2162,3916,2150,3909,2140,3883,2126,3853,2123,3844,2112,3808,2075,3780,2010,3732,2008,3730,L,2008,3710,Q,2011,3690,2011,3680,2011,3667,2007,3663,1997,3653,1995,3649,1992,3645,1992,3612,1992,3590,1993,3586,1995,3578,2011,3565,2048,3545,2056,3529,L,2101,3492,Q,2111,3479,2117,3470,2129,3451,2132,3448,L,2184,3354,Q,2188,3335,2195,3328,2210,3312,2210,3308,2210,3298,2220,3284,2228,3272,2229,3265,L,2218,3265,Q,2210,3257,2206,3259,2191,3263,2174,3256,2154,3247,2146,3247,2134,3247,2119,3237,L,2093,3233,1988,3178,Q,1964,3159,1940,3145,1938,3144,1887,3130,1878,3127,1873,3115,Q,1864,3131,1826,3124,Z]],label:"Madaripur District",shortLabel:"MD",labelPosition:[180.2,370.3],labelAlignment:[CEN,MID]},"BD.DA.MK":{outlines:[[M,1690,1906,L,1548,1906,1548,1899,1529,1899,1529,1884,1529,1884,Q,1520,1873,1516,1868,1515,1854,1513,1848,1508,1831,1503,1829,1501,1828,1481,1828,1456,1828,1456,1830,1450,1843,1433,1857,1404,1881,1400,1898,1394,1899,1365,1900,1344,1899,1338,1907,L,1315,1953,1305,1953,Q,1307,1946,1292,1932,1280,1920,1287,1904,L,1276,1904,Q,1278,1920,1266,1941,1265,1948,1253,1957,1243,1964,1250,1978,L,1209,1978,Q,1214,1965,1202,1963,1183,1958,1182,1957,1160,1931,1154,1931,1147,1931,1146,1954,L,1138,1954,1138,1965,1131,1965,1131,1950,Q,1121,1950,1118,1949,1125,1937,1111,1922,1095,1903,1096,1893,1096,1848,1079,1835,L,1079,1823,Q,1043,1821,1033,1826,1018,1832,990,1840,967,1846,952,1856,L,901,1856,Q,881,1844,875,1844,855,1902,876,1944,891,1973,938,2018,1002,2078,1006,2081,1053,2120,1051,2146,L,1051,2165,Q,1057,2177,1075,2205,1089,2234,1083,2264,1074,2300,1094,2326,1105,2340,1133,2369,1152,2400,1162,2410,1178,2427,1207,2443,1233,2465,1256,2471,1267,2474,1280,2489,L,1319,2492,Q,1338,2492,1345,2492,1348,2493,1366,2512,1374,2518,1382,2530,1390,2538,1406,2539,L,1406,2549,1324,2549,1324,2561,Q,1338,2566,1376,2612,L,1401,2612,1401,2600,Q,1407,2599,1423,2597,L,1431,2597,Q,1431,2613,1438,2621,L,1445,2647,Q,1456,2681,1484,2681,1520,2681,1549,2698,L,1564,2699,Q,1567,2698,1579,2708,L,1612,2708,Q,1613,2708,1615,2709,1613,2696,1634,2689,1640,2686,1642,2678,1643,2670,1650,2666,L,1650,2580,Q,1657,2581,1673,2581,1690,2581,1694,2579,1704,2570,1713,2571,L,1766,2571,Q,1782,2570,1796,2556,1806,2559,1814,2551,1823,2540,1830,2540,L,1830,2526,1859,2526,Q,1867,2535,1865,2541,L,1884,2541,Q,1889,2539,1902,2539,1916,2539,1921,2548,1925,2558,1949,2558,1955,2558,1981,2557,2003,2558,2001,2573,L,2014,2573,2014,2530,Q,2006,2521,2003,2517,1996,2509,1996,2497,1985,2469,1986,2456,L,1986,2426,Q,1988,2414,2020,2390,2038,2391,2041,2382,2045,2371,2058,2373,L,2058,2361,2070,2363,2070,2350,Q,2057,2354,2045,2347,2030,2339,2028,2340,1998,2326,1987,2326,1947,2315,1904,2313,1883,2311,1871,2292,1860,2269,1853,2262,1841,2249,1837,2232,1823,2208,1821,2198,1812,2184,1811,2179,1811,2165,1810,2160,1809,2155,1774,2138,1749,2123,1739,2120,1727,2116,1727,2104,1727,2083,1726,2082,1714,2065,1714,2062,L,1714,2036,Q,1713,2033,1693,2010,1672,1989,1658,1985,1645,1966,1624,1971,L,1623,1962,Q,1623,1955,1629,1952,1637,1948,1641,1940,1643,1935,1653,1935,1658,1935,1669,1935,1660,1905,1690,1914,Z]],label:"Manikganj District",shortLabel:"MK",labelPosition:[146.8,226.6],labelAlignment:[CEN,MID]},"BD.DA.MU":{outlines:[[M,2482,3231,L,2448,3231,Q,2429,3227,2417,3215,L,2379,3215,2379,3227,Q,2394,3222,2404,3233,2409,3240,2420,3253,2431,3261,2468,3295,2475,3300,2513,3334,2550,3366,2558,3366,L,2570,3364,2569,3331,Q,2569,3301,2580,3293,L,2580,3255,Q,2565,3258,2555,3252,2543,3244,2540,3243,2504,3250,2494,3241,Q,2483,3230,2482,3231,Z],[M,2785,2961,L,2789,3011,Q,2789,3020,2792,3035,2800,3041,2816,3033,2829,3033,2865,3016,2873,3013,2888,3002,2898,2995,2912,2996,2928,2997,2960,2979,2991,2961,3014,2967,L,3014,2952,3006,2952,Q,2966,2888,2962,2866,2958,2847,2936,2823,2915,2799,2914,2786,L,2811,2786,Q,2798,2809,2762,2833,2734,2852,2734,2878,Q,2734,2892,2785,2961,Z],[M,2635,2856,Q,2601,2863,2572,2848,2542,2827,2526,2817,2501,2786,2487,2786,2464,2786,2446,2756,L,2438,2756,Q,2434,2758,2434,2767,2434,2774,2426,2771,L,2426,2793,Q,2421,2791,2420,2795,2418,2800,2412,2801,L,2412,2812,Q,2415,2816,2415,2821,2414,2826,2405,2856,2405,2867,2405,2877,2404,2881,2392,2881,2368,2871,2337,2872,L,2336,2855,Q,2336,2837,2341,2833,2351,2823,2351,2812,2349,2793,2356,2787,2365,2780,2364,2769,2364,2750,2340,2735,2309,2719,2296,2709,2269,2687,2258,2681,2236,2668,2216,2669,2215,2669,2214,2669,L,2206,2669,Q,2198,2663,2196,2660,2190,2648,2186,2648,L,2144,2648,Q,2140,2632,2140,2631,L,2127,2631,2127,2651,Q,2125,2657,2114,2659,2107,2670,2104,2696,2086,2718,2086,2734,2085,2749,2072,2771,2070,2782,2070,2868,2070,2875,2041,2900,2036,2903,2033,2918,2027,2921,2017,2924,L,2010,2924,Q,2005,2906,1995,2906,1986,2905,1983,2901,1982,2896,1980,2894,L,1959,2894,Q,1965,2906,1946,2919,L,1945,2952,Q,1943,2966,1932,2977,L,1932,3008,Q,1946,3027,1955,3035,1985,3060,2037,3097,2070,3121,2126,3149,2128,3150,2180,3153,2190,3153,2232,3171,2244,3173,2291,3168,2326,3165,2343,3177,2349,3181,2366,3180,2379,3182,2386,3190,2396,3192,2416,3192,2422,3194,2433,3207,L,2594,3207,Q,2593,3219,2598,3228,2601,3232,2634,3254,2637,3258,2654,3292,L,2672,3292,2671,3261,Q,2671,3252,2725,3144,2754,3095,2757,3089,2758,3086,2758,3037,2758,2965,2736,2943,2708,2922,2698,2913,2681,2896,2684,2870,Q,2674,2870,2635,2856,Z]],label:"Munshiganj District",shortLabel:"MU",labelPosition:[247.3,299.8],labelAlignment:[CEN,MID]},"BD.DA.NY":{outlines:[[M,2811,2102,L,2805,2102,2797,2104,2774,2104,Q,2769,2082,2766,2080,2764,2069,2764,2066,2755,2059,2746,2046,2705,2016,2705,1993,L,2697,1993,2697,1971,2689,1971,Q,2693,1984,2686,1998,2678,2014,2679,2023,L,2658,2023,2658,2017,2639,2017,2639,2003,2630,2003,2630,2017,2614,2017,Q,2614,2035,2607,2047,2599,2060,2599,2082,2601,2090,2591,2099,2580,2108,2581,2110,2580,2126,2575,2143,L,2575,2160,Q,2559,2163,2559,2182,2559,2194,2561,2218,2558,2247,2551,2258,2545,2266,2545,2288,2545,2328,2566,2353,2591,2383,2601,2422,2608,2459,2616,2472,2641,2514,2641,2520,2641,2531,2630,2532,2614,2532,2605,2541,2589,2555,2553,2555,2503,2590,2461,2581,2461,2591,2460,2593,L,2451,2593,2451,2603,Q,2463,2608,2468,2620,2474,2634,2481,2640,2490,2648,2513,2679,2524,2690,2523,2730,2523,2752,2521,2792,2521,2792,2521,2793,2533,2799,2556,2807,2556,2816,2557,2820,L,2589,2820,Q,2610,2803,2609,2792,L,2626,2792,Q,2609,2844,2680,2844,2701,2844,2704,2839,2715,2816,2725,2805,2734,2794,2768,2758,2775,2750,2796,2745,2819,2740,2826,2736,2839,2724,2886,2713,L,2886,2592,2899,2591,Q,2902,2570,2908,2567,2910,2565,2931,2565,2947,2565,2959,2571,2970,2577,2994,2577,L,2994,2587,3004,2587,Q,3008,2576,3008,2552,3007,2529,3014,2519,3033,2514,3037,2498,3053,2472,3054,2472,L,3065,2472,3065,2448,Q,3064,2437,3085,2428,L,3114,2380,Q,3113,2371,3113,2355,3098,2361,3089,2350,3079,2337,3075,2337,3072,2336,3056,2320,3047,2311,3032,2315,2992,2321,2929,2299,L,2929,2287,2949,2287,Q,2945,2273,2953,2273,2956,2272,2966,2273,2968,2243,2988,2249,L,2988,2239,2972,2239,Q,2975,2229,2968,2221,2961,2211,2961,2205,L,2936,2205,Q,2933,2219,2924,2220,2912,2218,2906,2220,2896,2222,2893,2236,2890,2245,2878,2239,L,2876,2253,2867,2253,Q,2867,2255,2864,2261,L,2856,2261,Q,2854,2237,2848,2232,L,2848,2208,2869,2208,2869,2182,2885,2182,Q,2885,2178,2888,2166,2900,2168,2906,2158,L,2906,2134,2893,2134,2893,2150,2869,2150,Q,2860,2136,2854,2128,2844,2113,2824,2120,L,2824,2115,Q,2814,2111,2811,2111,Z]],label:"Narayanganj District",shortLabel:"NY",labelPosition:[278.2,240.7],labelAlignment:[CEN,MID]},"BD.DA.NS":{outlines:[[M,3437,1531,L,3417,1531,3417,1520,3359,1510,Q,3358,1507,3338,1477,L,3314,1442,Q,3301,1425,3277,1425,3260,1424,3244,1399,3227,1370,3221,1360,3187,1309,3183,1288,L,3170,1288,3170,1297,3153,1297,Q,3155,1309,3141,1315,3128,1320,3132,1333,L,3108,1333,3106,1325,3051,1325,Q,3053,1328,3053,1336,3053,1352,3041,1357,3028,1363,3028,1389,3028,1409,3036,1419,3042,1427,3041,1450,3042,1452,3069,1505,3069,1524,3050,1537,3049,1561,3036,1568,L,3036,1605,Q,3044,1608,3058,1627,3068,1643,3082,1643,L,3082,1656,3071,1656,Q,3070,1660,3073,1660,L,3073,1668,Q,3051,1667,3013,1670,L,2985,1670,Q,2979,1648,2957,1639,2954,1626,2955,1621,L,2945,1621,2942,1623,2944,1632,Q,2925,1626,2929,1647,2916,1647,2912,1649,L,2912,1657,Q,2929,1659,2927,1665,L,2952,1665,2973,1726,2973,1874,Q,2968,1883,2964,1883,2962,1882,2962,1890,2962,1893,2965,1903,2965,1908,2944,1910,2954,1937,2934,1937,2908,1933,2901,1937,L,2901,1967,Q,2909,1975,2914,1978,2914,1979,2914,1992,2914,2008,2875,2047,2833,2089,2829,2102,L,2811,2102,2811,2111,Q,2814,2111,2824,2115,L,2824,2120,Q,2844,2113,2854,2128,2860,2136,2869,2150,L,2893,2150,2893,2134,2906,2134,2906,2158,Q,2900,2168,2888,2166,2885,2178,2885,2182,L,2869,2182,2869,2208,2848,2208,2848,2232,Q,2854,2237,2856,2261,L,2864,2261,Q,2867,2255,2867,2253,L,2876,2253,2878,2239,Q,2890,2245,2893,2236,2896,2222,2906,2220,2912,2218,2924,2220,2933,2219,2936,2205,L,2961,2205,Q,2961,2211,2968,2221,2975,2229,2972,2239,L,2988,2239,2988,2249,Q,2968,2243,2966,2273,2956,2272,2953,2273,2945,2273,2949,2287,L,2929,2287,2929,2299,Q,2992,2321,3032,2315,3047,2311,3056,2320,3072,2336,3075,2337,3079,2337,3089,2350,3098,2361,3113,2355,3113,2371,3114,2380,L,3131,2352,Q,3157,2327,3163,2314,3161,2271,3159,2252,3157,2217,3169,2209,3173,2205,3187,2189,3196,2177,3202,2177,3215,2176,3223,2169,3229,2163,3239,2163,3249,2163,3250,2165,3252,2167,3257,2178,3263,2189,3288,2187,3290,2188,3297,2197,3301,2202,3309,2203,3321,2203,3343,2207,3358,2207,3365,2201,3373,2193,3390,2192,3433,2188,3443,2180,3447,2177,3470,2177,3487,2176,3491,2162,3494,2139,3507,2125,3513,2118,3514,2102,3516,2087,3524,2081,3532,2074,3536,2062,3541,2047,3546,2040,3557,2033,3557,2016,3557,2003,3562,1997,3585,1969,3578,1952,L,3638,1952,3638,1942,3610,1914,Q,3591,1891,3591,1875,3613,1852,3621,1837,3640,1798,3646,1793,3650,1788,3654,1784,3654,1769,3632,1765,3615,1761,3625,1745,L,3614,1745,3613,1756,3607,1756,Q,3600,1755,3600,1716,3599,1705,3588,1695,3579,1689,3586,1675,L,3568,1675,3568,1686,3527,1686,3527,1694,3510,1694,Q,3512,1683,3495,1668,3480,1655,3468,1649,3461,1642,3434,1642,3400,1644,3382,1643,L,3382,1636,3428,1636,3428,1612,Q,3416,1611,3410,1603,3402,1592,3396,1590,L,3396,1576,3408,1578,3410,1568,Q,3432,1568,3437,1563,Z]],label:"Narsingdi District",shortLabel:"NS",labelPosition:[323.2,183.4],labelAlignment:[CEN,MID]},"BD.DA.RB":{outlines:[[M,937,2365,Q,963,2362,975,2382,984,2397,1034,2438,1046,2447,1069,2462,1087,2477,1088,2494,1101,2497,1100,2482,1097,2462,1097,2455,L,1086,2455,Q,1091,2408,1082,2395,1056,2367,1042,2346,1029,2325,981,2325,932,2318,903,2318,789,2325,756,2325,L,756,2365,Z],[M,675,2273,Q,680,2282,653,2293,637,2298,623,2311,599,2330,593,2333,587,2336,578,2344,577,2345,560,2345,536,2345,525,2322,517,2295,512,2287,L,445,2287,445,2305,456,2305,456,2320,465,2320,Q,467,2324,464,2338,464,2352,476,2348,L,476,2384,466,2384,466,2368,Q,454,2371,423,2350,393,2328,388,2325,350,2307,350,2305,338,2276,339,2271,350,2223,327,2191,296,2160,284,2138,L,194,2138,Q,159,2138,155,2137,150,2125,129,2125,118,2125,114,2128,111,2131,107,2133,L,107,2262,Q,130,2295,126,2326,126,2329,126,2331,L,126,2369,Q,129,2381,97,2386,80,2399,64,2412,43,2426,43,2437,43,2443,49,2460,50,2466,52,2470,59,2484,66,2489,70,2491,118,2539,199,2620,205,2624,L,205,2624,Q,209,2624,222,2611,228,2611,247,2601,292,2604,288,2580,L,303,2580,Q,314,2605,377,2664,431,2713,432,2761,433,2772,435,2784,L,459,2784,459,2797,507,2797,509,2808,Q,509,2815,505,2817,L,505,2827,517,2827,517,2848,531,2848,Q,530,2852,535,2860,L,559,2860,559,2842,581,2842,581,2835,593,2835,593,2823,Q,566,2823,569,2810,L,553,2810,Q,556,2793,536,2797,L,536,2785,550,2785,550,2769,584,2769,Q,589,2772,589,2784,L,624,2784,Q,624,2796,625,2802,L,654,2802,654,2784,661,2784,661,2770,693,2770,693,2790,689,2802,689,2813,Q,700,2813,705,2812,L,705,2842,735,2842,Q,762,2843,787,2808,815,2773,832,2771,L,832,2752,846,2752,846,2821,854,2821,Q,854,2826,858,2846,L,872,2846,Q,871,2856,879,2855,L,946,2854,946,2846,Q,945,2840,943,2836,L,954,2836,954,2823,966,2823,966,2836,978,2836,Q,979,2852,980,2858,L,1039,2861,Q,1039,2851,1039,2846,1040,2839,1051,2842,L,1053,2825,1015,2801,Q,998,2799,992,2794,987,2790,987,2768,L,988,2662,1007,2662,1007,2668,Q,1026,2663,1021,2679,L,1034,2679,1034,2686,1046,2686,Q,1050,2685,1050,2670,1050,2653,1051,2651,1070,2656,1066,2635,L,1141,2635,1141,2604,1150,2604,1150,2593,1157,2593,1157,2603,1169,2603,1169,2590,1182,2590,1182,2581,Q,1177,2578,1169,2578,1165,2566,1127,2542,1097,2513,1086,2511,1060,2506,1045,2487,1039,2480,999,2455,968,2430,953,2419,926,2398,906,2397,L,761,2397,Q,765,2379,748,2365,727,2352,720,2345,715,2308,711,2302,702,2295,697,2291,689,2284,693,2273,Z]],label:"Rajbari District",shortLabel:"RB",labelPosition:[61.2,253.6],labelAlignment:[CEN,MID]},"BD.DA.SA":{outlines:[[M,2689,3430,L,2533,3430,Q,2503,3431,2489,3409,2463,3367,2461,3364,2437,3338,2425,3325,2403,3302,2377,3291,2356,3265,2332,3266,2290,3267,2271,3254,L,2238,3254,2238,3265,2229,3265,Q,2228,3272,2220,3285,2210,3298,2210,3308,2210,3312,2195,3329,2188,3335,2184,3355,L,2132,3448,Q,2129,3451,2118,3471,2111,3479,2102,3492,L,2056,3529,Q,2048,3545,2011,3566,1995,3578,1994,3587,1992,3590,1992,3612,1992,3645,1995,3650,1997,3653,2007,3663,2011,3667,2011,3680,2011,3690,2008,3710,L,2008,3730,Q,2010,3732,2075,3780,2112,3808,2123,3844,2126,3853,2140,3884,2150,3909,2163,3916,2177,3923,2204,3948,2231,3972,2231,3977,2231,4003,2192,4036,2181,4045,2168,4070,2158,4089,2145,4091,L,2145,4104,Q,2173,4117,2211,4164,2221,4176,2241,4203,2246,4210,2256,4218,2263,4227,2263,4245,2269,4248,2265,4263,L,2276,4263,2276,4254,2284,4254,2284,4233,Q,2283,4231,2282,4231,2280,4223,2293,4209,2299,4192,2301,4189,2312,4162,2336,4162,2360,4161,2390,4145,2401,4142,2437,4134,L,2437,4123,Q,2442,4121,2461,4113,2485,4113,2488,4112,2495,4110,2499,4091,2505,4084,2505,4067,2505,4053,2516,4046,2522,4043,2523,4035,2523,4022,2524,4020,2525,4016,2529,4010,2532,4004,2534,4001,2536,3998,2540,3981,2558,3981,2560,3973,L,2589,3973,2589,3979,Q,2557,3974,2549,3996,2553,4025,2533,4022,L,2533,4055,Q,2532,4085,2533,4088,2534,4094,2548,4108,2550,4119,2572,4119,2586,4119,2628,4116,2642,4115,2671,4149,2701,4183,2717,4182,2727,4178,2736,4162,2744,4146,2744,4135,2744,4123,2738,4118,2731,4111,2731,4097,2731,4073,2723,4061,2709,4020,2698,4006,2690,3989,2662,3988,2657,3988,2654,3982,2651,3977,2647,3977,2630,3977,2630,3970,L,2617,3970,2617,3962,Q,2619,3962,2647,3953,2662,3949,2678,3951,L,2678,3925,Q,2647,3881,2647,3878,2647,3861,2683,3835,2721,3810,2723,3808,2746,3779,2748,3769,2750,3752,2761,3745,2772,3738,2772,3726,2772,3722,2760,3693,2747,3660,2738,3650,2732,3643,2718,3568,2716,3537,2709,3528,2708,3527,2697,3489,Q,2689,3457,2689,3430,Z]],label:"Shariatpur District",shortLabel:"SA",labelPosition:[238.2,375.8],labelAlignment:[CEN,MID]},"BD.DA.TA":{outlines:[[M,1741,68,L,1714,68,1714,57,1690,57,1690,47,1679,47,1679,63,Q,1649,66,1648,67,1629,72,1620,78,1599,106,1580,122,1575,127,1573,138,1572,149,1565,153,1552,161,1542,181,1528,196,1528,207,1527,211,1518,215,1513,219,1516,230,L,1506,230,Q,1472,180,1471,161,1445,147,1431,132,1427,128,1413,126,1403,125,1403,113,L,1391,113,Q,1392,164,1381,169,1340,185,1340,199,1326,201,1319,201,L,1319,210,1306,210,1306,195,1300,195,1300,178,1280,178,Q,1277,204,1273,207,1271,209,1270,226,1271,246,1277,253,1281,258,1294,274,1304,290,1339,304,L,1339,348,1329,348,1329,334,Q,1327,334,1325,332,L,1295,332,Q,1299,343,1267,375,1256,386,1231,413,1218,424,1214,437,1211,452,1206,457,1207,474,1197,478,1179,484,1170,485,1170,506,1161,531,1153,556,1152,582,L,1105,582,Q,1103,579,1103,575,L,1065,575,Q,1061,587,1051,593,1052,597,1054,606,1054,613,1034,613,1012,614,1009,616,1003,621,986,626,975,628,979,641,L,960,641,960,662,Q,970,669,984,693,989,697,991,711,1001,720,1001,729,999,789,996,801,993,814,973,829,953,845,935,863,918,881,918,885,918,892,944,910,964,912,964,912,973,923,976,930,980,937,1010,960,1014,966,1023,979,1027,984,1027,997,1027,1010,1008,1024,988,1039,987,1048,L,1005,1065,Q,1015,1076,1018,1089,1030,1102,1053,1135,1058,1141,1071,1154,1083,1167,1082,1184,L,1082,1336,Q,1082,1350,1072,1366,1066,1376,1066,1384,1066,1387,1066,1389,L,1066,1407,Q,1071,1415,1089,1463,1089,1472,1066,1495,1066,1506,1082,1512,1099,1520,1101,1525,1105,1533,1140,1561,L,1137,1582,Q,1137,1586,1152,1609,1154,1622,1153,1655,1153,1734,1145,1743,1126,1763,1129,1774,1134,1790,1104,1800,1093,1822,1082,1823,1081,1823,1079,1823,L,1079,1835,Q,1096,1848,1095,1893,1095,1903,1111,1921,1125,1937,1118,1949,1121,1950,1131,1950,L,1131,1965,1138,1965,1138,1954,1146,1954,Q,1147,1931,1154,1931,1160,1931,1182,1957,1183,1958,1202,1962,1214,1965,1208,1978,L,1250,1978,Q,1243,1964,1253,1957,1265,1948,1265,1941,1278,1920,1276,1903,L,1287,1903,Q,1280,1920,1292,1932,1307,1946,1305,1953,L,1315,1953,1337,1906,Q,1344,1899,1365,1899,1394,1899,1399,1898,1404,1881,1433,1857,1450,1843,1455,1830,1456,1828,1481,1828,1501,1828,1503,1829,1508,1831,1513,1847,1515,1854,1515,1868,1520,1873,1529,1884,1536,1883,1551,1883,L,1551,1796,1561,1796,Q,1561,1801,1560,1804,L,1560,1812,Q,1572,1810,1581,1824,1589,1838,1602,1835,L,1602,1845,1612,1845,1612,1854,1629,1854,Q,1630,1840,1638,1837,1649,1834,1651,1830,1661,1811,1678,1815,L,1678,1796,1685,1796,1685,1781,1695,1783,1695,1801,1715,1802,Q,1721,1802,1730,1817,1741,1820,1751,1821,1757,1822,1758,1834,1774,1834,1779,1835,L,1779,1844,1798,1844,Q,1799,1834,1806,1831,1808,1819,1846,1796,1873,1771,1891,1757,L,1937,1723,1937,1657,Q,1959,1655,1959,1634,1956,1611,1958,1604,L,1966,1604,Q,1966,1618,1992,1654,L,2037,1654,Q,2036,1647,2044,1638,2053,1628,2053,1614,L,2053,1492,Q,2065,1446,2065,1420,2072,1410,2091,1406,2117,1401,2128,1395,2164,1372,2192,1372,L,2192,1359,Q,2171,1338,2168,1332,L,2168,1284,2205,1284,Q,2217,1280,2231,1272,L,2231,1265,Q,2235,1265,2243,1267,2243,1258,2245,1257,L,2245,1253,Q,2224,1246,2205,1240,2188,1236,2173,1233,2157,1230,2117,1195,2097,1178,2081,1138,2054,1080,2053,1074,2054,1067,2065,1067,2055,1047,2068,1042,2086,1036,2086,1021,2090,970,2090,953,2055,911,2042,891,2021,863,2018,856,2014,850,2014,819,2014,790,2016,770,2018,770,2038,773,L,2048,773,2048,767,Q,2057,765,2078,769,L,2078,759,Q,2054,751,2023,732,1981,706,1965,698,1936,681,1924,668,1903,647,1891,633,1872,609,1866,588,1865,581,1852,566,1842,556,1846,543,1835,541,1835,533,L,1837,514,Q,1838,512,1849,500,1846,487,1852,478,1861,471,1864,465,1906,421,1906,408,1873,356,1864,340,1825,306,1825,279,L,1825,170,Q,1830,154,1829,147,1828,134,1803,138,1785,141,1745,137,L,1745,134,Q,1748,126,1748,123,1748,120,1741,113,Z]],label:"Tangail District",shortLabel:"TA",labelPosition:[153.8,101.2],labelAlignment:[CEN,MID]}}}];exports["default"]={extension:geodefinitions,name:"dhaka",type:"maps"}}})});