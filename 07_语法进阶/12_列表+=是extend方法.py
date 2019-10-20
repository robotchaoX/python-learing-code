def demo(num,num_list):
    print("内部函数")
    num += num
    num_list += num_list  # 列表的+=是extend方法,与数值不一样
    # num_list = num_list + num_list  #局部变量,不影响全局变量
    # num_list = num_list *3  #局部变量,不影响全局变量
    print(num)
    print(num_list)


gl_num = 1
gl_list = [1, 2, 3]
print("前全局变量")
print(gl_num)
print(gl_list)
demo(gl_num, gl_list)
print("后全局变量")
print(gl_num)
print(gl_list)