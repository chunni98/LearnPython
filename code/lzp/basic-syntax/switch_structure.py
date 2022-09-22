"""
python选择结构语法
Python没有switch命令，用if - elif - else实现选择结构，表达式省略括号
Python中的与或非：and or not
Python中为False的一些值：
    一切0：0, 0.0, 0.000
    一切空：(), [], {}
    None值
"""
i = 0
s = ''
n = None
l = []

if i:
    print('(整型)条件成立')
else:
    print('(整型)条件不成立')

if s:
    print('(字符型)条件成立')
else:
    print('(字符型)条件不成立')

if n:
    print('(None)条件成立')
else:
    print('(None)条件不成立')

if l:
    print('(空类型)条件成立')
else:
    print('(空类型)条件不成立')

"""
python中的逻辑运算符：
用and连接时，从左到右，若表达式为真，则返回最后一个真值；若表达式为假，则返回第一个假值
用or连接时，从左到右，若表达式为真，则返回遇到的第一个真值；若表达式为假，则返回最后一个假值
注：返回值可能是布尔型或是具体数值，取决于语句中最终返回的部分是条件表达式还是具体的数值
"""
print(2 or 3>2)  # 同真，第一个真(2)
print(3>2 or 2)  # 同真，第一个真(True)
print(0 or 3>2)  # 一假一真，返回为真的部分(True)
print(2 or 3<2)  # 一真一假，返回为真的部分(2)
print(0 or 3<2)  # 同假，最后一个假(False)
print(3<2 or 0)  # 同假，最后一个假(0)

print(1 and 3>2)  # 同真，最后一个真(True)
print(3>2 and 1)  # 同真，最后一个真(1)
print(3>2 and 0)  # 一真一假，返回假(0)
print(3<2 and 3>2)  # 一假一真，返回假(False)
print(3<2 and 0)  # 同假，返回第一个假(False)
print(0 and 3<2)  # 同假，返回第一个假(0)


















