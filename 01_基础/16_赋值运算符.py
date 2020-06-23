# 单变量赋值
num = 1
print(num)

# 多变量赋相同值
a = b = 100
print(a)
print(b)

# 多变量赋值
num1, float1, str1 = 10, 0.5, 'hello'
print(num1)
print(float1)
print(str1)

# 复合赋值运算符
# +=, -=, *=, /=, //=, %=, **=
cnt = 0
cnt += 1
print(cnt)

# 注意: 复合运算符的右侧是整体
num1 = num2 = 1
num1 *= 1 + 2
num2 *= (1 + 2)  # 等效
print(num1)
print(num2)
