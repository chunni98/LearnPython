#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#\File        : revise.py
#\Author      : karl
#\Version     : 0.1.0.20220908_base
#\CreateTime  : 2022-09-08 10:41:09
#\Brief       : revise the python grammar
#\Log         :
#             : Sept. 08, 2022 - 创建文件.

# 1 输入输出

## 输出
print("Hello, world!")
# print(*objects, sep=' ', end='\n', file=sys.stdout)

## 输入
inp = input("Please input sth.\n")
print("Your input:",inp)

## 用逗号分隔，输出时用空格隔开
print("I","am","LiHua")

## 打印整数
print("100 + 200 =", 100 + 200)

# 2 数据类型和变量

## 整数
print(1,100,-1000)
print(0xff00, 0xa5b4c3d2)
print(10_000_000_000)
print(0xa1b2_c3d4)

## 浮点数
print(1.23, -9.01)
print(1.23e9,1.2e-5)

## 字符串
print("I'm \"OK\"!")

## 转义字符
print("hello, world!\n")
print("this is tab:\t,\\ is Escape Character")

## 使用 r 不转义
print("\\\t\\")
print(r"\\\t\\")

## 多行输出
print('''Line1
line2
line3''')

print('''Hello,\n
world''')

## 布尔值
# True or False
# 逻辑运算 and or not
age = 13
if age >= 18:
    print("adult")
else:
    print("teenager")

## 空值
an = None
print(an)

## 变量
var_1 = 1
var_2 = 'a'
var_3 = "hello"
var_4 = []
var_1 = (1,2) # 变量只是引用，Python 是动态语言。

## 常量
PI = 3.14159265359

