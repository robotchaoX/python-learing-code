#! /usr/bin/env python
# *-* coding:utf-8 *-*
# ----------------------------------------------------------
#     Project  :   13_文件操作
#     File     :   _08_eval计算器.py
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

# eval() 函数用来执行一个字符串表达式，并返回表达式的值
# eval('2 + 2')
# 返回 4
input_str = input("请输入算数题")
print(eval(input_str))
# 返回表达式计算结果