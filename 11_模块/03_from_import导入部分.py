# from模块导入函数
from _01_测试模块1 import say_hello
from _01_测试模块1 import title
# 导入会覆盖前面导入的同名的函数
# from _02_测试模块2 import say_hello  # 重名覆盖
# 导入功能取别名
from _02_测试模块2 import say_bye as module2_say_bye
from _02_测试模块2 import Cat


# _01_测试模块1的函数
say_hello()
print(title)

# _02_测试模块2 的类
tom = Cat()
print(tom)

# 函数别名
module2_say_bye()
