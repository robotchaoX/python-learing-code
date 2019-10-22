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
        print("aa")


class B:
    def bb(self):
        print("bb")


# 多继承
class C(A, B):
    pass


# 创建子类对象
c = C()
c.aa()
c.bb()

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
