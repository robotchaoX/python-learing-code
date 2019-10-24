#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ----------------------------------------------------------
#     Project  :   10_异常
#     File     :   _05_异常的传递.py
#     Author   :   chao
#     Date     :   18-12-9 
#  Description :
# ----------------------------------------------------------


def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()


try:
    print(demo2())
except Exception as error:
    print("未知错误：%s" % error)

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
