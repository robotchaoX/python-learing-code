from _01_测试模块1 import say_hello
# from _02_测试模块2 import say_hello  # 重名覆盖
# import导入的模块内有重名会覆盖之前的,可以起别名区分
from _02_测试模块2 import say_hello as module2_say_hello  # 起别名区分重名

say_hello()
module2_say_hello()
