#!/usr/bin/python
# -*- coding: UTF-8 -*-
print abs(-10)
print abs
a = abs(-10)
print a
#变量可以指向函数
a = abs
print a


def add(x, y, f):
    return f(x) + f(y)
print add(-5, 6, abs)


def f(x):
    return x * x
print  map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print  map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])


def add(x, y):
    return x + y
print reduce(add, [1, 3, 5, 7, 9])

def fn(x, y):
    return x * 10 + y
print reduce(fn, [1, 3, 5, 7, 9])

#Python内建的filter()函数用于过滤序列
def is_odd(n):
    return n % 2 == 1
print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
# 结果: [1, 5, 9, 15]

#把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])
# 结果: ['A', 'B', 'C']

#排序算法
#Python内置的sorted()函数就可以对list进行排序
print sorted([36, 5, 12, 9, 21])
#sorted()函数也是一个高阶函数
def reversed_cmp(x, y):
    if x > y:  #正常来说是返回1
        return -1
    if x < y:
        return 1
    return 0
#传入自定义的比较函数reversed_cmp，就可以实现倒序排序：
print sorted([36, 5, 12, 9, 21], reversed_cmp)

#字符串排序
print  sorted(['bob', 'about', 'Zoo', 'Credit'])
#对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
#['Credit', 'Zoo', 'about', 'bob']
#现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能定义出忽略大小写的比较算法就可以
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
#忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
#['about', 'bob', 'Credit', 'Zoo']