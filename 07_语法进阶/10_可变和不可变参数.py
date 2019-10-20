def demo(num, num_list):
    print("内部函数")
    num = 11
    num_list = [1, 2, 3]
    print(num)
    print(num_list)


gl_num = 99
gl_num_list = [4, 5, 6]
demo(gl_num, gl_num_list)
print("全局变量")
print(gl_num)
print(gl_num_list)

