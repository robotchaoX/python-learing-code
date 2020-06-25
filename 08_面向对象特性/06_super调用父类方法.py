# 父类
class Animal():
    # 公有方法
    def eat(self):
        print("Animal: eat")

    # 私有方法
    def __move(self):
        print("Animal私有: __move")


# 子类
# 子类继承父类的所有属性和方法
# class 子类名(父类名):
class Dog(Animal):  # 继承
    def shake(self):
        print("Dog: 摇尾巴")

    def bark(self):
        print("Dog: bark汪汪叫")

    # 私有方法
    def __jump(self):
        print("Dog私有: __jump")


# 子类的子类
# 子类继承父类的所有属性和方法
# class 子类名(父类名):
class XiaoTianQuan(Dog):  # 继承
    # 重写父类方法
    def bark(self):  # 覆盖 # 方法重写(定义一个跟父类同名的方法,覆盖父类的方法)
        print("方法重写,拓展: 叫得跟神一样")  # 子类的特殊需求(拓展父类的方法)

        # * 调用父类方法
        # 使用 super() 调用父类方法
        # 1.super().父类方法()
        super().bark()  # 调用父类中被重写方法,(继承父类的方法)

        # 2.super(类名, self).父类方法()
        super(XiaoTianQuan, self).bark()  # 写法,作用同上

        # 3.父类名.方法名(self) 调用父类的方法, python2.x 中
        Dog.bark(self)  # 不推荐

        # 注意：如果使用子类调用方法，会出现递归调用 - 死循环！
        # XiaoTianQuan.bark(self) # 递归,死循环

        # 增加其他子类的代码
        print("$%^*%^$%^#%$%")

        # super调用 父类 中的其他方法
        super().shake()
        # super调用 父类的父类 的方法(继承的传递性)
        super().eat()
        # super().super().eat()  # error

        # 子类不能直接访问父类的私有属性和方法
        # super也不能调用 父类 的私有属性和方法
        # super().__jump()  # 私有error
        # super也不能调用 父类的父类 私有属性和方法
        # super().__move()  # 私有error

        # super 不能调用当前类内方法
        # super().__fly()

        # 类内可以访问类内的私有属性和私有方法
        self.__fly()
        # 类内不能直接访问父类的私有属性和私有方法(父类算类外)
        # self.__jump()

    def __fly(self):
        print("XiaoTianQuan私有: __fly")


xtq = XiaoTianQuan()

# 如果子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()

# 类外部不能直接访问类的私有属性和私有方法
# xtq.__fly()
# 类外部不能直接访问父类的私有属性和私有方法
# xtq.__jump()
# 类外部不能直接访问父类的父类的私有属性和私有方法
# xtq.__move()
