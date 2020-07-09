# 进程库 multiprocessing
import multiprocessing


# 一个进程向Queue中写入数据，另外一个进程从Queue中获取数据，
# 通过Queue完成了 多个需要配合的进程间的数据共享，从而能够 起到 解耦的作用


# 子进程向Queue写入数据
def download_from_web(queue):
    """下载数据"""
    # 模拟从网上下载的数据
    data = [11, 22, 33, 44]

    # put()向队列中写入数据
    for temp in data:
        queue.put(temp)

    print("---下载器已经下载完了数据并且存入到队列中----")


# 子进程从Queue读取数据
def analysis_data(queue):
    """数据处理"""
    waitting_analysis_data = list()
    # get()从队列中获取数据
    while True:
        data = queue.get()
        waitting_analysis_data.append(data)

        if queue.empty():
            break

    # 模拟数据处理
    print(waitting_analysis_data)


def main():
    # 1. 创建一个Queue队列
    que = multiprocessing.Queue()

    # 2. 创建多个进程，将Queue队列的引用当做实参进行传递到里面
    # 子进程向Queue写入数据
    p1 = multiprocessing.Process(target=download_from_web, args=(que,))
    # 子进程从Queue读取数据
    p2 = multiprocessing.Process(target=analysis_data, args=(que,))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
