print("我是模块开头，导入立即执行，当前__name__的值:", __name__)

# 对外模块：全局变量、函数、类
# 注意：直接执行的代码不是向外界提供的工具！


def say_hello():
    print("你好你好，我是 say hello")


# 模块如果主动执行, __name__ 为 __main__
#     如果被调用执行, __name__ 为 _09__name__模块(模块名)
if __name__ == "__main__":
    print(__name__)  # 当直接执行时, __name__ 为 __main__

    # 文件被导入时，能够直接执行的代码不需要被执行！
    print("定义的__main__测试代码")
    say_hello()


print("我是模块末尾，当前__name__的值:", __name__)
