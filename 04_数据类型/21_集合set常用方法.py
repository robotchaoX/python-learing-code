# 集合set,集合数据不能重复
set1 = {10, 20}

# 增加数据
# add 增加单个数据
set1.add(99)  # 位置不定
print(set1)
# 集合自动去重，已经存在，不会增加
set1.add(99)
print(set1)
# add不能追加序列，报错
# set1.add([88, 99])  # 报错
# print(set1)

# update 增加序列数据
set2 = {10, 20}
set2.update([77, 88, 99])
print(set2)
# 集合自动去重，已经存在，不会增加
set2.update([77, 88, 99])
print(set2)
# update不能追加单个数据，报错
# set2.update(99)  # 报错
# print(set2)


# 删除数据
set1 = {10, 20, 30, 40}
# remove 删除指定数据，不存在报错
set1.remove(20)
print(set1)
# 删除的数据不存在，报错
# set1.remove(-20)
# print(set1)

# discord 删除指定数据，不存在不报错
set2 = {10, 20, 30, 40}
set2.discard(20)
print(set2)
# 删除的数据不存在，不报错
set2.discard(-20)  # 不报错
print(set2)

# pop 随机删除数据
set3 = {10, 20, 30, 40}
deled = set3.pop()
print(deled)
print(set3)

# 判断数据是否存在
# in 或 not in ,返回True，False
set1 = {10, 20, 30, 40}
print(10 in set1)
print(10 not in set1)
