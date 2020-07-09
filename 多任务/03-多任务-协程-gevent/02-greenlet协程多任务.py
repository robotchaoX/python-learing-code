# 协程 greenlet
from greenlet import greenlet
import time


# 函数
def test1():
    while True:
        time.sleep(10)
        print("---A--")
        # 切换到gr2中运行
        gr2.switch()  # 每次在此处暂停
        print("---gr2.switch()--")
        time.sleep(10)


# 函数
def test2():
    while True:
        time.sleep(10)
        print("---B--")
        # 切换到gr1中运行
        gr1.switch()  # 每次在此处暂停
        print("---gr1.switch()--")
        time.sleep(10)


print("---------------1-------------")
# greenlet对象
gr1 = greenlet(test1)
gr2 = greenlet(test2)
print("---------------2-------------")


# 切换到gr1中运行
gr1.switch()

print("---main--gr1.switch()--")
