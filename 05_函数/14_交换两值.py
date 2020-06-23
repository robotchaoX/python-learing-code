

# 不会交换数据？？
# 1 利用中间变量
def swap1(a, b):
    c = a
    a = b
    b = c
    # print(a, b)


# 2 拆包写法
def swap2(a, b):
    # 3 利用元组 -Python 专有
    # 提示：等号右边是一个元组，只是把小括号省略了
    # a, b = (b, a)
    a, b = b, a  # 可省略小括号
    # print(a, b)


# 3 自加减,不使用其他的变量
def swap3(a, b):
    a = a + b
    b = a - b
    a = a - b
    # print(a, b)


x = 100
y = 6
print(x, y)

# 函数调用,无法实现交换数据
swap1(x, y)
print(x, y)

swap2(x, y)
print(x, y)

swap3(x, y)
print(x, y)
