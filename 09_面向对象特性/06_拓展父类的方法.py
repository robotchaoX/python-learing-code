"""
__title__ = ''
__author__ = 'chao'
__mtime__ = '18-12-6'
__version__=''
__packages__=','
__description__=''
"""


class Animal():
    def eat(self):
        print("Animal: eat")

    def sleep(self):
        print("Animal: sleep")

    def __run(self):
        print("Animal私有: __run")


# class 子类名(父类名):  #子类继承父类的所有属性和方法
class Dog(Animal):
    def shake(self):
        print("Dog: 摇尾巴")

    def __jump(self):
        print("Dog私有: __jump")

    def bark(self):
        print("Dog: bark汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("XiaoTianQuan: fly")

    def __eye(self):
        print("XiaoTianQuan私有: __eye")

    # 当父类的方法不满足子类需求时,可对方法进行重写
    def bark(self):  # 覆盖 # 方法重写(定义一个跟父类同名的方法,覆盖父类的方法)
        super().bark()  # 调用父类中被重写方法,(继承父类的方法)
        super(XiaoTianQuan, self).bark()  # 作用同上???
        super().shake()  # super调用父类中的其他方法
        super().eat()  # super调用父类的父类的方法(继承的传递性)
        # super().__jump()  # super也不能调用父类的私有属性和方法
        # super().__eye() # super 用于调用父类方法,不能同类
        # self.__jump()  # 子类不能直接访问父类的私有属性和方法

        self.__eye()  # 类内可以访问类内的私有属性和私有方法
        # self.__jump()  # 类内不能直接访问父类的私有属性和私有方法(父类算类外)

        # 父类名.方法名(self) 调用父类的方法, python2.x 中
        Dog.bark(self)

        print("方法重写,拓展: 叫得跟神一样")  # 子类的特殊需求(拓展父类的方法)


xtq = XiaoTianQuan()
xtq.bark()
# xtq.__eye()  # 类外部不能直接访问类的私有属性和私有方法
# xtq.__jump()  # 类外部不能直接访问父类的私有属性和私有方法


"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃   神兽保佑   ┣┓
                ┃ 　永无BUG！  ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
