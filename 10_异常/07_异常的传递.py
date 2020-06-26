def demo1():
    return int(input("输入整数："))


# 嵌套调用函数
def demo_2():
    return demo1()


# 利用异常的传递性，在主程序捕获异常
try:
    res = demo_2()
    print(res)
except Exception as error:
    print("未知错误：%s" % error)
