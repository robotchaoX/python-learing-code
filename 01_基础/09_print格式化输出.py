# % 格式化输出

# 定义字符串变量 name
name = "小明"
print("名字:", name)  # 直接输出
print("我的名字叫 %s" % name)  # % name 一个变量
age = 18
print("name: %s , age: %d" % (name, age))  # %( a, b) 两个变量

# 定义整数变量 student_no，输出 我的学号是 000001
student_cnt = 3
print("学生数量: %06d" % student_cnt)  # 位数不足补0
student_no = 123456789
print("我的学号: %06d" % student_no)  # 位数超了不影响

# 定义小数 price、weight、money，
# 输出 苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00 元
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价 %.2f 元／斤，购买了 %.3f 斤，需要支付 %.4f 元" %
      (price, weight, money))  # %.2f 小数点后2位

# 定义一个小数 scale，输出 数据比例是 10.00%
scale = 0.8
print("数据比例是 %.2f%%" % (scale * 100))  # %.2f%% 百分比
# print("数据比例是 %.2f%%" % scale * 100)  # 重复100次, * 100优先级低
# 等价 # print(("数据比例是 %.2f%%" % scale) * 100)


# f-{}格式化字符串 python3.6
# print(f"名字:{name} , 年龄:{age}")


# 在默认情况下，print 函数输出内容之后，会自动在内容末尾增加换行
print("*")  # 自动换行
print(".............")
print("*", end="\n")  # 默认结束符,换行
print(".............")

print("*", end="--|--|--")  # 修改结束符
print(".............")

print("*", end="\t")  # 列对齐
print(".............")

print("*", end="")  # 取消自动换行
print(".............")


# 格式化字符串后面的 % () 本质是元组
print("%s 年龄是 %d 身高是 %.2f " % ("小明", 21, 1.75))
# 元组
info_tuple = ("小明", 21, 1.75)
# 格式化字符串后面的 % () 本质是元组
print("%s 年龄是 %d 身高是 %.2f " % info_tuple)
# 整体是字符串
info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print(info_str)
