"""
for 变量 in 列表变量:
    操作
"""

num_list = [1, 2, 3, 4, 5]
# for in : 迭代遍历列表
for elem in num_list:
    print(elem)
# 循环正常结束循环才会执行else语句,否则跳过,不执行,
# 循环中间有break退出,则不执行else语句
# 循环中间有continue是正常结束,执行else语句
else:
    # 3. 正常结束循环才会执行else语句
    print("正常结束循环才会执行else语句，完整遍历,中途break则不会执行else")

print("结束")
