# 全局变量

# 注意：在开发时，应该把模块中的所有全局变量
# 定义在所有函数上方，就可以保证所有的函数
# 都能够正常的访问到每一个全局变量了

# 定义全局变量
num_gl = 10

# global num = 10 # 错误,global函数内用时声明


# 访问全局变量
def demo1():
    # 访问全局变量
    print("demo3 ==> %d" % num_gl)


# 在python中，是不允许直接修改全局变量的值
# 同名局部变量,没有global声明
def demo2():
    # 默认使用赋值语句,会在函数内部，重新定义一个同名局部变量num_gl
    #! 重新定义一个同名的局部变量,作用域内覆盖全局变量
    num_gl = -22  # 同名的局部变量
    print("同名的局部变量 demo1 ==> %d" % num_gl)  # 无法直接修改全局变量


# 修改全局变量,global声明
def demo3():
    # 希望修改全局变量的值 - 使用 global 声明全局变量
    # global 关键字会告诉解释器后面的变量是一个全局变量
    # 再使用赋值语句时，就不会创建局部变量
    #! global声明全局变量
    global num_gl  # 函数内用时,必须要使用global声明全局变量
    num_gl = 99  # 修改全局变量
    print("demo2 ==> %d" % num_gl)


# 全局变量函数内外都能访问
print("num_gl : ", num_gl)

# 访问全局变量
demo1()

# 无法直接修改全局变量，除非global声明全局变量
# 定义同名局部变量
demo2()

# 使用global声明了全局变量，修改的是全局变量的值
demo3()

print("num_gl : ", num_gl)
