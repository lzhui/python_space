#!/usr/bin/python
# -*- coding: UTF-8 -*-
#使用多重继承

#采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计：
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

#会跑和会飞类
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')

# 各种动物:
class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Flyable):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

#通过多重继承，一个子类就可以同时获得多个父类的所有功能。

