# 1. 输入苹果单价
price_str=input("单价:")
# 2. 重量
weight_str=input("重量:")
# 3. 计算金额
price=float(price_str)
weight = float(weight_str)
money = price * weight
print("金额:",money)