## 四则运算
print(10 / 3) # 3.3333333333335 结果是浮点数
print(10 // 3) # 结果是 3
print(10 % 3) # 结果是 1

# 3 字符串和编码

## 编码
# unicode 2 字节表示一个字符或 4 个字节表示偏僻字符, Ascii 1 Byte
# utf-8: 1-6 字节，不定长
# 计算机内存中使用 UTF-16，是因为 UTF-16 是定长（两个字节）的，和 Unicode 直接对应。
# 而 UTF-8 是不定长的，要想知道所代表的字符需要经解码（UTF-8 解码成 Unicode）过程，所以速度慢。
# 所以存储或传输时使用 UTF-8 ，在内存中时，使用 UTF-16。

print(ord('A')) # 获取 A 的编码: 65
print(ord("中")) # 获取 中 的编码：20013

print(chr(65)) # A
print(chr(20013)) # 中

# Python 对 bytes 类型的数据用带 'b' 的前缀的单引号或双引号表示。
x = b"ABC" # b"ABC" 和 "ABC" 不同，后者是 str，b"ABC" 只占 3 字节。

# 通过 Utf-16 表示的 str 可以通过 encode() 方法编码为 bytes.
print("ABC".encode("ascii")) # b"ABC"
print("中文".encode("utf-8")) # b"\xe4\xb8\xad\xe6\x96\x87"

# 从网络或磁盘上读取了字节流，那么读到的数据就是 bytes，变为 utf-16 用 decode：
print(b"\xe4\xb8\xad\xe6\x96\x87".decode("utf-8"))

# len() 计算 str 的字节数
print(len(b"ABC")) #3
print(len(b"\xe4\xb8\xad\xe6\x96\x87")) #6
print(len("中文".encode("utf-8")))

## 格式化
# 常见的占位符： d 整数，f 浮点数， s 字符串， x 十六进制整数
print("Hello, %s, your score is %d" % ("Bart",59))
# 格式化整数还可以格式化整数的位数和补0的个数还有小数的位数。
print("%2d-%02d" % (3,1))
print("%.2f" % 3.1415926)
# % 用 % 转义
print("growth rate: %d %%" % 7)
# 4 list 和 tuple
## 列表

l1 = [] # 创建一个空列表

l2 = ["Michael", "Bob", "Tracy"]


# print("l2 元素个数为：",end = "")
print("l2 元素个数为: ",len(l2), sep = "")
# print(len(l2)) # len() 获取 list 元素个数。

# 通过下标取得 list 内的元素
i = 0
while i < len(l2):
    print(l2[i])
    i = i + 1

print("")

# 负索引
i = 1
while i <= len(l2):
    print(l2[-i])
    i = i + 1

# 添加元素进 list
l2.append("Mike")
l2.insert(0, "Dora")

# 删除元素
l2.pop() # 删除末尾元素并返回
l2.pop(1) # 删除指定位置元素并返回

# 替换元素
l2[1] = "karl"

# list 内的元素可以是不同类型
l3 = ["Jack", 27, [1,2,3]]
## tuple

# tuple 一旦初始化就不能修改

name = ("Michale", "Bob")

t1 = () # 空 tuple

t2 = (1,) # 定义只有一个元素的 tuple，而不是 t2 = (1)

t3 = (1,2, "Mike", [1,2,"Dora"])
# 5 流程控制
## 条件判断
age = 18
if age >= 18:
    print("Your age is", age)
    print("adult")

age = 3
if age >= 18:
    print("Your age is", age)
    print("adult")
else:
     print("Your age is", age)
     print("teenager")

age = 3
if age >= 18:
    print("Your age is", age)
    print("adult")
elif age > 6:
    print("Teenager")
else:
    print("kid")

x = None

if x:
    print("True")

## 循环

# 迭代 for

for i in range(1000):
    print(i)

# range() 生成的不是个列表，而是一个可迭代对象,可用 list() 把range()返回的可迭代对象转为一个列表。

# while 循环

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']

for i in L:
    print("Hello,",i, sep = "")

# break 提前退出循环。
# continue 跳过当前的这次循环，直接开始下一次循环。
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

# 6 字典和集合

## 字典
# dictionary,使用键-值（key-value）存储,具有极快的查找速度

# 初始化
d = {"Michael": 95, "Bob": 75, "Tracy": 85}
print(d["Michael"])

# 通过 key 放入
d["Karl"] = 99
d["Dora"] = 100
d[23] = "dstr"
print(d[23])

if not "Chunni" in d:
    d["Chunni"] = 33

print(d)

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值覆盖掉。
# 通过in判断key是否存在
if "Mike" in d:
    print(d["Mike"])
else:
    d["Mike"] = 23

print(d["Mike"])
# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas')) # 不存在则会输出 None
print(d.get('Thomas',-1)) # 不存在则会输出 -1

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(d.pop("Bob"))
# dict内部存放的顺序和key放入的顺序是没有关系的。

# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：

# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

# dict的key必须是不可变对象,这是因为dict根据key来计算value的存储位置

## 集合

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set(list(range(1,3)))
print(s)
# 重复元素在set中自动被过滤
# 通过 add(key) 方法添加元素。
s.add(3)
s.add(4)

# 使用 remove(key) 方法移除元素。
s.remove(4)

# set 可看作无序、无重复的集合，可进行交集、并集操作：
s1 = set([1,2,3,4,5])
s2 = set([2,4.6])
print(s1 & s2) # [2,4]
print(s1 | s2) # [1,2,3,4,5,6]
# 对于不变对象来说，调用对象自身的任何方法，都不会改变对象自身的内容，会创建新的对象返回。

# 7 函数

## 调用函数
# help(函数名) 查看函数帮助信息。
help(abs)

# 强制类型转换 
# int(x)，float(x), str(x), hex(x), oct(x), ord(x), chr(x),list()
# 函数别名
at = abs()
print(at(-3))

# 定义函数

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
# return None 可简写为 return

# 空函数
def nop():
    pass

# 参数类型检查
def my_func(x):
    if not isinstance(x,(int, float)):
        raise TypeError("Bad operand type")
    if x > 0:
        return x
    else:
        return -x

# 返回多个值
# 其实 python 返回的仍然是单一值，返回的是 tuple
# 多个变量可以同时接收一个 tuple，按位置赋值。

import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6) # r 是个 tuple

# 函数参数

# 默认参数
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

power(5) # 相当于 print(power(5,2)
# 默认参数必须放在位置参数后面，因为解释器是通过栈来存储参数。
def enroll(name, gender, age = 6, city = "BeiJing"):
    pass

enroll("Mike",'M')
enroll("Jack", 'M', 7, "ShenZhen")
enroll("Nancy", 'F', City = "ShangHai") # 不按顺序提供部分默认参数

# 定义默认参数必须指向不便对象
def add_end(L = None):
    if L is None:
        L = []
    L.append("END")
    return L
# 可变参数
def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum

# 与不使用可变参数的形式区别在于调用时不用组装成列表或 tuple。
calc(1, 2, 3) # 可变参数
calc([1, 2, 3]) # 参数为 list
# 可变参数传进函数的是 tuple，不可变。
# 将 list 或 tuple 传入可变参数函数中：
l1 = [1, 2, 3]
calc(*l1) # 形参前面加上 * 即可。 

