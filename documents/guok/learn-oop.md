****- [1 概述](#1-概述)
- [1 概述](#1-概述)
- [2 类和实例](#2-类和实例)
- [3 访问限制](#3-访问限制)
- [4 继承和多态](#4-继承和多态)
  - [4.1 Python 中的继承和多态](#41-python-中的继承和多态)
  - [4.2 静态语言和动态语言](#42-静态语言和动态语言)
- [5 获取对象信息](#5-获取对象信息)
- [6 实例属性和类属性](#6-实例属性和类属性)


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

### 4.1 Python 中的继承和多态
在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为派生类（Subclass），而被继承的 class 称为基类。

当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。

```python
class Animal(object):
    def run(self):
        print("Animal is running...")
        return None
    def eat(self):
        print("Animal is eating...")

class Dog(Animal):
    def run(self):
        print("Dog is running...")
        return None

class Cat(Animal):
    def run(self):
        print("Cat is running...")
        return None



dog = Dog()
dog.run() # Dog is running...

cat = Cat()
cat.run() # Cat is running...
```

在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。

```python
def run_twice(animal: Animal): 
    animal.run()               
    return None                
                               
run_twice(Animal())            
run_twice(Dog())               
run_twice(Cat())               
```

新增一个Animal的子类，不必对 run_twice() 做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

### 4.2 静态语言和动态语言

对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

```python
class AA(object):                        
    def run(self):                       
        print("time is running...")      
        return None

run_twice(AA()) # time is running...
```

这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

## 5 获取对象信息

我们来判断对象类型，使用type()函数：

```python
type(123) == int # True
type("123") == str # True
type("12.3") == float # True
```

判断一个对象是否是函数：
```python
import types                                     
                                                 
def fn():                                        
    pass                                         
                                                 
print(type(fn))                                  
                                                 
print(type(fn) == types.FunctionType)            
print(type(lambda x : x + x) == types.LambdaType)
print(type(abs) == types.BuiltinFunctionType)    
```

**isinstance()**

isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。

能用type()判断的基本类型也可以用isinstance()判断。

并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：

```python
>>>isinstance([1, 2, 3], (list, tuple))
True
```

**dir()**

如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

```python
>>>dir('ABC')
['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
```

类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。

我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：

```python
>>> class MyDog(object):
...     def __len__(self):
...         return 100
...
>>> dog = MyDog()
>>> len(dog)
100
```

配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态:

如果试图获取不存在的属性，会抛出AttributeError的错误，可以传入一个default参数，如果属性不存在，就返回默认值：

```python
class MyObject(object):                        
    def __init__(self, attr1: int, attr2: str):
        self.attr1 = attr1                     
        self.attr2 = attr2                     
        return None                            
■■■■                                           
    def power(self) -> int:                    
        return self.attr1 * int(self.attr2)    
                                               
obj = MyObject(1,"2")                          
print(hasattr(obj, "attr1")) # True            
setattr(obj, "attr3", 9)                       
print(getattr(obj, "attr3")) # 9               
print(getattr(obj, "attr4", 404))              
```

通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。

一个正确的用法的例子如下：

```python
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
```

假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。

## 6 实例属性和类属性

Python是动态语言，根据类创建的实例可以任意绑定属性。

给实例绑定属性的方法是通过实例变量，或者通过self变量：

```python
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
```

如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：

```python
class Student(object):
    name = 'Student'
```
实例属性优先级比类属性高，因此，它会屏蔽掉类的同名属性。

```python
class Student(object):       
    number = 0               
    def __init__(self, name):
        self.__name = name   
        Student.number += 1  
        return None          
                             
s1 = Student("chunni")       
s2 = Student("dora")         
print(Student.number)        
```