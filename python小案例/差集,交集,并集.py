#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-14 下午8:01

t=[1,2,3,4]
s=[3,4,5,6]

a=list(set(t)|set(s)) #并集

b=list(set(t)&set(s)) #交集

c=list(set(t)-set(s)) #差集

d=list(set(t)^set(s)) #对称差集