# 关键字参数

# 可以给函数传入不受限制的关键字参数，传入的参数有哪些需要在内部检查。
def person(name, age, **kw):
    if "city" in kw:
        pass
    if "job" in kw:
        pass
person("karl", 34, city = "BeiJing", date = 2022)
# 要限制关键字参数：
def person(name, age, *, city, date):
    pass
# * 后的参数被视为命名关键字参数
# 调用有命名关键字参数的函数必须传入参数名，否则会被视作位置参数。
person("karl", 28, city = "ShenZhen", date = 2022)

# 命名关键字参数可以有缺省值，从而简化调用：
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')

# 多种参数组合：
def func(name, age, *args, **kw):
    print("name:",name,"age:",age)
    print("arg:",end = "")
    for arg in args:
        print(arg,end = " ") 
    print("\nkw:")
    for k, v in kw.items():
        print(k, ":", v, end = " ")
    print("")

args = ["Alice", "Bob", "Cindy", 4]
kw = {"city":"ShenZhen", "date":202209}
# 调用 多种参数的函数：
func("Mike", 23, *args, **kw) # 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

def mul(*args):
    sum = 1
    for arg in args:
        sum = sum * arg
    return sum

l1 = [1,2,3,4,5]
print(mul(*l1))

# 8 高级特性

## Slice
l = list(range(0,100))
# 取前三个元素
lt = l[:3] # 0, 1, 2
print(lt)
# 取 后两个元素
lt = l[-2:]
print(lt)
# 从 0 开始，到 -95 为止。
lt = l[:-95]
print(lt)
# 前10个数，每两个取一个
lt = l[:10:2]
print(lt)
# 复制一个 list
lt = l[:]
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print((0, 1, 2, 3, 4, 5)[:3])
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
print('ABCDEFG'[::2])

# 去除字符串首尾的空格
def trim(s):
    result = []
    for i in range(0, len(s) - 1):
        if  s[i] != " ":
            result = s[i:]
            break
    for i in range(-1, -len(result), -1):
        if  s[i] != " ":
            result = result[:i + 1]
            break
    s = result[:]
    return s

print(trim("  dd dd  "))

## 迭代
# 迭代 dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

# 迭代 字符串
for ch in "String":
    print(ch)
# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行
# 通过collections.abc模块的Iterable类型判断是否是可迭代对象：
from collections.abc import Iterable
print(isinstance("abc", Iterable))

# 迭代列表时同时获取下标：
for i, value in enumerate(["a", "B", "C"]):
    print(i, value)

# 迭代时同时引用两个变量：
l = [[1,2],[3,4],[5,6]]
for x, y in l:
    print("(",x,",",y,")")

## 列表生成式

print([x * x for x in range(1,10)])
# 筛选
print([x * x for x in range(1,10) if x % 2 == 0])
# 条件判断
print([x * x if x % 2 == 0 else x  for x in range(1,10)])
# 多层循环
print([m + n for m in 'ABC' for n in 'XYZ'])
# 循环中使用多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + ":" + v for k, v in d.items()])
# 把 l1 中的字符串 小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() if isinstance(s, str) else s for s in L1 if s!=None]

## 生成器
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
g = (x * x for x in range(10))
for i in g:
    print(i)

# 函数形式的生成器
# 注意：调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。
# 可以用了xrange() 替代 range()
# 通过生成器实现杨辉三角：
def triangles(n):
    l = [1,1]
    result = l[:]
    for i in range(0, n):
        if i == 0:
            yield [1,]
        elif i == 1:
            yield result
        else:
            result = [1,1]
            for i in range(1, i):
               result.insert(i, l[i - 1] + l[i])
            l = result[:]
            yield l
    return "done"

for i in triangles(10):
    print(i)

# generator函数的调用实际返回一个generator对象,如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中。

## 迭代器
# 直接作用于for循环的对象统称为可迭代对象：Iterable。
# 生成器都是Iterator 对象，但list、dict、str 虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# Python的for循环本质上就是通过不断调用next()函数实现的，例如：
from collections.abc import Iterator
l = [1,2,3,4,5]
it = iter(l)

for i in l:
    pass 

# 等价于

while True:
    try:
        x = next(it)
    except StopIteration:
        break
