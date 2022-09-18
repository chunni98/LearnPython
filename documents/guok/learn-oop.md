- [1 概述](#1-概述)
- [2 类和实例](#2-类和实例)
- [3 访问限制](#3-访问限制)
- [4 继承和多态](#4-继承和多态)


## 1 概述

面向对象的设计思想是抽象出Class，根据Class创建Instance。

面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。

类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

## 2 类和实例

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同。

```python

# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的。
class Student(object):          
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去。  
    # 特殊方法“__init__”前后分别有两个下划线！！！
    # __init__方法的第一个参数永远是self，表示创建的实例本身。   
    def __init__(self, name, score): 
        self.name = name
        self.score = score
        return None

    def getName(self):
        return self.name

bart = Student("chunni", 99)
temp = Student("dora", 100)

temp.age = 18 # 给实例绑定一个 age 属性
print(temp.getName())
```

## 3 访问限制

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。

```python

class Student(object):                                                          
    def __init__(self, name, score):                                            
        self.__name = name                                                      
        self.__score = score                                                                 
        return None                                                             
                                                                                
    def print_score(self):                                                      
        print("%s %s" % (self.__name, self.__score))                            
        return None                                                             
                                                                                
student = Student("chunni", 99)
print(student.__name)
# Traceback (most recent call last):
#   File "/home/chunni/learnPython/code/./learn-oop.py", line 38, in <module>
#     print(student.__name)
# AttributeError: 'Student' object has no attribute '__name'

# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

class Student(object):
    def __init__(self, name, gender): 
        self.__name = name
        self.__gender = gender
        return None

    def get_gender(self):
        if self.__gender == 0 :
            return "male"
        elif self.__gender == 1:
            return "female"
        else:
            return None

    def set_gender(self, gender):
        self.__gender = gender
        return None

bart = Student('Bart', 0)
print(bart.get_gender())
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender(1)
    if bart.get_gender() != 'female': 
        print('测试2失败!')
    else:
        print('测试成功!')
```
## 4 继承和多态