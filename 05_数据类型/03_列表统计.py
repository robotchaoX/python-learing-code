name_list = ["zhangsan", "lisi", "wangwu", "zhangsan"]

list_len = len(name_list)  # 数组元素的个数

print("列表中包含 %d 个元素" % list_len)

count = name_list.count("zhangsan")  # 统计元素出现的个数
print("zhangsan出现了 %d 次" % count)

name_list.remove("zhangsan")
print(name_list)

