# 线程库 threading
import threading
import time

# 定义一个全局变量
g_num = 0


def test1(num):
    global g_num
    print("-----in test1 g_num=%d----" % g_num)
    for i in range(num):
        # 上锁
        mutex.acquire()
        g_num += 1  # 修改全局变量
        # 解锁
        mutex.release()
    print("-----in test1 g_num=%d----" % g_num)  # 全局变量（两个函数修改的共同结果）

# 锁的粒度过小，每个循环都需要抢锁


def test2(num):
    global g_num
    print("-----in test1 g_num=%d----" % g_num)
    for i in range(num):
        # 上锁
        mutex.acquire()
        g_num += 1  # 修改全局变量
        # 解锁
        mutex.release()
    print("-----in test2 g_num=%d=----" % g_num)


# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def main():
    print("in main Thread g_num = %d" % g_num)

    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()

    # 等待上面的2个线程执行完毕....
    time.sleep(2)

    print("in main Thread g_num = %d" % g_num)


if __name__ == "__main__":
    main()
