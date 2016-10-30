#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 文档测试
import re
m = re.search('(?<=abc)def', 'abcdef')
print m.group(0)