employee_tuple = ("zhangsan", 18, 1.75, "zhangsan")
print("元组 = ",employee_tuple)

# 取值
tuple_value = employee_tuple[2]
print("指定元素的值: %d" %tuple_value)

# 取索引
tuple_index = employee_tuple.index(1.75)
print("指定元素下标: %d " % tuple_index)

# 统计元素个数
tuple_count = employee_tuple.count("zhangsan")
print("指定元素个数: %d " % tuple_count)

# 元组元素个数
tuple_len = len(employee_tuple)
print("元组的个数: %d " % tuple_len)
