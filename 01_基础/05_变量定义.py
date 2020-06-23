# 定义变量,不需要声明,不需要类型
# 先定义,后使用

# 定义一个变量,自动推导类型
name = "Tom"

# 已定义的变量,啥也不干
name  # 没有影响

# 在控制台输出变量的信息
print(name)  # 输出变量


# 定义苹果的单价
price = 8.5  # 自动推导类型

# 定义购买数量
weight = 7.5

# 计算金额
money = price * weight

# 只要买苹果返5块
money = money - 5

print("money=", money)
