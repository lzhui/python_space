#!/usr/bin/python
# -*- coding: UTF-8 -*-
#使用元类
from hello import Hello
h = Hello()
h.hello()
print(type(Hello))

print(type(h))

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)


'''
要创建一个class对象，type()函数依次传入3个参数：
class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''
Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

'''
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。metaclass，直译为元类，简单的解释就是：
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
'''

# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类

