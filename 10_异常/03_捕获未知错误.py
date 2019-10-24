#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ----------------------------------------------------------
#     Project  :   10_异常
#     File     :   _03_捕获未知错误.py
#     Author   :   chao
#     Date     :   18-12-9 
#  Description :
# ----------------------------------------------------------

try:
    num = int(input("输入一个整数:"))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数!")
except Exception as error:
    print("未知错误: %s" % error)

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
