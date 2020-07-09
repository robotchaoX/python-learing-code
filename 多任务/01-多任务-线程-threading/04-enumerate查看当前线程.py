# 线程库 threading
import threading
import time


def sing():
    """唱歌 5秒钟"""
    for i in range(5):
        print("----正在唱歌---%d---" % i)
        time.sleep(1)
    # 如果创建Thread时执行的函数，运行结束那么意味着 这个子线程结束了....


def dance():
    """跳舞 10秒钟"""
    for i in range(10):
        print("----正在跳舞---%d---" % i)
        time.sleep(1)


def main():
    # 仅创建子线程对象
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    # 子线程开始执行，创建子线程
    # 子线程执行顺序不定
    t1.start()
    t2.start()

    # 主线程打印所有运行线程信息
    while True:
        print(threading.enumerate())
        # 只剩主线程，退出
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)


if __name__ == "__main__":
    main()
