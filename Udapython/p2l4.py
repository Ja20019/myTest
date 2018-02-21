#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:30:00 2018

@author: jason
"""

"""
练习：飞行马戏团演员表

你将要为电视节目 Monty Python 飞行马戏团的演员创建一个演员表。

编写一个名为 create_cast_list 的函数，该函数将文件名作为输入，并返回一个演员姓名列表。 
该函数将在文件 flying_circus_cast.txt（信息源自 imdb.com）上运行。
该文件的每一行都包含一个演员名字、一个逗号以及一些他们在节目中所扮演角色的（凌乱）相关信息。
你仅需要提取名称并将其添加到列表中。也可以使用 .split() method 处理每一行。

"""

def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as f:
        for line in f:

            eachline = line.split(",")
            cast_list.append(eachline[0])

            print(cast_list[-1])



    return cast_list
    
print(create_cast_list("flying_circus_cast.txt")) 