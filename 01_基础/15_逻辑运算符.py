# python关系运算符与c++不相同
# 逻辑运算符: and, or, not
# 返回值: True False

a = 1
b = 2
c = 3

# and 与
print(a < b and b < c)

# or 或
print(a < b or b < c)

# not 非
print(not(a < b))


# 定义一个整数变量 age，编写代码判断年龄是否正确
# 要求人的年龄在 0-100 之间

age = 12
# and 与
if age >= 0 and age <= 100:
    print("and 年龄正确")
else:
    print("and 年龄不正确")

age = 150
# python 可像数学式一样直接连写,c++不可以
if 0 <= age <= 100:
    print("0 <= age <= 100 年龄正确")
else:
    print("0 <= age <= 100 年龄不正确")
