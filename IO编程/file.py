#!/usr/bin/python
# -*- coding: UTF-8 -*-
#文件读写
f = open('test.txt', 'r')
print f.read()
f.close()
'''
由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
'''
try:
    f = open('test.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()
'''
但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
'''
with open('test.txt', 'r') as f:
    print f.read()
'''
这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
'''

'''
如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
'''
f = open('test.txt', 'r')
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉

'''
前面讲的默认都是读取文本文件，并且是ASCII编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
'''
f = open('test.png', 'rb')
#print f.read()

'''
要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：
'''
f = open('test.txt', 'rb')
u = f.read().decode('gbk')
print u


'''
如果每次都这么手动转换编码嫌麻烦（写程序怕麻烦是好事，不怕麻烦就会写出又长又难懂又没法维护的代码），
Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读出unicode：
'''
import codecs
with codecs.open('test.txt', 'r', 'gbk') as f:
    print f.read() # u'\u6d4b\u8bd5

'''
写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
'''
f = open('test.txt', 'w')
f.write('Hello, world!')
f.close()

'''
你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险
'''
with open('test.txt', 'w') as f:
    f.write('Hello, world!666')

'''
在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯
'''
















