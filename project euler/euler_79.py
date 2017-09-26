#!/usr/bin/python
# -*- coding: utf-8 -*-
#利用itertools的permutations函数暴力穷举

import re
import itertools as it
#导入数据
text = open('/users/gaoteng/documents/code/python/euler_79.txt').read()
logins = [int(v) for v in text.split('\n')] 
#构造正则表达式
def findlog(n):
  s = list(str(n)) 
  return '.*'+'.*'.join(s)+'.*'
#permutations构造所有的组合  
for i in it.permutations(['1','2','3','6','7','8','9','0'],8): 
  flag = 1
  for j in logins:
    if not re.match(findlog(j),''.join(i)):
      flag = 0
      break
  if flag:
    print ''.join(i)
    break