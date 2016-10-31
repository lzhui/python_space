#!/usr/bin/python
# -*- coding: UTF-8 -*-
#collections集合模块
'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
可以验证创建的Point对象是tuple的一种子类：
'''
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x
print p.y
print isinstance(p, Point)
print isinstance(p, tuple)
Circle = namedtuple('Circle', ['x', 'y', 'r'])

'''
deque
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
'''
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q

'''
defaultdict
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
'''
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print dd['key1'] # key1存在
print dd['key2']  # key2不存在，返回默认值

'''
OrderedDict
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict：
'''
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d # dict的Key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od # OrderedDict的Key是有序的

'''
注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
'''
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print od.keys() # 按照插入的Key的顺序返回

from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)

'''
Counter
Counter是一个简单的计数器，例如，统计字符出现的个数：
'''
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print c













