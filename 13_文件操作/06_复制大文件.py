#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ----------------------------------------------------------
#     Project  :   文件操作
#     File     :   _05_复制文件.py
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
file1_read = open("README")  # 只读打开
file1_write = open("readme_副本", "w")  # 只写打开

# 读 写
while True:
    # 读取一行内容
    text_line = file1_read.readline()
    if not text_line:
        break
    file1_write.writelines(text_line)  # 连续write写多次是追加写

# 关闭
file1_read.close()
file1_write.close()
