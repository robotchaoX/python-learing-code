# 线程库 threading
import threading
import time

# 定义一个全局变量
g_num = 100


# 修改全局变量
def test1():
    global g_num
    g_num += 100
    print("-----in test1 g_num = %d----" % g_num)


# 查看全局变量
def test2():
    print("-----in test2 g_num = %d----" % g_num)


def main():
    print("in main Thread g_num = %d" % g_num)

    # 仅创建子线程对象
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    # 子线程开始执行，创建子线程
    t1.start()  # 修改全局变量
    time.sleep(1)

    t2.start()  # 显示全局变量，共享
    time.sleep(1)

    # 线程间共享全局变量
    print("in main Thread g_num = %d" % g_num)


if __name__ == "__main__":
    main()
