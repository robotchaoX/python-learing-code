# 导入模块
import _01_测试模块1
import _02_测试模块2

# 使用模块
_01_测试模块1.say_hello()
_02_测试模块2.say_hello()

dog = _01_测试模块1.Dog()
print(dog)

cat = _02_测试模块2.Cat()
print(cat)
