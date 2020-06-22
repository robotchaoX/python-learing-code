# 元组常用方法

# 元组里数据的类型可以不同
employee_tuple = ("zhangsan", 18, 1.75, True)
print(type(employee_tuple))
print("元组 = ", employee_tuple)

# [下标] 取值
tuple_value = employee_tuple[2]
print("指定元素的值: %d" % tuple_value)

# index 按值取索引
tuple_index = employee_tuple.index("zhangsan")
print("指定元素下标: %d " % tuple_index)

# count 统计元素个数
tuple_count = employee_tuple.count("zhangsan")
print("指定元素个数: %d " % tuple_count)

# len 元组元素总个数
tuple_len = len(employee_tuple)
print("元组的个数: %d " % tuple_len)


# 元组数据修改
# 无法修改元组的数据
tp1 = ("aa", "bb", "cc")
# tp1[1] = "BBBB"  # 无法修改元组的数据

# 元组内嵌套的列表中的数据可以被修改
tp2 = (10, 20, 30, ["aa", "bb", "cc"])
tp2[3][1] = "BBBB"  # 可以修改元组内嵌套的列表中的数据
print(tp2)
