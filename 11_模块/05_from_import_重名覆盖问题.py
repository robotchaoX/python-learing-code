from _01_测试模块1 import say_hello
# 导入会覆盖前面导入的同名的函数
from _02_测试模块2 import say_hello  # 重名覆盖

# 功能起别名
# import导入的模块内有重名会覆盖之前的,可以起别名区分
# 给函数起别名可避免同名覆盖问题 # 起别名区分重名
from _01_测试模块1 import say_bye
from _02_测试模块2 import say_bye as module2_say_bye


# 导入模块重名覆盖
say_hello()  # 模块2 覆盖 模块1

# 起别名区分重名
say_bye()  # 模块1
module2_say_bye()  # 模块2
