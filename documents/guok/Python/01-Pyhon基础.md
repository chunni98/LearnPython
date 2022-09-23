- [1.1 数据类型和变量](#11-数据类型和变量)
  - [1.1.1 输出与输入](#111-输出与输入)
  - [1.1.2 数据类型与变量](#112-数据类型与变量)
- [1.2 字符串和编码](#12-字符串和编码)
- [1.3 list 和 tuple](#13-list-和-tuple)
- [1.4 条件判断](#14-条件判断)
- [1.5 循环](#15-循环)
  - [1.5.1 for 迭代](#151-for-迭代)
  - [1.5.2 while 循环](#152-while-循环)
- [1.6 dict 与 set](#16-dict-与-set)
  - [1.6.1 dict](#161-dict)
  - [1.6.2 set](#162-set)
  - [1.6.3 不变对象与可变对象](#163-不变对象与可变对象)

## 1.1 数据类型和变量

### 1.1.1 输出与输入

```python
print("Hello, world!")
print(*objects, sep=' ', end='\n', file=sys.stdout)

## 输入
inp = input("Please input sth.\n")
print("Your input:",inp)

## 用逗号分隔，输出时用空格隔开
print("I","am","LiHua")

## 打印整数
print("100 + 200 =", 100 + 200)
```

### 1.1.2 数据类型与变量

```python
## 整数
print(1,100,-1000) # 十进制
print(0xff00, 0xa5b4c3d2) # 十六进制
# 下划线分割
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
# 布尔值可以用 and、or、not 运算
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
print(10 / 3) # 精确除法，3.3333333333335 结果是浮点数
print(10 // 3) # 整除，结果是 3
print(10 % 3) # 取余，结果是 1
```

## 1.2 字符串和编码

unicode 2 字节表示一个字符或 4 个字节表示偏僻字符, Ascii 1 Byte，utf-8: 1-6 字节，不定长。

计算机内存中使用 UTF-16，是因为 UTF-16 是定长（两个字节）的，和 Unicode 直接对应。

而 UTF-8 是不定长的，要想知道所代表的字符需要经解码（UTF-8 解码成 Unicode）过程，所以速度慢。

所以存储或传输时使用 UTF-8 ，在内存中时，使用 UTF-16。

```python
print(ord('A')) # 获取 A 的编码: 65
print(ord("中")) # 获取 中 的编码：20013

print(chr(65)) # A
print(chr(20013)) # 中
```

Python 对 bytes 类型的数据用带 'b' 的前缀的单引号或双引号表示。

`x = b"ABC" ` 中 `b"ABC"` 和 `"ABC"` 不同，后者是 `str`，`b"ABC"` 只占 3 字节。

```python
# 通过 Utf-16 表示的 str 可以通过 encode() 方法编码为 bytes.
print("ABC".encode("ascii")) # b"ABC"
print("中文".encode("utf-8")) # b"\xe4\xb8\xad\xe6\x96\x87"

# 从网络或磁盘上读取了字节流，那么读到的数据就是 bytes，变为 utf-16 用 decode：
print(b"\xe4\xb8\xad\xe6\x96\x87".decode("utf-8"))

# len() 计算 str 的字节数
print(len(b"ABC")) #3
print(len(b"\xe4\xb8\xad\xe6\x96\x87")) #6
print(len("中文".encode("utf-8")))
```

常见的格式化占位符： d 整数，f 浮点数， s 字符串， x 十六进制整数

格式化整数还可以格式化整数的位数和补 0 的个数还有小数的位数。

```python
print("Hello, %s, your score is %d" % ("Bart",59))

print("%2d-%02d" % (3,1))
print("%.2f" % 3.1415926)
# % 用 % 转义
print("growth rate: %d %%" % 7)
```

## 1.3 list 和 tuple

```python
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
```

## 1.4 条件判断

```python
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

# x 为非零数值、非空字符串、非空list
if x:
    print("True")
```
## 1.5 循环


### 1.5.1 for 迭代

```python
for i in range(1000):
    print(i)
```

range() 生成的不是个列表，而是一个可迭代对象,可用 list() 把range()返回的可迭代对象转为一个列表。

### 1.5.2 while 循环

```python
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']

for i in L:
    print("Hello,",i, sep = "")
```

break 提前退出循环。

continue 跳过当前的这次循环，直接开始下一次循环。

```python
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
```

## 1.6 dict 与 set

### 1.6.1 dict

dictionary,使用键-值（key-value）存储,具有极快的查找速度。

**初始化**

`d = {"Michael": 95, "Bob": 75, "Tracy": 85}`

`d = dict(Michael = 95, Bob = 75, Tracy = 85)`

**使用**

`print(d["Michael"])`

**通过 key 放入**

dict内部存放的顺序和key放入的顺序是没有关系的。

```python
d["Karl"] = 99
d["Dora"] = 100
d[23] = "dstr"
print(d[23])
```

**判断**

由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值覆盖掉，通过in判断key是否存在：

```python
if "Mike" in d:
    print(d["Mike"])
else:
    d["Mike"] = 23

print(d["Mike"])
# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas')) # 不存在则会输出 None
print(d.get('Thomas',-1)) # 不存在则会输出 -1
```

**删除**

要删除一个key，用pop(key)方法，对应的value也会从dict中删除：

`print(d.pop("Bob"))`

和list比较，dict有以下几个特点：

1. 查找和插入的速度极快，不会随着key的增加而变慢。
2. 需要占用大量的内存，内存浪费多。
而list相反
1. 查找和插入的时间随着元素的增加而增加；
2. 占用空间小，浪费内存很少


**dict 的 key 必须是不可变对象，这是因为 dict 根据 key 来计算 value 的存储位置。**

### 1.6.2 set

set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

要创建一个set，需要提供一个list作为输入集合，重复元素在set中自动被过滤：

```python
s = set(list(range(1,3)))
print(s)
```

**添加元素**

```python
# 通过 add(key) 方法添加元素。
s.add(3)
s.add(4)
```

**移除**

```python
# 使用 remove(key) 方法移除元素。
s.remove(4)
```

**交集、并集**

```python
# set 可看作无序、无重复的集合，可进行交集、并集操作：
s1 = set([1,2,3,4,5])
s2 = set([2,4.6])
print(s1 & s2) # [2,4]
print(s1 | s2) # [1,2,3,4,5,6]
```

### 1.6.3 不变对象与可变对象

对于可变对象，比如list，对list进行操作，list内部的内容是会变化的。

对于不变对象来说，调用对象自身的任何方法，都不会改变对象自身的内容，会创建新的对象返回。