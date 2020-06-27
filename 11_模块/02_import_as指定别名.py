# 模块起别名
# 导入模块,并起别名
import _01_测试模块1 as DogModule
import _02_测试模块2 as CatModule


# 使用模块
# 函数
DogModule.say_hello()
CatModule.say_hello()

# 变量
print(DogModule.title)
print(CatModule.title)

# 类
dog = DogModule.Dog()
print(dog)
cat = CatModule.Cat()
print(cat)
