# 进程库 multiprocessing
import multiprocessing
import os
import time


# 定义一个全局变量
g_num = [11, 22, 33]


# 修改全局变量
def test1():
    global g_num
    g_num.append(44)
    print("--在进程中1中g_num=%s" % str(g_num))
    time.sleep(3)
    print("--子进程test1-end")


# 查看全局变量
def test2():
    print("--在进程中2中g_num=%s" % str(g_num))
    time.sleep(2)
    print("--子进程test2-end")


def main():
    print("++主进程 pid=%d，主进程的父进程pid=%d" % (os.getpid(), os.getppid()))

    # 子进程1
    p = multiprocessing.Process(target=test1)
    p.start()

    # 主进程阻塞等待子进程1结束
    p.join()
    print("----join")

    # 子进程2
    p2 = multiprocessing.Process(target=test2)
    p2.start()

    # 主进程结束，子进程2还未结束
    print("++主进程 pid=%d，主进程的父进程pid=%d" % (os.getpid(), os.getppid()))


if __name__ == "__main__":
    main()
