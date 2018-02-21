#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:06:10 2018

@author: jason
"""

"""
print_list 是一个以列表作为输入，并将其逐行打印为一个编号或项目符号列表的函数。该函数具有三个参数：

    l：要打印的列表
    numbered：设置为 True 时打印编号列表。
    bullet_character：放在每个列表元素之前的符号。如果 numbers 为 True，则忽略。

调用该函数时很麻烦，即使用户想要的是一个编号序列，仍然需要一个 bullet_character 参数！

添加默认参数可使函数更容易使用。默认情况下，该函数可产生一个项目符号列表，默认的项目符号字符应为 "-"。

更改后，该函数的表现如下：

>>> print_list(["cats", "in", "space"])
- cats
- in
- space
>>> print_list(["cats", "in", "space"], True)
1: cats
2: in
3: space

"""

def print_list (l, numbered = False, bullet_character = "-"):
    
    for index, item in enumerate(l):
        if numbered == True:
            print ("{},{}".format(index+1, item))
        else:
            print ("{},{}".format(bullet_character, item))
            
    return

print_list(["cats", "in", "space"])

print_list(["cats", "in", "space"], True)

print_list(["cats", "in", "space", "Univers"], True)
