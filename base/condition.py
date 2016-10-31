#!/usr/bin/python
#coding:utf-8
age =3
if age >= 18:
    print 'your age is',age
    print 'audlt'
elif age >= 6:
    print 'your age is',age
    print 'tennager'
else:
    print 'your age is',age
    print 'kid'

age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'

names = ['Michael','Bob','Tracy']
for name in names:
    print name

sum = 0
for x in range(1,11):
    sum = sum + x
print sum
print range(5)

sum = 0
for x in range(101):
    sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

birth = int(raw_input('birth:'))
if birth < 2000:
    print '00前'
else:
    print '00后'


