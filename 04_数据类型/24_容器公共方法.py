# 公共方法

# 1.运算符
str1 = "aa"  # 字符串
str2 = "bb"
list1 = [11, 22]  # 列表
list2 = [33, 44]
tuple1 = (5, 6)  # 元组
tuple2 = (7, 8)
dict1 = {"name": "python"}  # 字典
dict2 = {"age": 18}
# + 合并 (字符串，列表，元组)
print(str1 + str2)  # 字符串
print(list1 + list2)  # 列表
print(tuple1 + tuple2)  # 元组
# 字典不支持 +合并
# print(dict1 + dict2)  # 字典


str1 = "A"
list1 = [11, 22]
tuple1 = (5, 6)
dict1 = {"name": "python"}
# * 元素复制 (字符串，列表，元组)
print(str1 * 5)  # 字符串
print(list2 * 5)  # 列表
print(tuple1 * 5)  # 元组
# 字典不支持 *复制
# print(dict1 * 5)  # 字典

str1 = "abcde"
list1 = [11, 22]
tuple1 = (5, 6)
dict1 = {"name": "python", "age": 18}
# in 和 not in 是否存在 (字符串，列表，元组，字典)
print("a" in str1)  # 字符串
print("a" not in str1)
print(11 in list1)  # 列表
print(11 not in list1)
print(5 in tuple1)  # 元组
print(5 not in tuple1)
print("name" in dict1)  # 字典
print("name" not in dict1)
print("name" in dict1.keys())
print("name" not in dict1.keys())
print("python" in dict1.values())
print("python" not in dict1.values())
print(("age", 18)in dict1.items())
print(("age", 18) not in dict1.items())


# 2.公共方法
# len 统计数据个数
str1 = "abcde"
list1 = [11, 22, 33, 44]
tuple1 = (5, 6, 7)
dict1 = {"name": "python", "age": 18}
print(len(str1))
print(len(list1))
print(len(tuple1))
print(len(dict1))

# del 删除变量
str1 = "abcde"
list1 = [11, 22, 33, 44]
tuple1 = (5, 6, 7)
dict1 = {"name": "python", "age": 18}
# str是不可变数据，不可以下标删除某个元素值
# del str1[1]  # error
# 删除整个字符串容器
del str1
# print(str1)

# 删除列表某个元素值
del list1[1]
# print(list1[1])
# 删除整个列表容器
del list1
# print(list1)

# 元组tuple是不可变数据，不可以下标删除某个元素值
# del tuple1[1] # error
# 删除整个元组容器
del tuple1
# print(tuple1)

# 删除字典某个键值对
del dict1["name"]
# print(dict1["name"])
# 删除整个字典容器
del dict1
# print(dict1)


# max 最大值
# min 最小值
str1 = "abcde"
list1 = [11, 22, 33, 44]
tuple1 = (5, 6, 7)
dict1 = {"name": "python", "age": 18}
print(max(str1))
print(min(str1))
print(max(list1))
print(min(list1))
print(max(tuple1))
print(min(tuple1))
print(max(dict1))  # key的最大值
print(min(dict1))

# range生成序列
# range(start,end,step)
# 范围[start,end)左闭右开
# 0 1 2 3 4 5 6 7 8 9
for i in range(0, 10, 1):  # [0,10)步长1
    # print(i)
    pass

# 0 1 2 3 4 5 6 7 8 9
for i in range(0, 10):  # 默认步长1
    # print(i)
    pass

# 0 2 4 6 8
for i in range(0, 10, 2):  # [0,10)步长2
    # print(i)
    pass

# 0 1 2 3 4 5 6 7 8 9
for i in range(10):  # 默认0开始，步长1
    # print(i)
    pass

# enumerate 将可遍历对象组合为一个索引序列
# enumerate 返回值是元组，第一个是原迭代对象对应的小标，第二个是原迭代对象的数据
list1 = ["a", "b", "c", "d"]
for i in enumerate(list1):  # 默认下标起始0
    print(i)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')

for i in enumerate(list1, 100):  # 下标起始值100
    print(i)
# (100, 'a')
# (101, 'b')
# (102, 'c')
# (103, 'd')
