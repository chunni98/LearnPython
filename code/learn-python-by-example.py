#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#\File        : learn-python-by-example.py
#\Author      : chunni
#\CreateTime  : 2022-09-10 20:38:39
#\Version     : 0.1.0
#\Brief       : learn-python-by-example
#\Log         : 
#             : Sept. 10, 2022 创建文件。

# 函数式编程

# Python对函数式编程提供部分支持。
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

## 高阶函数
# 变量可以指向函数；函数名也是变量；函数可以作为参数
def f(x, y, fun):
    return fun(x) + fun(y)
# 类似 C 语言的回调函数
print(f(-1, -2, abs))

## Map and Reduce

# map
l1 = list(range(0,10))
# 把 l1 所有的元素变成字符串
r = map(str, l1)
print(list(r))

# map() 的返回值是一个 Iterator，是一个惰性序列。
# reduce() 返回值是一个具体的值
# reduce

# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，

from functools import reduce

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 将 [1,3,5,7,9] 转为 13579
def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1,3,5,7,9]))

# 例子：str2int()
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def chr2num(s):
    return DIGITS[s]

def str2int(string):
    return reduce(lambda x,y: x * 10 + y, map(chr2num, string))

print(isinstance(str2int("12345"),int))
from functools import reduce


def normalize(name):
    return list(map(lambda s : s[0].upper() + s[1:].lower(), name))

L1 = ['adam', 'LISA', 'barT']
print(normalize(L1))

def prod(L):
    return reduce(lambda x, y: x * y, L)

print(prod([3, 5, 7, 9]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def chr2num(c):
    return DIGITS[c]

def str2float(s):
    j = 0
    for i, ch in enumerate(s):
        if ch == '.':
            j = i
        l1 = s[:j]
        l2 = s[j + 1:]
        print(l2)

    return reduce(lambda x, y: x * 10 +y, map(chr2num, l1)) + (reduce(lambda x, y: x * 10 + y, map(chr2num,l2)) * 0.0001  )

print(isinstance(str2float("3.2415"), float))
print(str2float("3.2415"))
## filter
def is_odd(num):
    return num % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
# filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
# filter()、map()、reduce()必须接受两个参数，第一个参数是判断函数，第二个参数是可迭代对象。
# 因此如果判断函数需要多个参数，可以用lambda 替代。

# 构造一个从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x : x % n > 0

def aaa(x, n):
    return x % n > 0

def prime():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it)
        yield n
        # it = filter(_not_divisible(n), it)
        it = filter(lambda x : aaa(x, n), it )

for i in prime():
    print(i)
    if i > 100:
        break
# 筛选出回数
def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = list(filter(is_palindrome, range(1, 200)))
print(output)

## 筛选函数
def is_palindrome(x):
    return str(x) == str(x)[::-1]

# 全体自然数序列，惰性求值
def all_num():
    n = 0
    while True:
        yield n
        n += 1

# 获得筛选后的回数序列，惰性求值
def palindrome():
    it = all_num() # 首先获得Iterator对象:
    it = filter(is_palindrome, it) # 获得筛选后的序列
    while True:
        x = next(it) 
        yield x

for i in palindrome():
    if i > 200:
        break
    print(i, end = ",")
# 排序

# sorted 对 list 排序
l1 = [36, 5, -12, 9, -21]
print(sorted(l1))

# 接受函数实现自定义排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
# 反向排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(l):
    return l[0].lower()

def by_score(l):
    return l[1]

L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score, reverse=True)
print(L2)
print(L3)

## 返回函数

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(1,2,3,4,5,6)
print(f)        # 返回求和函数:  <function lazy_sum.<locals>.sum at 0x7fd59b1be050>
print(f())      # 调用函数 f，返回结果: 21

# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种程序结构称为“闭包（Closure）”。
# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

f1 = lazy_sum(1,2,3,4,5,6)
f2 = lazy_sum(1,2,3,4,5,6)
print(f1 == f2) # False, f1()和f2()的调用结果互不影响。

#返回的函数并没有立刻执行，而是直到调用了才执行。因此返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要使用，请重新创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def count():
    fs = []
    def f(x):
        return lambda  : x * x 

    for i in range(1, 4):
        # def f():
        #     return i * i
        # fs.append(f)
        fs.append(f(i)) ## f(i)立刻被执行，因此 i 的当前值被传入f(x) 
    return fs

