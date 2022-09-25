#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# \File        : ./code/guok/learn-oop2.py
# \Author      : chunni
# \Email       : shachi1758@outlook.com
# \CreateTime  : 2022-09-18 19:59:03
# \Version     : 0.1.0
# \Brief       :
# \Log         :

class Student(object):
    def __init__(self, name : str = "unnamed", age: int = 1, score : float = 11.1) -> None:
        self.__name = name
        self.__age = age
        self.__score = score
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def age(self) -> int:
        return self.__age
    
    @property
    def score(self) -> float:
        return self.__score

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @age.setter
    def age(self, age) -> None:
        self.__age = age
    
    @score.setter
    def score(self, score) -> None:
        self.__score = score
    
