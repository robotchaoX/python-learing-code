
# 列表拆包
list1 = ["A", "B", "C"]
gl_A, gl_B, gl_C = list1
print(gl_A, gl_B, gl_C)


# 元组拆包
list1 = ("X", "Y", "Z")
gl_X, gl_Y, gl_Z = list1
print(gl_X, gl_Y, gl_Z)


dict1 = {"Temp": 11, "Wetness": 22}
# 字典拆包
# 拆的是各个键key的值
gl_temp, gl_wetness = dict1  # 拆包
print(gl_temp, gl_wetness)  # key
# value值
print(dict1[gl_temp], dict1[gl_wetness])  # value


# 函数返回值为元组
def measure():
    # print("测量开始...")
    temp = 39
    wetness = 50
    # print("测量结束...")

    # 函数返回的类型是元组，小括号可以省略
    return temp, wetness  # 返回多个变量,元组,小括号省了
    # 返回元组
    # return (temp, wetness)  # 元组


#! 返回值拆包
# 返回值为元组，拆包
gl_temp, gl_wetness = measure()  # 拆包
print(gl_temp)
print(gl_wetness)


# 不定长参数，元组/字典
def demo(*args, **kwargs):
    print(args)
    print(kwargs)
    print("-----")


# 元组变量
gl_tuple = (1, 2, 3)
# 字典变量
gl_dict = {"name": "小明", "age": 18}

#! 参数拆包
# 拆包语法，简化元组变量/字典变量的传递
# *拆包元组变量 ， **拆包字典变量
demo(*gl_tuple, **gl_dict)

# 所有值都传给了 *args 元组，不会拆包
# 变量整体作为元组的一个元素
# ( (1, 2, 3), {'age': 18, 'name': '小明'} )
demo(gl_tuple, gl_dict)  # error

# 一个一个传麻烦
demo(1, 2, 3, name="小明", age=18)
