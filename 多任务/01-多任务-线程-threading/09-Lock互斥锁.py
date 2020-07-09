# 线程库 threading
import threading
import time


# 子线程回调函数
def test1(num):
    global g_num
    # 上锁，如果之前没有被上锁，那么此时 上锁成功
    # 如果上锁之前 已经被上锁了，那么此时会堵塞在这里，直到 这个锁被解开位置
    mutex.acquire()
    for i in range(num):
        # 修改全局变量
        g_num += 1  # +不是原子操作
    # 解锁
    mutex.release()
    print("-----in test1 g_num=%d----" % g_num)


# 子线程回调函数
def test2(num):
    global g_num
    # 上锁
    mutex.acquire()
    for i in range(num):
        # 修改全局变量
        g_num += 1
    # 解锁
    mutex.release()
    print("-----in test2 g_num=%d=----" % g_num)


# 定义全局变量
g_num = 0

# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def main():
    print("in main Thread g_num = %d" % g_num)

    # 创建子线程对象，传参
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    # 开始子线程
    t1.start()
    t2.start()

    # 等待上面的2个线程执行完毕....
    time.sleep(2)

    print("in main Thread g_num = %d" % g_num)


if __name__ == "__main__":
    main()
