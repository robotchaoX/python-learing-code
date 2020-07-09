# 线程库 threading
import threading
import time


# 全局变量
g_nums = [11, 22]  # list可变类型，传引用


# 子线程传参
def test1(temp):  # list可变类型，传引用
    # 修改全局变量
    temp.append(33)
    print("-----in test1 temp=%s----" % str(temp))


# 子线程传参
def test2(temp):  # list可变类型，传引用
    # 查看全局变量
    print("-----in test2 temp=%s----" % str(temp))


# 子线程传参，形参，不定长参数，字典
def test(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


def main():
    print("-----------------------------------")
    # 子线程传参，形参，不定长参数，字典
    t0 = threading.Thread(target=test, args=(
        "aa", "bb", "cc", 111, 222, 333, 444), kwargs={"Tom": 18})
    # 开始子线程
    t0.start()
    time.sleep(1)
    print("-----------------------------------")

    print("-----in main Thread g_nums = %s---" % str(g_nums))

    # 子线程对象
    # target指定 线程执行的函数  # target=函数名
    # args指定 调用函数时传递的参数  # args=元组
    # g_nums列表，可变类型，传引用
    t1 = threading.Thread(target=test1, args=(g_nums,))  # args=元组
    t2 = threading.Thread(target=test2, args=(g_nums,))

    # 开始子线程，修改全局变量
    t1.start()
    time.sleep(1)

    # 开始子线程，查看全局变量
    t2.start()
    time.sleep(1)

    print("-----in main Thread g_nums = %s---" % str(g_nums))


if __name__ == "__main__":
    main()
