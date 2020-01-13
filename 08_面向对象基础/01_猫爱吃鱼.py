# class Cat():  # 没有继承,定义时类名后小括号可以省
class Cat:  # 没有继承,定义时类名后小括号可以省
    """这是一个猫类"""

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


# 创建猫对象
tom = Cat()

tom.drink()
tom.eat()

print(tom)  # 输出内存地址

addr = id(tom)
print("%d" % addr)
print("0x%x" % addr)  # %x十六进制
