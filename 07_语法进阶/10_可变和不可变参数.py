def demo(num, num_list):
    print("---内部函数")
    print("num = %d , id = %d" % (num, id(num)))
    print("num_list = %s , id = %d" % (num_list, id(num_list)))
    # 在函数内部，针对参数使用赋值语句，不会修改到外部的实参变量
    num = 1  # 定义了同名变量??
    num_list = [1, 1, 1]  # 定义了同名变量??
    print("num = ", num, " id = ", id(num))
    print("num_list = ", num_list, " id = %d", id(num_list))
    print("---函数执行完成")


gl_num = 99
gl_num_list = [9, 9, 9]
print("num = %d , id = %d" % (gl_num, id(gl_num)))
print("num_list = %s , id = %d" % (gl_num_list, id(gl_num_list)))
demo(gl_num, gl_num_list)
print("全局变量")
print(gl_num)
print(gl_num_list)

print("-------------------------------1--------------------------------------")


# 参数为不可变对象（数值类型、字符串str、元组tuple），python 通过值传递
def change(val):
    print('---val=', val, " id=", id(val))
    val += 10  # 重新定义了同名新变量??
    print('---val=', val, " id=", id(val))


nums = 20
print(nums)
print('nums=', nums, " id=", id(nums))
change(nums)  # 无法修改 nums
print('nums=', nums, " id=", id(nums))
print(nums)

print("-------------------------------2--------------------------------------")


# 参数为可变对象（列表list、字典dict、集合set是可变类型），python 通过引用传递
def change(val):
    print('---val=', val, " id=", id(val))
    val.append(99)  # 使用方法修改,会影响传入的实参
    print('---val=', val, " id=", id(val))


nums = [0, 1]
print(nums)
print('nums=', nums, " id=", id(nums))
change(nums)
print('nums=', nums, " id=", id(nums))
print(nums)

print("-------------------------------3--------------------------------------")


# 参数为可变对象，但传递过去的参数又指向了其他对象
def change(val):
    print('---val=', val, " id=", id(val))
    val = val + [10]  # 这句是关键，经过该赋值语句，此 val 已非彼 val , 重新定义同名变量??
    print('---val=', val, " id=", id(val))


nums = [0, 1]
print(nums)
print('nums=', nums, " id=", id(nums))
change(nums)
print('nums=', nums, " id=", id(nums))
print(nums)
