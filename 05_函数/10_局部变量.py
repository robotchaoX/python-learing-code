# 局部变量


def demo1():
    # 局部变量
    num_local = 10
    # 函数体内部访问
    print("demo1 ==> %d" % num_local)


demo1()
# 函数外部无法访问局部变量
# print("demo1 ==> %d" % num_local)


def demo2():
    # 局部变量
    num_local = 99  # 同名 局部变量 互不影响
    print("demo2 ==> %d" % num_local)


# 同名 局部变量 互不影响
demo2()
