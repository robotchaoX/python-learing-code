# 不推荐
from _01_测试模块1 import *
from _02_测试模块2 import *  # 重名覆盖

print(title)
say_hello()  # 重名覆盖

wangcai = Dog()
print(wangcai)
