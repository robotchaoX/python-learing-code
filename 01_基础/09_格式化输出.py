# 定义字符串变量 name，输出 我的名字叫 小明，请多多关照！
name = "小明"
print("我的名字叫 %s" % name)  # % 一个变量
age = 18
print("name: %s , age: %d" % (name, age))  # %( , ) 两个变量

# 定义整数变量 student_no，输出 我的学号是 000001
student_cnt = 3
print("学生数量: %06d" % student_cnt)  # 位数不足补0
student_no = 123456789
print("我的学号: %06d" % student_no)  # 超了不影响

# 定义小数 price、weight、money，
# 输出 苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00 元
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价 %.2f 元／斤，购买了 %.3f 斤，需要支付 %.4f 元" % (price, weight, money))  # %.2f小数点后2位

# 定义一个小数 scale，输出 数据比例是 10.00%
scale = 0.8
print("数据比例是 %.2f%%" % (scale * 100))
# print("数据比例是 %.2f%%" % scale * 100)  # 重复100次 # 等价 # print(("数据比例是 %.2f%%" % scale) * 100)

import keyword

print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
