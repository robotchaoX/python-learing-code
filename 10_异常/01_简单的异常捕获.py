#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ----------------------------------------------------------
#    Project  :  10_异常
#    File     :  _01_简单的异常捕获.py
#    Author   :  chao
#    Date     :  18-12-9
# Description :  简单
# ----------------------------------------------------------

# 异常处理 try:--except:--
try:  # 不能确定能否正常执行的代码
    num = int(input("请输入一个整数:"))
except:  # 处理异常问题
    print("请输入正确的整数")

print("-" * 50)

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
