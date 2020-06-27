# 不推荐
# 一次导入全部函数等
from _01_测试模块1 import *
# 后导入的会覆盖之前导入的同名函数
from _02_测试模块2 import *


# 后导入的会覆盖之前导入的同名函数
say_hello()  # 重名覆盖
print(title)  # 重名覆盖


# _01_测试模块1 的类
wangcai = Dog()
print(wangcai)
# _02_测试模块2 的类
tom = Cat()
print(tom)
