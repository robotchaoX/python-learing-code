#  列表 元组 集合 可以相互转换

# list() 转换为列表
# 元组->列表
tuple_1 = (55, 66, 77)
print(type(list(tuple_1)), "//", list(tuple_1), "//", tuple_1)
# 集合->列表
set_1 = {700, 800, 900}
print(type(list(set_1)), "//", list(set_1), "//", set_1)

# tuple() 转换为元组
# 列表->元组
list_1 = [1, 2, 3]
print(type(tuple(list_1)), "//", tuple(list_1), "//", list_1)
# 集合->元组
set_1 = {700, 800, 900}
print(type(tuple(set_1)), "//", tuple(set_1), "//", set_1)

# set() 转换为集合
# 集合set自动去重
# 列表->集合
list_1 = [1, 1, 1, 2, 3]
print(type(set(list_1)), "//", set(list_1), "//", list_1)
# 元组->集合
tuple_1 = (55, 55, 55, 66, 77)
print(type(set(tuple_1)), "//", set(tuple_1), "//", tuple_1)

# 字典dict 无法转换
dt = {'name': 'Tom', 'age': 18}
print(type(dt))
