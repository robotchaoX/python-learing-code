# 字典 {key:value}  键值对key:value  各个键值对逗号,隔开
# 字典 是一个 无序 的数据集合，key必须是字符串
# 使用print函数输出字典时，通常输出的顺序和定义的顺序是不一致的
dict1 = {
    "name": "张三",  # 键:值对
    "age": 18,
    "height": 1.75}
print(type(dict1))
print(dict1)  # 无序排列,每次输出顺序不同??

# 空字典
dict2 = {}
print(type(dict2))
print(dict2)

# dict()函数创建空字典
dict3 = dict()  # dict()系统函数
print(type(dict3))
print(dict3)
