"""
python中的变量：
Python中没有声明变量的命令(无需使用任何类型声明)，首次为其赋值时才会创建
字符串类型可以用单引号或双引号进行声明
变量名称只能包含数字、字母、下划线，不能以数字开头，区分大小写
Python允许在一行中为多个变量赋值，或者一行中为多个变量赋相同值
Python同样拥有全局变量和局部变量，在方法中改变全局变量的值需要用global关键字引用该变量
"""

x = 10
y = 3.14
a = "hello"  # 双引号声明字符串
b = 'world'  # 单引号声明
x = "10"  # 变量声明之后甚至可以改变其类型
r, s, t = 1, 2, 3  # 允许一行声明多个变量
o = p = q = 18  # 允许在一行中为多个变量赋相同值


def func():
    str = "局部变量"
    print("这是一个局部变量：" + str)
    global x  # 修改全局变量时先用global关键字进行引用，否则相当于重新定义一个同名的局部变量
    x = "修改了全局变量x的值"


func()







