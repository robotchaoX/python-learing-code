# from xx import * 仅允许导入__all__列表的内容
from _06___all__模块 import *  # 导入__all__列表的内容


# 使用模块
# __all__列表中包含的，被导入了
# 函数
say_hello()
# 变量
print(title)


# __all__列表中没有包含，没有被导入，不能调用
# 函数
# say_bye()
# 类
# pq = Pig()
# print(pq)
