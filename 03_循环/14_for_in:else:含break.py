"""
for 变量 in 列表变量:
    操作
"""

num_list = [1, 2, 3, 4, 5]
# for in : 迭代遍历列表
for elem in num_list:
    print(elem)
    if elem == 3:
        print("break退出")
        break
# 循环正常结束循环才会执行else语句,否则跳过,不执行,
# 循环中间有break退出,则不执行else语句
# 循环中间有continue是正常结束,执行else语句
else:
    # 3. 正常结束循环才会执行else语句
    # 如果循环体内部使用break退出了循环
    # else 下方的代码就不会被执
    print("break退出,则不执行else语句,只有正常结束循环才会执行else语句")

print("结束")
