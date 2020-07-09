# 进程库 multiprocessing
import multiprocessing
import os
import time


def test1():
    print("--1--in 子进程1 pid=%d ,父进程的pid=%d---" %
          (os.getpid(), os.getppid()))
    time.sleep(3)
    print("--1--子进程test1-end")


def test2():
    print("--2--in 子进程2 pid=%d ,父进程的pid=%d---" %
          (os.getpid(), os.getppid()))
    time.sleep(3)
    print("--2--子进程test2-end")


def main():
    print("++主进程 pid=%d，主进程的父进程pid=%d" % (os.getpid(), os.getppid()))

    # 子进程1
    p1 = multiprocessing.Process(target=test1)
    p1.start()

    # join主进程阻塞等待子进程1结束
    p1.join()
    print("----join")

    # 子进程2
    p2 = multiprocessing.Process(target=test2)
    p2.start()

    # 主进程结束，子进程2还未结束
    print("++主进程 pid=%d，主进程的父进程pid=%d" % (os.getpid(), os.getppid()))


if __name__ == "__main__":
    main()
