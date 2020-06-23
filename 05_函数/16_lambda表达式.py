

# lambda表达式 匿名函数
# lambda 参数列表: 表达式


# 函数实现
def add1(a, b):
    return a+b


result = add(1, 2)
print(result)


# lambda表达式实现
# lambda 参数列表: 表达式
# add2 = lambda a,b:  a+b
# print(add2)  # 函数地址
# print(add2(1,2))  # 函数调用


# 无参数
# fun1 = lambda : 100
# print(fun1())

# 一个参数
# fun2 = lambda a: a*2
# print(fun2(22))

# 两个参数
# fun3 = lambda a,b: a+b
# print(1,2)

# 默认参数
# fun4 = lambda a,b,c=100: a+b+c
# print(fun4(1,2))
# print(fun4(1,2,3))

# 可变参数 *args
# fun5 = lambda *args: args
# print(fun5(10,20,30))

# 可变参数 **kwargs
# fun6 = lambda **kwargs: kwargs
# print(fun6(name="小明",age=18))


# 带判断的lambda
# 三目运算 a if a>b else b
# fun1 = lambda a,b: a if a>b else b
# print(fun1(3,333))
