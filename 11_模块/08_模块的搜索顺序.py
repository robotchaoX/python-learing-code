# 本地包不可与系统包重名,会覆盖系统包
# 先搜索当前目录再搜索系统目录
import random  # 避免与系统文件重名

# __file__ 输出包文件的路径
print(random.__file__)

# 使用模块
rand = random.randint(0, 10)
print(rand)
