#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ----------------------------------------------------------
#     Project  :   10_异常
#     File     :   _06_抛出异常.py
#     Author   :   chao
#     Date     :   18-12-9 
#  Description :
# ----------------------------------------------------------
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


def input_password():
    pwd = input("输入密码：")

    if len(pwd) == 8:
        return pwd

    print("抛出异常:")

    # 创建异常对象
    ex_len_error = Exception()  # 创建异常对象，Exception是异常类
    # 抛出异常
    raise ex_len_error

try:
    print(input_password())
except Exception as error:
    print(error)


