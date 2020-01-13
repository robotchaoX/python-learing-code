#! /usr/bin/env python
# -*- coding:utf-8 -*-


class MusicPlayer(object):
    # 记录第一个被创建的对象的地址
    instance = None  # 类属性

    # 记录是否被执行过初始化动作
    init_flag = False  # 利用flag标记实现只初始化一次

    def __new__(cls, *args, **kwargs):  # 重写__new__方法
        # 判断属性是否为空对象
        if cls.instance is None:
            # 调用父类的方法为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回类属性保存的对象
        # 实现多个对象共用同一地址(单例)
        return cls.instance

    def __init__(self):  # 每次创建对象时都会进行__init__初始化
        # 判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return  # 初始化过了就直接返回
        # 如果没有执行过,在执行初始化动作
        print("__init__初始化播放器")
        # 修改类属性标记
        MusicPlayer.init_flag = True


# 创建多个对象,共用同一地址
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
