# 进程库 multiprocessing
import multiprocessing
# import threading
import time


# 子进程回调函数
def sing():
    """唱歌 5秒钟"""
    for i in range(5):
        print("----正在唱歌---%d---" % i)
        time.sleep(1)


# 子进程回调函数
def dance():
    """跳舞 5秒钟"""
    for i in range(5):
        print("----正在跳舞---%d---" % i)
        time.sleep(1)


def main():
    # # 创建多线程
    # t1 = threading.Thread(target=test1)
    # t2 = threading.Thread(target=test2)
    # t1.start()
    # t2.start()

    # 创建多进程
    # 仅创建子进程对象
    p1 = multiprocessing.Process(target=sing)
    p2 = multiprocessing.Process(target=dance)

    # 子进程开始执行，创建子进程
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
