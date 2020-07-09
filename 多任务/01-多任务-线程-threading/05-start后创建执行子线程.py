# 线程库 threading
import threading
import time


def test1():
    for i in range(5):
        print("-----test1---%d---" % i)
        time.sleep(1)


def main():
    # 在调用Thread之前先打印当前线程信息
    print(threading.enumerate())  # MainThread
    t1 = threading.Thread(target=test1)  # 只创建子线程对象
    # 在调用Thread之后打印
    print(threading.enumerate())  # MainThread

    t1.start()  # 子线程开始执行，创建子线程
    # 在调用start之后打印
    print(threading.enumerate())  # MainThread,Thread-1


if __name__ == "__main__":
    main()
