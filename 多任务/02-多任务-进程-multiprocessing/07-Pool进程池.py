# 进程库 multiprocessing
from multiprocessing import Pool
import os
import time
import random


# 子进程，传入参数
def worker(msg):
    # 计时
    t_start = time.time()
    print("%s开始执行,进程号为%d" % (msg, os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print("--%s执行完毕，耗时%0.2f" % (msg, t_stop-t_start))


def main():
    # 定义一个进程池，最大进程数3
    po = Pool(3)  # 工作线程数3，等待任务队列>3

    # 将所有任务加入进程池等待任务队列中
    for argument in range(0, 10):
        # 将所有任务加入进程池等待任务队列中，空闲进程自动调取任务执行
        # Pool().apply_async(要调用的目标函数,(函数参数,))
        po.apply_async(worker, (argument,))  # 传参

    print("----start----")
    # 关闭进程池，关闭后po不再接收新的请求
    po.close()
    # 等待进程池中所有子进程执行完成，必须放在close语句之后
    po.join()
    print("-----end-----")


if __name__ == "__main__":
    main()
