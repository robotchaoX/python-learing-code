# 函数多个返回值
# return返回 元组,列表,字典


def measure():
    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 元组-可以包含多个数据，因此可以使用元组让函数一次返回多个值
    # 如果函数返回的类型是元组，小括号可以省略
    return temp, wetness  # 返回多个变量,元组,小括号省了
    # 元组
    # return (temp, wetness)
    # 列表
    # return [temp, wetness]
    # 字典
    # return {"Temp":temp, "Wetness":wetness}


# 接收元组
result = measure()  # 返回值为一个元组
print(result)

# 需要单独的处理温度或者湿度 - 不方便
print(result[0])
print(result[1])

print("-----------------")

# 如果函数返回的类型是元组，同时希望单独的处理元组中的元素
# 可以使用多个变量，一次接收函数的返回结果
# 注意：使用多个变量接收结果时，变量的个数应该和元组中元素的个数保持一致
# (gl_temp, gl_wetness) = measure()  #返回值为元组,小括号可省,变量可单独使用
gl_temp, gl_wetness = measure()  # 拆包
print(gl_temp)
print(gl_wetness)
