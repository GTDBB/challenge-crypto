#!/usr/bin/python
# -*- coding: utf-8 -*-
#简单异或加密
#空格出现最多，32
all_the_text = open('/users/gaoteng/documents/euler_59.txt').read()
#导入ascii码
encrypted_val = [int(v) for v in all_the_text.split(',')] 
ascii_sum = 0
for i in range(3):
    key_list = [encrypted_val[j] ^ 32 for j in range(i, len(encrypted_val), 3)]
    key_ = max(key_list, key=key_list.count) #干净利落，巧妙的使用max()函数中的key
    print(key_)
    ascii_sum += sum([encrypted_val[j] ^ key_ for j in range(i, len(encrypted_val), 3)])
print(ascii_sum)