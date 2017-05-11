# -*- coding: utf-8 -*-
from __future____ import print_function
from __future__ import  division
from  __future__ import unicode_literals

import unittest

class Dog:
    def __init__(self,name):
        self.name=name
        self.age=1

    def bark(self):
        return "my name is "+self.name
    def grow_up(self):
        self.age+=k
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name

class TestDog(unittest.TestCase):
    def setUp(self):
        print ('Test begin')
        self.mydog=Dog('Bob')
    def tearDown(self):
        print ('test over!')

    def testBark(self):
        self.assertTrue(self.mydog.bark().startswith('my name is'))
        self.assertTrue(self.mydog.bark().endswith(self.mydog.get_name()))
    def testAge(self):
        old_age=self.mydog.get_age()
        self.mydog.grow_up(3)
        self.assertEqual(old_age+3,self.mydog.get_age())
if __name__=='__main__':
    unittest.main()