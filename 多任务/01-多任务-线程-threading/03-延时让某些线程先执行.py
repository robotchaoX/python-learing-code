# 线程库 threading
import threading
import time


def sing():
    """唱歌 5秒钟"""
    for i in range(5):
        print("----正在唱歌---%d---" % i)
        time.sleep(1)


def dance():
    """跳舞 5秒钟"""
    for i in range(5):
        print("----正在跳舞---%d---" % i)
        time.sleep(1)


def main():
    # 仅创建子线程对象
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    # 通过延时决定谁先执行
    t1.start()
    time.sleep(1)
    print("---1---")

    t2.start()
    time.sleep(1)
    print("---2---")

    # 打印所有运行线程信息
    print(threading.enumerate())


if __name__ == "__main__":
    main()
