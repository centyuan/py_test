#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-3-26 下午10:22

a=(1,2,3,4,5)
b=[1,2,3,4,5]
c=[7,8,9]
print(a[::-1])#(5, 4, 3, 2, 1)#最后一个表示步长
print(b[::-2])#[5, 3, 1]

print(a[:-1])#(1, 2, 3, 4)
print(b[:-1])#(1, 2, 3, 4)
print(a[:-2])#(1, 2, 3)
#表示从元组中切片，默认从第一个元素开始，到倒数第一个元素前面的那个元素为止
b.append(c)
print(b)
print(b[5])