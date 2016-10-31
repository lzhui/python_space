def my_abs(x):
    if not isinstance(x,(int,float,str)):
        raise TypeError('bad operand type111')
    if x > 0:
        return x
    else:
        return -x
print my_abs('A11')

import math
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi/6)
print x,y
r = move(100,100,60,math.pi/6)
print r
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(2,2)
print power(5,3)
print power(5)

def enroll(name,gender,age=6,city='Bejing'):
    print 'name:',name
    print 'gender:',gender
    print 'age:',age
    print 'city:',city
enroll('lizeng','F')
enroll('bob','f',7)
enroll('adam','F',city='Tianjin')



def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print add_end()
print add_end()

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1, 2]
print calc(*nums)

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
person('mai',30,city='beijing')
person('mail2',20,city='beijing',job='Engineer')

kw  = {'city':'beijing','job':'engineer'}
person('Jack',24,city= kw['city'],job = kw['job'])
person('Tom',23,**kw)

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1,2)
func(1,2,c=3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=99)

args =(1,2,3,4)
kw = {'x':99}
func(*args,**kw)










