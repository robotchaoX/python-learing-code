# 导入模块时，从上到下模块中可执行的语句都会被执行
print("我是模块开始，立即执行")


def say_hello():
    print("你好")


# 可执行语句
print("可执行语句调用函数say_hello()")
say_hello()


print("我是模块末尾")
