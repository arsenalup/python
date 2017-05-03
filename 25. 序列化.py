# -*- coding: utf-8 -*-
from __future__ import print_function
from  __future__ import division
from  __future__ import unicode_literals

import pickle
class Dog:
    def __init__(self,name):
        self.age=1
        self.name=name
    def bark(self):
        print ('my name is:',self.name)
def test_object():
    dog1=Dog('bob')
    with open('object.data','wb')as f_out:
        pickle.dump(dog1,f_out)

    with open('object.data','rb')as f_in:
        dog2=pickle.load(f_in)

    dog1.bark()
    dog2.bark()
    print (dog1.age,dog2.age)

def test_class():
    with open('class.data','wb')as f_out:
        pickle.dump(Dog,f_out)
    with open('class.data','rb')as f_in:
        NewDog=pickle.load(f_in)

    dog1=Dog('jack')
    dog2=Dog('alice')

    dog1.bark()
    dog2.bark()
    print (dog1.age,dog2.age)

if __name__ == '__main__':
    test_object()
    test_class()