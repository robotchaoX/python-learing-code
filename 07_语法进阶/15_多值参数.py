# 参数个数不确定
# *元组参数, **字典参数
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


# 元组()直接逗号分隔,字典{}key=value
demo(99, 1, 2, 3, name="小明", age=18)
