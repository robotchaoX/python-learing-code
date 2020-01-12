# 1 利用中间变量
def swap1(a, b):
    c = a
    a = b
    b = c
    print(a, b)


# 2 自加减,不使用其他的变量
def swap2(a, b):
    a = a + b
    b = a - b
    a = a - b
    print(a, b)


def swap3(a, b):
    # 3 利用元组 -Python 专有
    # a, b = (b, a)
    # 提示：等号右边是一个元组，只是把小括号省略了
    a, b = (b, a)
    # a, b = b, a  # 可省略小括号
    print(a, b)


x = 100
y = 6
print(x, y)

swap1(x, y)
swap2(x, y)
swap3(x, y)
