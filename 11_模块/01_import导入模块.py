# 模块就是python文件


# 导入模块
import _01_测试模块1
import _02_测试模块2

# 重复导入,不报错
import _01_测试模块1
import _02_测试模块2

# 使用模块
# 函数
_01_测试模块1.say_hello()
_02_测试模块2.say_hello()

# 变量
print(_01_测试模块1.title)
print(_02_测试模块2.title)

# 类
dog = _01_测试模块1.Dog()
print(dog)
cat = _02_测试模块2.Cat()
print(cat)
