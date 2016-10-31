#!/usr/bin/python
# -*- coding: UTF-8 -*-
#itertools
#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print n
# cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
# for c in cs:
#     print c

ns = itertools.repeat('A', 10)
for n in ns:
    print n

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 20, natuals)
for n in ns:
    print n

for c in itertools.chain('ABC', 'XYZ'):
    print c

for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group)  # 为什么这里要用list()函数呢？
for key, group in itertools.groupby('A1aaBBbcCAA', lambda c: c.upper()):
    print key, list(group)
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print x
r = map(lambda x: x * x, [1, 2, 3])
print r
r = itertools.imap(lambda x: x*x, [1, 2, 3])
print r
for x in r:
    print x

# r = itertools.imap(lambda x: x*x, itertools.count(1))
r = map(lambda x: x*x, itertools.count(1))
print r
# for n in itertools.takewhile(lambda x: x<100, r):
#     print n







