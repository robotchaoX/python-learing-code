# 线程库 threading
import threading
import time


# 子线程回调函数
def sing():
    """唱歌 5秒钟"""
    for i in range(5):
        print("----正在唱歌---%d---" % i)
        time.sleep(1)
        # 打印所有运行线程信息
        # print(threading.enumerate())


# 子线程回调函数
def dance():
    """跳舞 5秒钟"""
    for i in range(5):
        print("----正在跳舞---%d---" % i)
        time.sleep(1)


def main():
    # 创建多线程
    # 仅创建子线程对象
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    # 子线程开始执行，创建子线程
    # 子线程谁先执行顺序不定
    t1.start()
    t2.start()

    # 打印所有运行线程信息
    print(threading.enumerate())

    # 主线程等待子线程结束
    # python主线程自动等待子线程结束，不需要c++的join阻塞等待回收


if __name__ == "__main__":
    main()
