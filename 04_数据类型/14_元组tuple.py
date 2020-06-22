# 元组
# 元组里数据的类型可以不同
employee_tuple = ("zhangsan", 18, 1.75, True)
print(type(employee_tuple))
print("元组 = ", employee_tuple)

# 多个数据元组
tp1 = (10, 20, 30)
print(type(tp1))

#! 单个数据元组,末尾需要逗号，标识
tp2 = (10,)  # 当个数据末尾需要逗号，标识
print(type(tp2))  # tuple
# 如果单个元组不加逗号，标识，就是单个基础类型数据，不是元组
tp3 = (10)  # 单个数据
print(type(tp3))  # int

tp4 = ("abc",)  # 当个数据末尾需要逗号，标识
print(type(tp4))  # tuple
# 如果单个元组不加逗号，标识，就是单个基础类型数据，不是元组
tp5 = ("abc")  # 单个数据
print(type(tp5))  # str
