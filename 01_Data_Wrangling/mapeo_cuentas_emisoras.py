# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:34:45 2019

@author: arman
"""

import pandas as pd
import numpy as np

import os
os.getcwd()

os.chdir('C:\\Users\\arman\\Desktop\\Proyectos Manuel Sarmiento\\02 Algoritmos\\Python')



#df = pd.read_csv('AA1CK - 3015.csv')
#
#
#
#cuenta_catalogo_sql = {
#    1:1,
#    3:3,
#    4:4,
#    5:5,
#    8:8,
#    11:11,
#    16:16,
#    17:17,
#    18:18,
#    19:19,
#    20:20,
#    21:21,
#    24:24,
#    25:25,
#    26:26,
#    27:27,
#    28:28,
#    29:29,
#    32:32,
#    33:33,
#    34:34,
#    36:36,
#    38:38,
#    39:39,
#    40:40,
#    41:41,
#    42:42,
#    43:43,
#    44:44,
#    46:46,
#    47:47,
#    48:48,
#    49:49,
#    60:60,
#    62:62,
#    66:66,
#    67:67,
#    69:69,
#    79:79,
#    80:80,
#    81:81,
#    83:83,
#    84:84,
#    85:85,
#    86:86,
#    87:87,
#    88:88,
#    89:89,
#    93:93,
#    94:94,
#    95:95,
#    96:96,
#    97:97,
#    111:111,
#    112:112,
#    113:113,
#    114:114,
#    115:115,
#    116:116,
#    117:117,
#    121:121,
#    122:122,
#    127:127,
#    130:130,
#    131:131,
#    135:135,
#    136:136,
#    137:137,
#    139:139,
#    144:144,
#    148:148,
#    155:155,
#    156:156,
#    159:159,
#    160:160,
#    162:162,
#    163:163,
#    164:164,
#    169:169,
#    170:170,
#    178:178,
#    180:180,
#    181:181,
#    182:182,
#    184:184,
#    185:185,
#    187:187,
#    188:188,
#    189:189,
#    190:190,
#    192:192,
#    193:193,
#    196:196,
#    197:197,
#    198:198,
#    202:202,
#    204:204,
#    205:205,
#    206:206,
#    208:208,
#    209:209,
#    230:230,
#    232:232,
#    235:235,
#    239:239,
#    241:241,
#    247:247,
#    258:258,
#    259:259,
#    295:295,
#    298:298,
#    299:299,
#    302:302,
#    317:317,
#    321:321,
#    327:327,
#    331:331,
#    333:333,
#    334:334,
#    335:335,
#    340:340,
#    341:341,
#    342:342,
#    343:343,
#    345:345,
#    361:361,
#    369:369,
#    374:374,
#    378:378,
#    380:380,
#    392:392,
#    405:405,
#    406:406,
#    418:418,
#    422:422,
#    423:423,
#    433:433,
#    434:434,
#    435:435,
#    436:436,
#    437:437,
#    439:439,
#    441:441,
#    443:443,
#    445:445,
#    447:447,
#    448:448,
#    449:449,
#    450:450,
#    451:451,
#    458:458,
#    477:477,
#    478:478,
#    480:480,
#    481:481,
#    485:485,
#    489:489,
#    490:490,
#    491:491,
#    492:492,
#    493:493,
#    494:494,
#    495:495,
#    507:507,
#    515:515,
#    522:522,
#    523:523,
#    588:588
#
#}
#
#conceptos = df['concepto']
#
#df['Existe'] = conceptos.map(cuenta_catalogo_sql)


s = pd.Series(['cat', 'dog', np.nan, 'rabbit'])

s

s.map({'cat': 'kitten', 'dog': 'puppy'})
