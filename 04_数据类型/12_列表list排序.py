# 列表排序
name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
num_list = [6, 8, 4, 1, 10]


# 升序
name_list.sort()  # 默认升序
num_list.sort()
print(name_list)
print(num_list)


# 降序
name_list.sort(reverse=True)  # 降序
num_list.sort(reverse=True)
print(name_list)
print(num_list)


# 逆序（反转）
name_list.reverse()  # 反序
num_list.reverse()
print(name_list)
print(num_list)
