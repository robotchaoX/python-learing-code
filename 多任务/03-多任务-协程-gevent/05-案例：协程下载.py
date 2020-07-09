# URL请求包
import urllib.request

# 协程 gevent
import gevent
# 打补丁
from gevent import monkey
monkey.patch_all()


# 网络下载图片
def downloadPic(img_name, img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    # joinall 阻塞等待所有协程结束
    gevent.joinall([
        # 任务1，创建协程
        gevent.spawn(downloadPic, "gaokao.gif",
                     "https://www.baidu.com/img/dong_54209c0ff3da32eecc31f340c08a18f6.gif"),
        # 任务2，创建协程
        gevent.spawn(downloadPic, "baidu.png",
                     "https://www.baidu.com/img/flexible/logo/pc/index.png")
    ])


if __name__ == '__main__':
    main()
