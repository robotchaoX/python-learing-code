# 线程库 threading
import threading
import time

# 创建子线程有两种方式：全局函数，继承Thread类


# 子线程回调函数
def smile():
    """微笑 5秒钟"""
    for i in range(5):
        print("++++正在微笑---%d---" % i)
        time.sleep(1)
        # 打印所有运行线程信息
        # print(threading.enumerate())


# 子线程回调函数
def cry():
    """大哭 5秒钟"""
    for i in range(5):
        print("++++正在大哭---%d---" % i)
        time.sleep(1)


# 子线程类
# 必须继承 threading.Thread 类
class MySingThread(threading.Thread):
    # 必须定义 run方法，start会自动调用
    def run(self):
        """唱歌 5秒钟"""
        for i in range(5):
            print("----正在唱歌---%d---" % i)
            time.sleep(1)


# 子线程类
# 必须继承 threading.Thread 类
class MyDanceThread(threading.Thread):
    # 必须定义 run方法，start会自动调用
    def run(self):
        """跳舞 5秒钟"""
        for i in range(5):
            print("----正在跳舞---%d---" % i)
            time.sleep(1)


def main():
    # 仅创建子线程对象
    # 1.全局函数方法创建子线程对象
    t1 = threading.Thread(target=smile)
    t2 = threading.Thread(target=smile)
    # 2.自定义子线程类对象
    t3 = MySingThread()
    t4 = MyDanceThread()

    # 子线程开始执行，创建子线程
    # 子线程谁先执行顺序不定
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # 打印所有运行线程信息
    print(threading.enumerate())

    # 主线程等待子线程结束


if __name__ == "__main__":
    main()
