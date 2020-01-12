def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

# demo(gl_nums, gl_dict)  # 所有值都传给了 *args 元组

# 拆包语法，简化元组变量/字典变量的传递
demo(*gl_nums, **gl_dict)  # * / ** 对应

# 一个一个传麻烦
demo(1, 2, 3, name="小明", age=18)
