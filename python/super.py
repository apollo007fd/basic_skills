#!/usr/bin/env python

#class A(object):  # for python2, object is needed.
class A:
    def add(self, x):
        y = x + 1
        print(y)
class B(A):
    def add(self, x):
        #super(B, self).add(x)  # for python2, 2 more parameters needed
        super().add(x)

b = B()
b.add(2)

#Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx
