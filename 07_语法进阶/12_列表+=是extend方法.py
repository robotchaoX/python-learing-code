def demo(nums, num_list):
    print("内部函数")
    print('nums=', nums, " id=", id(nums))
    nums += nums  # num 新同名局部变量???
    print('nums=', nums, " id=", id(nums))

    # 列表变量使用 += 不会做相加再赋值的操作 ！
    # 本质上是在调用列表的 extend 方法
    num_list += num_list  # 列表的 += 是extend方法,与数值不一样
    # num_list.extend(num_list) # 等价 +=

    # num_list = num_list + num_list  # 新建同名局部变量,不影响实参???
    # num_list = num_list *3  # 新建同名局部变量,不影响实参

    print(nums)
    print(num_list)
    print("函数完成")


gl_num = 1
gl_list = [1, 2, 3]
print("前全局变量")
print(gl_num)
print(gl_list)
demo(gl_num, gl_list)
print("后全局变量")
print(gl_num)
print(gl_list)
