#!/usr/bin/python
# -*- coding: UTF-8 -*-
#base64
'''
Base64是一种用64个字符来表示任意二进制数据的方法。
用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。
Base64的原理很简单，首先，准备一个包含64个字符的数组：
'''
import base64
print base64.b64encode('binary\x00string')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64decode('abcd--__')

print base64.b64decode('YWJjZA==')
# print base64.b64decode('YWJjZA')
# print base64.urlsafe_b64decode('YWJjZA')






