#!/usr/bin/python
# -*- coding: UTF-8 -*-
print range(1, 11)
print [x + x for x in range(1, 11)]
print [x * x for x in range(1, 11) if x % 2 == 0]
print [m + n for m in 'ABC' for n in 'XYZ']
import os
print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.iteritems():
    print k, '=', v
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print [k + '=' + v for k, v in d.iteritems()]
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
