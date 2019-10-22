#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------
#   Project :  09_面向对象特性
#   File    :  _17_方法综合.py
#   Author  :  chao
#   Date    :  18-12-7 下午5:32
# ---------------------------------------------------



class Dog(object):
    @staticmethod  # 静态方法,可以被实例调用 实例.静态方法 , 可以被类调用 类名.静态方法
    def run():  # 不需要self , 静态方法不访问实例属性/类方法
        print("小狗要跑...")


wangcai = Dog()
wangcai.run()  # 可被实例调用 实例.静态方法
Dog.run()  # 可被类调用 类名.静态方法


"""
# code is far away from bugs with the god animal protecting
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
