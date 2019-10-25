#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ----------------------------------------------------------
#     Project  :   文件操作
#     File     :   _04_分行读取文件.py
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

# 打开文件
file1 = open("README")

while True:
    # 读取文件
    text1 = file1.readline()
    print(type(text1))
    # 读取到内容末尾退出(空行是\n ,不是空)
    if not text1:
        break
    print(text1)

# 关闭文件
file1.close()
