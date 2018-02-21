# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
尝试编写一个使用元组返回多个值的函数。
编写 hours2days 函数，传入一个整数类型的参数，该参数表示一个以小时为单位的时间段。
该函数应该返回一个元组，用天和小时为单位表示传入的时间段，不足一天的时间用小时表示。
例如，39 个小时表示 1 天 15 个小时，所以函数返回的应该是 (1,15)。
"""

def hours2days(tup):
    return int(tup/24), tup%24

print (hours2days(24))

print (hours2days(25))

print (hours2days(10000))