#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ----------------------------------------------------------
#     Project  :   文件操作
#     File     :   _01_读取文件.py
#     Author   :   chao
#     Date     :   18-12-12 
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

# 1 打开文件
file1 = open("README")

# 2 读取文件
text1 = file1.read()
print(text1)

# 3 写入文件

# 4 关闭文件
file1.close()
