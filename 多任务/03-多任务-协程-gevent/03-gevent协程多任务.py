# 协程 gevent
import gevent
import time


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # 没打补丁，不可直接使用系统time函数
        # time.sleep(0.5)
        gevent.sleep(0.5)


def f22(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)


def f333(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)


# 创建3个协程
# 协程创建后，立即生效，只要遇到延时就立即切换执行
print("----1---")
g1 = gevent.spawn(f1, 2)  # 参数 2
print("----2---")
g2 = gevent.spawn(f22, 3)  # 传参 3
print("----3---")
g3 = gevent.spawn(f333, 6)  # 传参 6
print("----4---")

# join阻塞等待g1结束，延时，协程切换执行
g1.join()
print("----g1.join()----")
g2.join()
print("----g2.join()----")
g3.join()
print("----g3.join()----")

# gevent.sleep(10)
