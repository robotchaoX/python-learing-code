# del 关键字本质上是将一个变量从内存中删除的
name = "Tom"
del name  # 删除变量
# 注意：如果使用 del 关键字将变量从内存中删除，后续的代码就不能再使用这个变量了
print(name)  # NameError: name 'name' is not defined


name_list = ["张三", "李四", "王五"]

# del 删除列表元素
# 提示：在日常开发中，要从列表删除数据，建议使用列表提供的方法
del name_list[1]  # 删除指定下标的值,不推荐
print(name_list)
