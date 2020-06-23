import functools

# abs() 取绝对值
abs(-5)  # 5

# round() 四舍五入
round(3.14)  # 3
round(6.9)  # 7


# 第三个参数,函数引用
def sum_num(a, b, fun):
    return fun(a)+fun(b)


# abs取绝对值
result = sum_num(-1, 2, abs)
print(result)
# round四舍五入
result = sum_num(3.14, 6.9, round)
print(result)


# 内置高阶函数
# map
# map(func,lst) 将传入的函数变量func作用到lst变量中的每一个元素,返回map对象
# 列表数据
list1 = [1, 2, 3, 4, 5]


# 作用函数
def func(x):
    return x**2


result = map(func, list1)
print(result)  # map对象
print(list(result))  # 列表


# reduce
# reduce(func,lst)每次func计算的结果继续和序列的下一个元素做累积计算
# 导入模块
# import functools
# 列表数据
list1 = [1, 2, 3, 4, 5]


# 作用函数
def func(a, b):
    return a+b


result = functools.reduce(func, list1)
print(result)


# filter
# filter(func,lst) 过滤序列,过滤掉不符合规则条件的元素,返回filter对象
# 列表数据
list1 = [1, 2, 3, 4, 5]


# 过滤函数
def func(x):
    return x % 2 == 0


result = filter(func, list1)
print(result)  # filter对象
print(list(result))  # 转换为列表
