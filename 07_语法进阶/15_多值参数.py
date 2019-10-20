# *元组参数, **字典参数
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)

# 元组直接逗号分隔,
demo(99,1,2,3,name="小明",age=18)