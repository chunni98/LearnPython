"""
python六大基本数据类型之String类型
可用单引号或双引号创建字符串类型
Python中没有单字符类型
"""
str1 = "hello world"
str2 = "12345"
str3 = 2222
print(str1[2:8])  # 截取2~8区间子串
print(str(str3) + 'b')  # int 转 string
print(int(str2) + 1)  # string 转 int
print(float(str2) + 1)  # string 转 float

# 格式化字符串
name = '张三'
age = 18
id = 45
score = 314.1592658
text = "我叫{}，今年{}岁，期末考了{}分"
text1 = "我叫{1}，今年{2}岁，编号{0}"
print('姓名：%s' % name)  # s%可用于任意字符
print('年龄：%s' % age)
print('年龄：%d' % age)  # d%为整数专用
print('编号：%03d' % id)  # 不足3位，用0补全
print("分数：%f" % score)  # 默认保留六位小数
print("分数：%.2f" % score)  # 指定保留2位小数，末位四舍五入
print("姓名：%s 年龄：%d 分数：%.2f" % (name, age, score))  # 格式化多个变量
print(f'编号：{id} 姓名：{name} 年龄：{age}')  # f 格式化字符串
print(text.format(name, age, score))  # format函数根据参数顺序格式化
print(text1.format(id, name, age))  # 指定使用参数的顺序

# 内置函数
# 拼接类函数
str4 = '这是一个字符串'
print('|'.join(str4))  # 在字符串中插入指定字符
print(str4.center(50, '*'))  # 字符串居中，'*'为左右填充字符
print(str4.ljust(20, '<'))  # 字符串左对齐，如果指定的长度小于字符串长度，则返回原字符串
print(str4.rjust(20, '>'))  # 字符串右对齐
print(str4.zfill(20))  # 字符串右对齐，若字符串长度小于指定长度，则用0补齐

# 查找类函数
str5 = 'hello world!'
print(str5.count('l'))  # 统计字符出现次数
print(str5.find('l'))  # 返回第一次出现的位置索引，不包含该字符则返回-1
print(str5.index('l'))  # 返回第一次出现的位置索引，不包含该字符则抛出异常
print(str5.rfind('l'))  # 返回最后一次出现的索引，不包含则返回-1
print(str5.rindex('l'))  # 返回最后一次出现的索引，不包含则抛出异常

# 分割和替换
str6 = '!how are you!'
print(str6.replace(' ', '-'))  # 将空格替换成'-'，并不改变原字符串
print(str6.split(' ', 1))  # 按空格分割，指定分割次数，从左往右遍历
print(str6.rsplit(' ', 1))  # 按空格分割，从右往左
print(str6.strip('!'))  # 删除首尾指定字符，默认删除空格
print(str6.lstrip('!'))  # 删除头部指定字符
print(str6.rstrip('!'))  # 删除尾部指定字符

# 大小写操作
str7 = 'watch`s your name?'
str8 = 'abcd'
str9 = 'EFGHIJ'
str10 = 'oHgBdsFG'
print(str7.capitalize())  # 将首字母大写
print(str7.title())  # 将每个单词首字母大写
print(str8.upper())  # 所有字母转大写
print(str9.lower())  # 所有字母转小写
print(str10.swapcase())  # 大小写互换

# 判断内容
st1 = 'dg5b1a3b4ga'
print(st1.startswith('a'))  # 判断是否以a开头
print(st1.endswith('a'))  # 判断是否以a结尾
print(st1.isalnum())  # 判断是否只包含字母或数字
print(st1.isalpha())  # 判断是否只包含字母
print(st1.isdigit())  # 判断是否只包含数字
print(str8.islower())  # 判断是否只包含小写字母
print(str9.isupper())  # 判断是否只包含大写字母
print(st1.isspace())  # 判断是否只包含空白字符










