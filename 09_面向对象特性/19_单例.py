#! /usr/bin/env python
# -*- coding:utf-8 -*-


class MusicPlayer(object):
    # 类属性,记录第一个被创建的对象的地址
    instance = None

    def __new__(cls, *args, **kwargs):  # 重写__new__方法
        # 判断属性是否为空对象
        if cls.instance is None:  # 只有第一次创建对象时才分配空间
            # 调用父类的方法为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回类属性保存的对象
        # 实现多个对象共用同一地址(单例)
        return cls.instance  # 返回共用的地址(第一个对象的地址)


# 创建多个对象,共用同一地址
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
