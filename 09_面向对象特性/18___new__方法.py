#! /usr/bin/env python
# -*- coding:utf-8 -*-


class MusicPlayer(object):
    # 分配空间,返回对象地址
    # 创建对象时,__new__方法会被自动调用
    def __new__(cls, *args, **kwargs):
        print("创建对象时,自动调用__new__方法,分配空间")

        # 为对象分配空间
        instance = super().__new__(cls)

        # 返回对象的引用
        return instance

        # 分配空间,返回对象地址
        # return super().__new__(cls)  # 语法固定 , 必须cls参数
        # return super(MusicPlayer, self).__new__()  # 语法错误

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
wangyiyun = MusicPlayer()
print(wangyiyun)
