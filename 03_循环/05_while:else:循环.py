# 打印 5 遍 Hello Python

# 1. 定义一个整数变量，记录循环次数
i = 0

# 2. 开始循环
while i < 5:  # 0 开始 < 判断
    # 1> 希望在循环内执行的代码
    print("Hello Python")
    # 2> 处理计数器
    i += 1
# while正常结束循环才会执行else语句,否则跳过,不执行,
# while中间有break退出,则不执行else语句
# while中间有continue是正常结束,执行else语句
else:
    # 3. 正常结束循环才会执行else语句
    print("正常结束循环才会执行else语句，i = %d" % i)

# 4. 观察一下，循环结束后，计数器 i 的数值是多少
print("循环结束后，i = %d" % i)
