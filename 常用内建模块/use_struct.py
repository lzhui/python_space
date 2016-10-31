#!/usr/bin/python
# -*- coding: UTF-8 -*-
#struct
import struct
print struct.pack('>I', 10240099)
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
