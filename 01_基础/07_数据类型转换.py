# 基本数据类型 整型:int
#            浮点型:float 没有double
#            布尔:bool ,值 True False
# 高级数据类型 字符串:str
#            列表:list
#            元组:tuple
#            集合:set
#            字典:dict


# 整型:int()
float1 = 3.94
str1 = "44"
print(type(int(float1)), int(float1), float1)  # 去除小数,损失精度
print(type(int(str1)), int(str1))  # 字面意

# 浮点型:float()
int1 = 1
str1 = "55"
print(type(float(int1)), float(int1), int1)  # float(int1)单次转换,不会影响原值
print(type(float(str1)), float(str1))

# 布尔:bool() ，真 True ,假 False
flag = 2  # 真
print(type(bool(flag)), bool(flag), flag)

# 字符串:str()
int1 = 6
print(type(str(int1)), str(int1), int1)


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


# eval() 将字符串转换为有效对象
str1 = "1"
str2 = "1.1"
str3 = "[1, 2, 3]"
str4 = "(10, 20, 30)"
str5 = "{100, 200, 300}"
print(type(eval(str1)), str1)
print(type(eval(str2)), str2)
print(type(eval(str3)), str3)
print(type(eval(str4)), str4)
print(type(eval(str5)), str5)
