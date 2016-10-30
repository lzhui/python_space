#!/usr/bin/python
# -*- coding: UTF-8 -*-
#访问限制
'''
实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
'''

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Bart Simpson', 98)
#print bart.__name
'''
这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
'''
print bart.get_name()
'''
如果又要允许外部代码修改score怎么办？可以给Student类增加set_score方法：
'''
bart.set_score(80)
print bart.get_score()
'''
需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
'''
print  bart._Student__name
'''
但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
'''
