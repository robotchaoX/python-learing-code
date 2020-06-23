# 从第一行开始执行,跳过函数定义
print("从第一行开始执行,跳过函数定义")


print("跳过函数定义")
# Python 解释器知道下方定义了一个函数,跳过函数定义
def say_hello():
    """打招呼"""
    print("hello 1")
    print("hello 2")
    print("hello 3")


# 变量
name = "小明"


# 只有在程序中，主动调用函数，才会让函数执行，否则不执行
say_hello()
