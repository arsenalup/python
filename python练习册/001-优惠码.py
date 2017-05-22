# -*- coding: utf-8 -*-
import random
import string
b=[]
while len(set(b))<200:


    for i in range(0,200):
        a=list(string.ascii_letters)
        random.shuffle(a)
        a=''.join(a)
        b.append(a[:8])
    # print b
    print b[1]