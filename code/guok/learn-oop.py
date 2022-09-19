#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#\File        : code/learn-oop.py
#\Author      : chunni
#\CreateTime  : 2022-09-17 20:15:48
#\Version     : 0.1.0
#\Brief       : Python 的面向对象。
#\Log         :
#             : Sept 17, 2022 学习 “类和实例”、“访问限制”、“继承和多态”

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#         return None
# 
#     def getName(self):
#         return self.name
# 
# 
# bart = Student("chunni", 99)
# temp = Student("dora", 100)
# temp.age = 18
# print(temp.getName())
# 
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#         return None
# 
#     def print_score(self):
#         print("%s %s" % (self.__name, self.__score))
#         return None
# 
# student = Student("chunni", 99)
# print(student.__name)
# Traceback (most recent call last):
#   File "/home/chunni/learnPython/code/./learn-oop.py", line 38, in <module>
#     print(student.__name)
# AttributeError: 'Student' object has no attribute '__name'

# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

# class Student(object):
#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender
#         return None
# 
#     def get_gender(self):
#         if self.__gender == 0 :
#             return "male"
#         elif self.__gender == 1:
#             return "female"
#         else:
#             return None
# 
#     def set_gender(self, gender):
#         self.__gender = gender
#         return None
# 
# bart = Student('Bart', 0)
# print(bart.get_gender())
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender(1)
#     if bart.get_gender() != 'female':
#         print('测试2失败!')
#     else:
#         print('测试成功!')

# class Animal(object):
#     def run(self):
#         print("Animal is running...")
#         return None
#     def eat(self):
#         print("Animal is eating...")
# 
# class Dog(Animal):
#     def run(self):
#         print("Dog is running...")
#         return None
# 
# class Cat(Animal):
#     def run(self):
#         print("Cat is running...")
#         return None
# 
# 
# 
# dog = Dog()
# dog.run()
# 
# cat = Cat()
# cat.run()
# 
# def run_twice(animal: Animal):
#     animal.run()
#     return None
# 
# class AA(object):
#     def run(self):
#         print("time is running...")
#         return None
# 
# 
# run_twice(Animal())
# run_twice(Dog())
# run_twice(Cat())
# run_twice(AA())

# print(type(33))
# print(type(32.5) == float)
# 
# import types
# 
# def fn():
#     pass
# 
# print(type(fn))
# 
# print(type(fn) == types.FunctionType)
# print(type(lambda x : x + x) == types.LambdaType)
# print(type(abs) == types.BuiltinFunctionType)
# print(dir("ABC"))

# class MyObject(object):
#     def __init__(self, attr1: int, attr2: str):
#         self.attr1 = attr1
#         self.attr2 = attr2
#         return None
#     
#     def power(self) -> int:
#         return self.attr1 * int(self.attr2)
# 
# obj = MyObject(1,"2")
# print(hasattr(obj, "attr1")) # True
# setattr(obj, "attr3", 9)
# print(getattr(obj, "attr3")) # 9
# print(getattr(obj, "attr4", 404))

# class Student(object):
#     number = 0
#     def __init__(self, name):
#         self.__name = name
#         Student.number += 1
#         return None

# s1 = Student("chunni")
# s2 = Student("dora")
# print(Student.number)
def mul(*args: int) -> int:
    sum = 1
    for arg in args:
        sum = sum * arg
    return sum

l1 = [1,2,3,4,5]
print(mul(*l1))