# input输入的类型都是字符串str类型
# 1. 输入苹果的单价
price_str = input("苹果的单价：")
print("input输入的类型都是字符串str:", type(price_str))

# 2. 输入苹果的重量
weight_str = input("苹果的重量：")

# 3. 计算支付的总金额
# 注意：两个字符串变量之间是不能直接用乘法的
# money = price_str * weight_str

# 1> 将str转换成float
price = float(price_str)  # 类型转换
weight = float(weight_str)  # 类型转换

# 2> 用两个小数来计算最终的金额
money = price * weight

print(money)

# input 输入改进
# 1. 单价
price = float(input("单价："))  # 直接类型转换
# 2. 重量
weight = float(input("重量："))  # 直接类型转换
# 3. 金额
money = price * weight
print("金额:", money)
