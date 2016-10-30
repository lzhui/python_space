#!/usr/bin/python
# -*- coding: UTF-8 -*-
#获取对象信息
#判断对象类型，使用type()函数：
import types
class Animal(object):
    def run(self):
        print 'Animal is running...'
class Dog(Animal):
    def run(self):
        print 'Dog is running...'

    def eat(self):
        print 'Eating meat...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly...'

def run_twice(animal):
    animal.run()
    animal.run()
class Husky(Dog):
    def run(self):
        print 'Husky is running slowly...'

print type(123)
print type('str')
print type(None)
print  type(abs)
a = Animal()
print type(a)

print type(123)==type(456)
print type(int)

print type('abc') == types.StringType
print type(u'abc')==types.UnicodeType
print type([])==types.ListType
print type(str)==types.TypeType
a = Animal()
d = Dog()
h = Husky()
print isinstance(h,Husky)
print isinstance(h, Dog)
print isinstance(h, Animal)
print  isinstance(d, Dog) and isinstance(d, Animal)
print isinstance(d, Husky)
#能用type()判断的基本类型也可以用isinstance()判断：
print  isinstance('a', str)
print  isinstance('a', str)
print isinstance('a', unicode)
#并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode：
print isinstance('a', (str, unicode))
print isinstance(u'a', (str, unicode))
#由于str和unicode都是从basestring继承下来的，所以，还可以把上面的代码简化为：
print isinstance(u'a', basestring)

#使用dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print  dir('ABC')

'''
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
'''
print len('ABC')
print 'ABC'.__len__()

#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def __len__(self):
        return 100
    def power(self):
        return self.x * self.x
obj = MyObject()
print len(obj)
#剩下的都是普通属性或方法，比如lower()返回小写的字符串：
print 'ABC'.lower()
print  hasattr(obj, 'x')  # 有属性'x'吗？
print  obj.x
print hasattr(obj, 'y') # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print hasattr(obj, 'y') # 有属性'y'吗？
print getattr(obj, 'y') # 获取属性'y'
print obj.y  # 获取属性'y'

#如果试图获取不存在的属性，会抛出AttributeError的错误：
#print getattr(obj, 'z')  # 获取属性'z'

#可以传入一个default参数，如果属性不存在，就返回默认值：
print  getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404

#也可以获得对象的方法：
print hasattr(obj, 'power') # 有方法'power'吗？
print getattr(obj, 'power')  # 获取属性'power'
fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn
print  fn # fn指向obj.power
print  fn() # 调用fn()与调用obj.power()是一样的
'''
通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
'''
sum = obj.x + obj.y
#就不要写：
sum = getattr(obj, 'x') + getattr(obj, 'y')




