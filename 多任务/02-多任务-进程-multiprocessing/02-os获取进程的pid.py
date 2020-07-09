# 进程库 multiprocessing
import multiprocessing
import os
import time


# 子进程的函数
def test():
    for i in range(5):
        # os.getpid() 子进程
        # os.getppid() 父进程
        print("----in 子进程 pid=%d ,父进程的pid=%d---" % (os.getpid(), os.getppid()))
        time.sleep(1)


def main():
    # os.getpid() 当前进程
    # os.getppid() 当前进程的父进程
    print("主进程 pid=%d，主进程的父进程pid=%d" % (os.getpid(), os.getppid()))

    # 创建多进程
    # 仅创建子进程对象
    p = multiprocessing.Process(target=test)

    # 子进程开始执行，创建子进程
    p.start()


if __name__ == "__main__":
    main()
