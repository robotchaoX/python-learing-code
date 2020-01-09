"""
姓名：小明
年龄：18 岁
性别：是男生
身高：1.75 米
体重：75.0 公斤
"""

# 在 Python 中，定义变量时是不需要指定变量的类型的
# 在运行的时候，Python 解释器，会根据赋值语句等号右侧的数据
# 自动推导 出变量中保存数据的准确类型

# str 表示是一个字符串类型
name = "小明"
print(type(name))

# int 表示是一个整数类型
age = 18
print(type(age))

# bool 表示是一个布尔类型，真 True 或者假 False
gender = False  # 不是
print(type(gender))

# float 表示是一个小数类型，浮点数
height = 1.75
print(type(height))

weight = 75
print(name)

# python3 不区分 int 和 long, 都是int, python2 区分
print(type(2 ** 32), 2 ** 32)  # python3 int , python2 int
print(type(2 ** 64), 2 ** 64)  # python3 int , python2 long
print(type(2 ** 1000), 2 ** 1000)  # python 不会溢出??

# 字符串拼接 +
first_name = "三"
last_name = "张"
name = first_name + last_name
print(name)

#  重复拼接字符串
print("-" * 50)
