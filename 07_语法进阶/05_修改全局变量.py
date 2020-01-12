# 全局变量
# global num = 10 # 错误,函数内用时声明
num = 10
print("num : ", num)


def demo1():
    # 希望修改全局变量的值 - 使用 global 声明一下变量即可
    # global 关键字会告诉解释器后面的变量是一个全局变量
    # 再使用赋值语句时，就不会创建局部变量
    global num  # 函数内用时,必须声明要使用全局变量
    num = 99
    print("demo1 ==> %d" % num)


def demo2():
    print("demo2 ==> %d" % num)


demo1()
demo2()
