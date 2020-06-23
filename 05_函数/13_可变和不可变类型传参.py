# 数据能够直接修改就是可变类型,不能直接修改就是不可变类型
# 不可变类型（整型int、浮点型float、字符串str、元组tuple）
# 可变类型（列表list、字典dict、集合set）


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


# 全局变量
gl_num = 99
gl_num_list = [9, 9, 9]
print("num = %d , id = %d" % (gl_num, id(gl_num)))
print("num_list = %s , id = %d" % (gl_num_list, id(gl_num_list)))

demo(gl_num, gl_num_list)
print("全局变量")
print(gl_num)
print(gl_num_list)

print("----------------------1------------------------")


#! 实参为不可变对象（数值类型、字符串str、元组tuple），
#! python 通过值传递
def change(val):
    print('---val=', val, " id=", id(val))
    val += 10  # 新变量??
    print('---val=', val, " id=", id(val))


nums = 20
print(nums)
print('nums=', nums, " id=", id(nums))
# 数值变量是不可变类型，传值
change(nums)  # 无法修改 nums
print('nums=', nums, " id=", id(nums))
print(nums)  # 源不变

print("----------------------2------------------------")


#! 实参为可变对象（列表list、字典dict、集合set是可变类型），
#! python 通过引用传递
def change(val):
    print("--id=", id(val),  ' val=', val)
    # 使用容器方法修改列表的内容
    val.append(99)  # 容器方法修改,会修改外部传入的实参数据

    # 列表的 += 等价extend方法,不是list=list+list,与数值不一样
    # num_list += num_list  # 等价extend方法
    # num_list.extend(num_list) # 等价 +=
    print("--id=", id(val), ' val=', val)


# 全局变量
# list列表,可变类型
nums_list = [0, 1]
print("  id=", id(nums_list), ' nums_list=', nums_list)

# 列表list变量是可变类型,传引用
change(nums_list)  # 可以修改源
# 修改了源全局变量
print("  id=", id(nums_list), ' nums_list=', nums_list)


print("----------------------3------------------------")


#! 参数为可变对象，但传递过去的参数又指向了其他对象
def change(val):
    print("--id=", id(val), ' val=', val)
    val = [5, 6, 7]  # 定义了同名变量??
    # val = val + [10]  # 这句是关键,经过该赋值语句,此val已非彼val,重新定义同名变量??
    # 列表的 += 等价extend方法,不是list=list+list,与数值不一样
    # val = val + val  # 新建同名局部变量,不影响实参???
    # val = val * 3  # 新建同名局部变量,不影响实参
    print("--id=", id(val), ' val=', val, )


nums_list = [0, 1]
print(nums_list)
print('nums_list=', nums_list, " id=", id(nums_list))
# 列表list变量是可变类型,传引用,但传递过去的参数又指向了其他对象
change(nums_list)  # 不可修改源
print('nums_list=', nums_list, " id=", id(nums_list))
print(nums_list)  # 源不变
