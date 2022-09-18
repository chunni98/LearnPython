#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#\File        : ./code/guok/learn-oop2.py
#\Author      : chunni
#\Email       : shachi1758@outlook.com
#\CreateTime  : 2022-09-18 19:59:03
#\Version     : 0.1.0
#\Brief       :
#\Log         :

# from types import MethodType

# class Student(object):
#     pass
# 
# s = Student()
# s.name = "chunni" # 给实例绑定一个属性。
# print(s.name)
# 
# def set_age(self, age):
#     self.age = age
#     return None
# 
# s.set_age = MethodType(set_age, s) #  # 给实例绑定一个方法
# s.set_age(19)
# print(hasattr(s, "age")) 
# 
# def set_score(self, score):
#     self.score = score
#     return None
# 
# Student.set_score = set_score # 给 class 绑定方法。
# 
# print(dir(Student))
# print("")
# print(dir(Student()))
# 
# s2 = Student()
# s2.set_score(12)
# print(s2.score)
# print(hasattr(Student(), "score")) # False

# class Student(object):
#     __slots__ = ("name", "age")
# 
# s = Student()
# s.name = "Chunni"

# class Student(object):
#     def __init__(self, name: str, age: int):
#         self.__name = name
#         self.__age = age
#         return None
#     @property
#     def name(self)->str:
#         return self.__name
    
#     @name.setter
#     def name(self, name: str):
#         if not isinstance(name, str):
#             raise ValueError('score must be an str!')
#         else:
#             self.__name = name
    
#     @property
#     def age(self)->int:
#         return self.__age
    
#     @age.setter
#     def age(self, age: int):
#         if not isinstance(age, int):
#             raise ValueError('score must be an integer!')
#         if age < 0 or age > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self.__age = age

# s = Student("chunni", 23)

# print(s.age, s.name)
# s.age =13
# s.name = "karl"
# print(s.age, s.name)

# class Screen(object):
#     def __init__(self, width: float, height: float):
#         self.__width = width
#         self.__height = height
#         return None
    
#     @property
#     def width(self)->float:
#         return self.__width
    
#     @width.setter
#     def width(self, width: float):
#         if not isinstance(width, float):
#             raise ValueError("...")
#         else:
#             self.__width = width
#         return None

# class Student(object):
#     def __init__(self, name: str) -> None:
#         self.__name = name
#         return None
    
#     def __str__(self) -> str:
#         return 'Student object (name: %s)' % self.__name
    
#     __repr__ = __str__

# print(Student("Mike"))

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    
    def __getitem__(self, n)->int:
        a, b = 1, 1
        for x in range(n):
            a = b
            b = a + b
        return a

for i in Fib():
    print(i)