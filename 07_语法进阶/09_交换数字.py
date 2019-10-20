a = 100
b = 6

# 利用中间变量
c = a
a = b
b = c
print(a,b)

# 自加减
a = 100
b = 6
a = a +b
b = a - b
a = a - b
print(a, b)

a = 100
b = 6
# 利用元组
a, b = (b, a)
# a, b = b, a  # 省略小括号
print(a, b)
