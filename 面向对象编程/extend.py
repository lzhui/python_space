#!/usr/bin/python
# -*- coding: UTF-8 -*-
#继承和多态
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

dog = Dog()
dog.run()

cat = Cat()
cat.run()

'''
要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：
'''
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

'''
判断一个变量是否是某个类型可以用isinstance()判断：
'''
print isinstance(a, list)
print isinstance(b, Animal)
print isinstance(c, Dog)
print isinstance(c, Animal)
print isinstance(b, Dog)
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())