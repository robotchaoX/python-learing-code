#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ----------------------------------------------------------
#     Project  :   文件操作
#     File     :   _03_写入文件.py
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

# 打开方式, r 只读(默认), w 只写(覆盖), a 追加
#           r+只读(头开始读全部,追加), w+只写(末尾开始读,读不到?,覆盖), a+追加(末尾开始读,读不到?,追加)
file1 = open("README", "r+")

# 读入
txt_line = file1.readline()
print(txt_line)
text1 = file1.read()
print(text1)  # w+ a+方式打开的,读入为空?
print(len(text1))

# 写入,可以使用 转义字符 \n
file1.write("\n123456写入")
file1.write("\n123456写入")  # 连续write写是追加

# 关闭
file1.close()
