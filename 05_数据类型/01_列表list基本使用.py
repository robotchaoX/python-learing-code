name_list = ["zhangsan", "lisi", "wangwu"]

# 1 查
# 1.1 取值
print(name_list[2])  # 取值
# print(name_list[6])  # IndexError: list index out of range - 列表索引超出范围

# 1.2 index 取索引
# 知道数据的内容，想确定数据在列表中的位置
print(name_list.index("wangwu"))  # 取索引
# 如果传递的数据不在列表中，程序会报错！
# print(name_list.index("----"))  # ValueError: '----' is not in list

# 2. 修改
name_list[1] = "李四"
# 列表指定的索引超出范围，程序会报错！
# name_list[6] = "王小二"  # IndexError: list assignment index out of range

# 3. 增加
# 3.1 append 向列表的末尾追加数据
name_list.append("王小二")  # 追加
# 3.2 insert 在列表的指定索引位置插入数据
name_list.insert(1, "小美眉")  # 插入

# 3.3 extend 把其他列表中的完整内容，追加到当前列表的末尾
temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)
print(name_list)

# 4. 删除
# 4.1 remove 方法可以从列表中删除指定的数据
name_list.remove("wangwu")  # 按值删
# 4.2 pop 方法可以指定要删除元素的索引
name_list.pop(3)  # 按下标删
# 4.2 pop 方法默认可以把列表中最后一个元素删除
name_list.pop()
# 4.3 clear 方法可以清空列表
name_list.clear()  # 清空
print(name_list)
