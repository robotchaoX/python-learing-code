# 1 查
name_list = ["zhangsan", "lisi", "wangwu"]
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
print(name_list)

# 3. 增加
name_list = ["zhangsan", "lisi", "wangwu"]
# 3.1 append 向列表的末尾追加数据
name_list.append("王小二")  # 追加
print(name_list)
name_list.append(["赵六", "钱八"])  # 追加列表，整体嵌套
print(name_list)
# 3.2 insert 在列表的指定索引位置插入数据
name_list.insert(1, "小美眉")  # 插入
print(name_list)
# 3.3 extend 把其他列表中的完整内容，追加到当前列表的末尾
name_list = ["zhangsan", "lisi", "wangwu", "zhaoliu"]
temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)
name_list.extend("ABC")  # 字符串也是列表，将字符串拆开一个个字符追加
print(name_list)
# 3.4 += 等价extend方法
num_list = [1, 2, 3]
print("id=", id(num_list), num_list)
# 列表变量使用 += 不会做相加再赋值的操作 ！
# 本质上是在调用列表的 extend 方法
# 列表的 += 等价extend方法,不是list=list+list,与数值不一样
num_list += num_list  # 等价extend方法
print("id=", id(num_list), num_list)
num_list.extend(num_list)  # 等价 +=
# 3.5 + 方法
num_list = [1, 2, 3]
print("id=", id(num_list), num_list)
num_list = num_list + num_list  # 新建同名变量???
print("id=", id(num_list), num_list)
# 3.5 * 方法
num_list = [1, 2, 3]
print("id=", id(num_list), num_list)
num_list = num_list * 3  # 新建同名变量???
print("id=", id(num_list), num_list)

# 4. 删除
name_list = ["zhangsan", "张三", "wangwu", "张三"]
# 4.1 remove 方法可以从列表中删除指定的数据,只删第一个，如果数据不存在，程序会报错
name_list.remove("张三")  # 按值删 # 只删第一个
print(name_list)
# 4.2 pop 方法可以指定要删除元素的索引，返回被删除的值
ret = name_list.pop(1)  # 按下标删
print(ret)
print(name_list)
# 4.2 pop 方法默认可以把列表中最后一个元素删除
ret = name_list.pop()
print(ret)
print(name_list)
# 4.3 clear 方法可以清空列表
name_list.clear()  # 清空
print(name_list)


# copy 复制
name_list = ["zhangsan", "lisi", "wangwu"]
name_li2 = name_list.copy()
print(name_list)
print(name_li2)

# 列表嵌套
# [ [],[],[] ]
name_list = [["zhangsan", "lisi", "wangwu"],
             ["张三", "李四", "王五"],
             ["孙悟空", "猪二哥", "沙师弟"]]
print(name_list)
print(name_list[1])
print(name_list[1][2])
