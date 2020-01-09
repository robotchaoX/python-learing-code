# 定义一个整数变量 age，编写代码判断年龄是否正确
# 要求人的年龄在 0-120 之间

age = 12
if age >= 0 and age <= 120:  # and
    print("and 年龄正确")
else:
    print("and 年龄不正确")

age = 1201
if 0 <= age <= 120:  # python 可像数学式一样直接连写
    print("0 <= age <= 120 年龄正确")
else:
    print("0 <= age <= 120 年龄不正确")