f1, f2, f3 = count()
print(f2())

## nonlocal

# 使用闭包时，对外层变量赋值前，需要先使用 nonlocal 声明该变量不是当前函数的局部变量。

def inc():
    x = 0
    def temp():
        nonlocal x
        x = x + 1
        return x
    return temp

print(inc()()) # 1
# 每次 调用了inc() 都返回一个新的 函数，局部变量不同。
print(inc()()) # 1
f = inc()
print(f()) # 1
print(f()) # 2

# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return x
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5

#  装饰器
# 装饰器本质上是一个函数，作用是为已经存在的函数或对象添加额外的功能。
# 如插入日志、性能测试、事务处理、权限校验等场景。

# 一个简单例子：
# 一个函数：

def hi():
    print("Hello,world")
    return None

# 想在不破坏 hi 代码的基础上，给 hi 添加功能：
def decorator(func):
    def wrapper():
        print("Before func()...")
        ret = func()
        print("After func()...")
        return ret
    return wrapper

# 这已经是一个简单的装饰器了。

# 使用语法糖：

def decorator(func):
    def wrapper():
        print("Before func()...")
        # 注意，如果被装饰的函数有返回值，要记得返回。
        ret = func()
        print("After func()...")
        return ret
    return wrapper

@decorator
def hi():
    print("Hello,world")
    return None

# 如果原函数带有参数，返回的函数也要带有相同的参数:
def decorator(func):
    def wrapper(name):
        print("Before func()...")
        ret = func(name)
        print("After func()...")
        return ret
    return wrapper

@decorator
def hi(name):
    print("hi,%s!" % name)
    return name

def hello(name, age):
    print("hello, %s, %d years old." % (name, age))
    return None

# 但是这样的话，又不能适用于其他参数不一样的函数了，
# Python 有 *args 和 **kwargs 可以接收任意数量的位置参数和关键字参数。
# 因此 可以这样写：

def decorator(func):
    def wrapper(*args, **kw):
        print("Before func()...")
        ret = func(*args, **kw)
        print("After func()...")
        return ret
    return wrapper

@decorator
def hi(name):
    print("hi,%s!" % name)
    return name

@decorator
def hello(name, age):
    print("hello, %s, %d years old." % (name, age))
    return None

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("Before func()..., %s." % text)
            ret = func(*args, **kw)
            print("After func()...")
            return ret
        return wrapper
    return decorator

@log("text")
def hi(name):
    print("hi,%s!" % name)
    return name

def hello(name ,age):
    print("hello, %s , %d years old." % (name, age))
    return None

@log("text") 等同于 hi = log("text")(hi) 的语法糖。

# 由于，函数也是对象，它有__name__等属性，需要把原始函数的__name__等属性复制到wrapper()函数中，
# 否则，有些依赖函数签名的代码执行就会出错。
# 使用 functools.wraps()

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("Before func()..., %s." % text)
            ret = func(*args, **kw)
            print("After func()...,func name is %s." % func.__name__)
            return ret
        return wrapper
    return decorator

@log("text")
def hi(name):
    print("hi,%s!" % name)
    return name

# h() # decorator(hi)() 效果一样
# hi() # 使用 语法糖后 hi = decorator(hi)
hi("karl")

# example 1
# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间

import functools
import time

def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start_time = time.time()
        ret = func(*args, **kw)
        end_time = time.time()
        print("time: %f" % (end_time - start_time))
        return ret
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

# example 2
# 如果装饰器可选参数，使用无参数的装饰器，需要写成：
# @log() 一定不能忘记空格，这样代表 log 使用默认参数，否则将会把 被装饰的函数当作参数。

def log(text = "nothing"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(text)
            return func(*args, **kw)
        return wrapper
    return decorator

# 注意不要忘记写括号。
@log()
def f():
    pass

@log(text = "execute")
def g():
    pass

f()
g()

# 偏函数
import functools

int2 = functools.partial(int, base = 2)
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2("10002") # 相当于 int("10002", base = 2)
# 相当于kw = {base: 2} int("10002",**kw)

# 模块

# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
# __init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是文件名。
# 模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。

# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
# 最常见的就是运行测试。

if __name__ == "__main__":
    pass

# 作用域

# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如 _abc，__abc 等；
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。

# 安装 第三方模块使用 pip 

