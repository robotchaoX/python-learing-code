# 遍历列表

# for in : 迭代遍历列表
name_list = ["zhangsan", "lisi", 0.3, "xiaozhao"]
for elem in name_list:
    # print("我的名字叫 %s " % name)
    print(elem)

print("---------------------")


# while: 遍历列表
name_list = ["zhangsan", "lisi", 0.3, "xiaozhao"]
i = 0
while i < len(name_list):
    # name_list[i] 列表下标
    print(name_list[i])
    i += 1
