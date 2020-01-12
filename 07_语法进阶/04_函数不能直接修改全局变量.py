# 全局变量
num = 10
print("num : ", num)


# 在 python 中，是不允许直接修改全局变量的值
def demo1():
    # 如果使用赋值语句，会在函数内部，定义一个局部变量
    num = 99  # 重新定义一个同名的局部变量,作用域内覆盖全局变量
    print("demo1 ==> %d" % num)  # 无法直接修改全局变量


def demo2():
    print("demo2 ==> %d" % num)


demo1()
demo2()
