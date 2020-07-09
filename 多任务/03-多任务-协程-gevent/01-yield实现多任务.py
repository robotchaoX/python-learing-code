import time


# 函数中有yield语句，这个就不再是函数，而是一个生成器的模板
def task_1():
    while True:
        print("---1----")
        time.sleep(0.1)
        yield  # yield暂停执行时返回空


# 函数中有yield语句，这个就不再是函数，而是一个生成器的模板
def task_2():
    while True:
        print("---2----")
        time.sleep(0.1)
        yield  # yield暂停执行时返回空


def main():
    # 如果在调用create_num的时候，发现这个函数中有yield那么此时，
    # 不是调用函数，而是创建一个生成器对象
    # 创建生成器对象
    t1 = task_1()
    t2 = task_2()

    # 先让t1运行一会，当t1中遇到yield的时候，再返回到24行，然后
    # 执行t2，当它遇到yield的时候，再次切换到t1中
    # 这样t1/t2/t1/t2的交替运行，最终实现了多任务....协程
    while True:
        # next生成数据
        next(t1)
        next(t2)


if __name__ == "__main__":
    main()
