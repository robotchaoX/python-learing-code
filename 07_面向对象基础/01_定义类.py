# 定义类
# class 类名():
#       类属性/类方法
#       def 类方法
#       self.类属性


# 定义类
# class Cat: # 经典类 # 没有继承,定义时类名后小括号可以省
# class Cat(object):  # 新式类,默认继承自object
class Cat():  # 新式类,省略object
    """这是一个猫类"""

    # 类方法
    # self指向当前对象,指的是调用该函数的对象
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


# 创建猫对象
tom = Cat()  # 创建对象,类名需要括号

# 调用类方法
tom.drink()
tom.eat()


# 输出类对象内存地址
print(tom)
addr = id(tom)
print("0x%x" % addr)  # %x十六进制
print("%d" % addr)  # 十进制
