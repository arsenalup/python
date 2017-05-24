# -*- coding: utf-8 -*-
from __future__ import print_function
from  __future__ import  division
from  __future__ import  unicode_literals

import time
import  functools

def my_timer(func):
    @functools.wraps(func)
    def inner_fun(*args,**kw):
        start_time=time.time()
        ans=func(*args,**kw)
        end_time=time.time()
        print ('time',end_time-start_time,'s')
        return  ans
    return inner_fun

class Test:
    def __init__(self):
        self._x=None

    @property
    def x(self):
        if self._x is None:
            print ('x is none')
        else:
            return self._x

    @x.setter
    def x(self,val):
        if val>100 or val<0:
            print ('input is illegal!')
        else:
            self._x=val


@my_timer
def test_time(n):
    for i in range(n):
        i*n


if __name__ == '__main__':
    test_time(10000000)
    t=Test()
    print (t.x)
    t.x=430
    print (t.x)
    t.x=44
