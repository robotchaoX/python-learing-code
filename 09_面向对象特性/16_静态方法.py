#!/usr/bin/env python
# coding:utf-8


class Dog(object):
    # 静态方法,不访问实例属性/类属性,与C++静态含义不同
    @staticmethod  # 静态方法,可以被实例调用 实例.静态方法 , 可以被类调用 类名.静态方法
    def run():  # 不需要self , 静态方法不访问实例属性/类方法
        print("小狗要跑...")


# 通过类名.调用静态方法 - 不需要创建对象
Dog.run()  # 可被类调用 类名.静态方法

# 创建对象
wangcai = Dog()
wangcai.run()  # 可被实例调用 实例.静态方法
