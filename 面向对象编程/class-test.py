#!/usr/bin/python
# -*- coding: UTF-8 -*-
#类和实例
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

#bart = Student()
#print bart
#print Student
#可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
#bart.name = 'Bart Simpson'
#print bart.name

bart = Student('Bart Simpson', 59)
print bart.name
print bart.score
bart.print_score()
print bart.get_grade()

lisa = Student('Lisa Simpson', 87)
bart.age = 8
print bart.age
print  lisa.age
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'
'''
