def measure():
    temp = 39
    wetness = 50

    return temp, wetness  # 返回多个变量,元组,小括号省了


# result = measure()
# print(result)
#
# print("temp",result[0])
# print("wetness",result[1])
# 接收元组变量
temp, wetness = measure()
# (temp, wetness) = measure()  #元组,小括号可省,变量可单独使用
print(temp)
print(wetness)


