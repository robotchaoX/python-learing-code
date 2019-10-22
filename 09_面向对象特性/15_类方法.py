"""
__title__ = ''
__author__ = 'chao'
__mtime__ = '18-12-7'
__version__=''
__packages__=','
__description__=''
"""


class Tool(object):
    count = 0  # 类属性

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name
        # cls.count += 1  # cls 只能在@classmethod类内
        # self.count += 1  # self 不能访问cls.类属性 # self.count 创建对象属性
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
Tool.show_tool_count()

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
