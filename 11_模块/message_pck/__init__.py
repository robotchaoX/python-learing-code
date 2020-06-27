# 新建包
# [new]--[python package]--[输入包名]--[ok]
# 包内部自动创建__init__.py文件，控制包的行为
# 在包文件夹下添加模块


# from 包名 import *
# 必须在包下__init__.py文件里设置__all__列表，添加允许导入的模块
__all__ = ["send", "receive"]
