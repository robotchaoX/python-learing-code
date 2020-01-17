# 本地包不可与系统包重名,会覆盖系统包
# 先搜索当前目录再搜索系统目录
import random

# __file__ 包文件的路径
print(random.__file__)

rand = random.randint(0, 10)

print(rand)
