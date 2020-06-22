employ_tuple = ("zhangsan", 18, 1.75)
print(employ_tuple)

# 使用格式字符串拼接 element 这个变量不方便！
# 因为元组中通常保存的数据类型是不同的！
# 使用 for in 迭代遍历元组
for elem in employ_tuple:
    print(elem)


print("---------------------")


# while: 遍历列表
employ_tuple = ("zhangsan", 18, 1.75)
i = 0
while i < len(employ_tuple):
    # name_list[i] 列表下标
    print(employ_tuple[i])
    i += 1
