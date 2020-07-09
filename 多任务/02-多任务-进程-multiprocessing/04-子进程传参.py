# 进程库 multiprocessing
import multiprocessing
import os
import time


# 子线程传参，形参，不定长参数，字典
def test(a, b, c, *args, **kwargs):
    print("----in 子进程1 pid=%d ,父进程的pid=%d---" %
          (os.getpid(), os.getppid()))
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
    time.sleep(1)


def main():
    print("主进程 pid=%d，主进程的父进程pid=%d" % (os.getpid(), os.getppid()))

    # 子进程传参
    # target指定 线程执行的函数  # target=函数名
    # args指定 调用函数时传递的参数  # args=元组
    p = multiprocessing.Process(target=test, args=(
        "aa", "bb", "cc", 44, 55, 66, 77, 88), kwargs={"mm": 11})
    p.start()


if __name__ == "__main__":
    main()
