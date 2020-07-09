# 生成器是特殊的迭代器

# 迭代器生成列表
nums_it = [x * 2 for x in range(10)]
print(nums_it)  # 列表 [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 生成器
nums_gen = (x * 2 for x in range(10))
print(nums_gen)  # 生成器对象
for val in nums_gen:
    print(val)
