#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ----------------------------------------------------------
#   Project :  09_面向对象特性
#   File    :  _18___new__方法.py
#   Author  :  chao
#   Date    :  18-12-8 
# ----------------------------------------------------------
"""
Description:
"""


class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        # 创建对象时,__new__方法会被自动调用
        print("创建对象,__new__方法,分配空间")
        # 分配空间,返回对象地址
        return super().__new__(cls)  # 语法固定 , 必须cls参数
        # return super(MusicPlayer, self).__new__()  # 语法错误

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
wangyiyun = MusicPlayer()
print(wangyiyun)
kugou = MusicPlayer()
print(kugou)


"""
code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃   神兽保佑   ┣┓
                ┃ 　永无BUG！  ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
