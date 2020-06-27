# 定义多个功能，把部分功能添加到__all__列表
# from xx import * 仅允许导入__all__列表的内容
__all__ = ["title", "say_hello"]


# 全局变量
title = "模块3"


# 函数
def say_hello():
    print("我是 %s" % title)


def say_bye():
    print("bye %s" % title)


# 类
class Pig(object):
    pass
