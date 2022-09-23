#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# \File        : ./code/guok/learn-oop2.py
# \Author      : chunni
# \Email       : shachi1758@outlook.com
# \CreateTime  : 2022-09-18 19:59:03
# \Version     : 0.1.0
# \Brief       :
# \Log         :

class MyMetaclass(type):
    def __new__(cls, name: str, bases: tuple, dct: dict) :
        obj = super().__new__(cls, name, bases, dct)
        return obj

class Myclass(metaclass = MyMetaclass):
    pass

myclass = Myclass()
print(myclass.__class__)
print(myclass.__class__.__class__) # <class '__main__.MyMetaclass'>