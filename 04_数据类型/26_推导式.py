# 推导式
# 列表推导式
# [xx for xx in range()]
# 集合推导式
# {xx for xx in 容器}
# 字典推导式
# {key:value for ... in ...}

# * 1.列表推导式
# 列表生成式
# 创建有规律的列表

# 创建1-9列表
# while 循环
list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)

# for 循环
list1 = []
for i in range(0, 10, 1):
    list1.append(i)
print(list1)

#! 列表推导式
list1 = [i for i in range(0, 10)]
print(list1)
list1 = [i*2 for i in range(0, 10, 1)]
print(list1)

# 带if的列表推导式
# 创建0-10的偶数列表
# range步长控制
list2 = [i for i in range(0, 10, 2)]  # 步长2
print(list2)

# for 循环
list2 = []
for i in range(0, 10, 1):
    if i % 2 == 0:  # 条件
        list2.append(i)
print(list2)

#! 带if的列表推导式
list2 = [i for i in range(10) if i % 2 == 0]
print(list2)

# 多个for循环实现列表推导式
# [(1,10),(1,20),(1,30),
#  (2,10),(2,20),(2,30)]
list3 = []
for i in range(1, 3):
    for j in range(10, 40, 10):
        list3.append((i, j))
print(list3)

#! 多个for循环实现列表推导式
# 多个for循环的列表推导式 等同于 for循环嵌套
list3 = [(i, j) for i in range(1, 3) for j in range(10, 40, 10)]
print(list3)


# * 2.字典推导式
# 创建字典
# {0: 0,   1: 1,   2: 4,   3: 9,   4: 16}
dict1 = {i: i**2 for i in range(5)}
print(dict1)

# 将两个列表合并为字典
list_key = ["name", "age", "gender"]
list_value = ["张三", 18, "男"]
dict2 = {list_key[i]: list_value[i] for i in range(len(list_key))}
print(dict2)

# 提取字典中的目标数据
# 提取分数超过60的键值对
dict_score = {"张三": 22, "小明": 59, "小红": 99, "老王": 88}
dict_pass = {key: value for key, value in dict_score.items() if value >= 60}
print(dict_pass)


# * 3.集合推导式
list4 = [1, 1, 2, 2, 3]
# 集合自动去重
set4 = {i ** 2 for i in list4}
print(set4)
