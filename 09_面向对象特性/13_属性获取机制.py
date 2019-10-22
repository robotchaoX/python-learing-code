"""
__title__ = ''
__author__ = 'chao'
__mtime__ = '18-12-7'
__version__=''
__packages__=','
__description__=''
"""


class Tool(object):
    # 使用复制语句定义类属性
    count = 0

    def __init__(self, name):
        self.name = name  # 实例属性

        # 让类属性值+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")
# 输出工具对象的总数
print("向上查找类属性 %s" % tool3.count)


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
