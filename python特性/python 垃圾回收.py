#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-10 下午1:31

"""
Python GC主要使用引用计数（reference counting）来跟踪和回收垃圾。
在引用计数的基础上，通过“标记-清除”（mark and sweep）解决容器对象可能产生的循环引用问题，
通过“分代回收”（generation collection）以空间换时间的方法提高垃圾回收效率。

python采用的是引用计数机制为主，
标记-清除(首先标记对象（垃圾检测），然后清除垃圾（垃圾回收）。)
和
分代收集(这种思想简单点说就是：对象存在时间越长，越可能不是垃圾，应该越少去收集。
)两种机制为辅的策略

内存池机制
"""
#1引用计数机制：(简单，实时)python里每一个东西都是对象，它们的核心就是一个结构体：PyObject
#PyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。当一个对象有新的引用时，
#它的ob_refcnt就会增加，当引用它的对象被删除，它的ob_refcnt就会减少
#当引用计数为0时，该对象生命就结束了。


#2标记清除:基本思路是先按需分配，等到没有空闲内存的时候从寄存器和程序栈上的引用出发，
# 遍历以对象为节点、以引用为边构成的图
# (可达的（reachable）对象标记为活动对象，不可达的对象就是要被清除的非活动对象。根对象就是全局变量、调用栈、寄存器。)
# 把所有可以访问到的对象打上标记，然后清扫一遍内存空间，把所有没标记的对象释放。