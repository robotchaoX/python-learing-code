def demo(num_list):
    print("函数内部")
    num_list.append(9)  # 函数内部方法,是双向传递,会修改外部数据
    print(num_list)


gl_list = [1,2,3]
print("全局变量")
print(gl_list)
demo(gl_list)
print("全局变量")
print(gl_list)
