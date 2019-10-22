"""
__title__ = ''
__author__ = 'chao'
__mtime__ = '18-12-7'
__version__=''
__packages__=','
__description__=''
"""


class A():
    def aa(self):
        print("A -- aa")

    def bb(self):
        print("A -- aa")


class B:
    def aa(self):
        print("B -- bb")

    def bb(self):
        print("B -- bb")


# 多继承
# class C(A, B):
class C(B, A):
    pass


# 创建子类对象
c = C()
c.aa()
c.bb()

print(C.__mro__)


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
