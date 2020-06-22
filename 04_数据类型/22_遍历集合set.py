# 遍历集合

# for in : 迭代遍历集合
set1 = {10, 20, 30, 40}  # 顺序随机
for elem in set1:
    print(elem)  # 访问顺序随机

print("---------------------")


# 不能够while: 遍历集合，因为集合不能[下标]随机访问
# set1 = {10, 20, 30, 40}
# i = 0
# while i < len(set1):
#     print(set1[i])  # set1[i] 下标
#     i += 1
