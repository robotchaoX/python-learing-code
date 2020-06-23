# 函数参数


# 位置参数
# 函数形参,不需要类型说明
def print_info(name, age):
    print("%s，年龄%d" % (name, age))


# 函数调用,直接传参
# 参数的顺序与个数必须一致
print_info("小明", 22)
print("-------------------")


# 关键字参数
def print_info(name, age):
    print("%s，年龄%d" % (name, age))


# 函数调用时说明形参
# 关键字参数，顺序可以不一致
print_info(age=22, name="小明")
# 位置参数必须在关键字参数前面
print_info("小美", age=18)
print("-------------------")


# 缺省参数
# 缺省参数放末尾
def print_info(name, age=18, gender=True):  # 默认值
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s，年龄%d，性别 %s" % (name, age, gender_text))


# 缺省参数传值
print_info("小明")
print_info("小张", 22)
print_info("小美", 33, True)
# 有多个缺省参数时可用形参名=修改缺省值
print_info("小艾", gender=False)  # 选择指定某个缺省值


# 参数个数不确定
# *元组参数, **字典参数
def demo(num, *args, **kwargs):
    print(num)  # 参数
    print(args)  # 元组
    print(kwargs)  # 字典
    print("-----")


# 元组()直接逗号分隔,字典{}key=value
demo(-99)
demo(-99, 1, 2, 3)
demo(-99, 1, 2, 3, name="小明", age=18)

# 传入参数作为元组


def demo(*args):
    print(args)


# 不定长参数，作为元组()传入
demo(1, 2, 3)  # 元组
demo(1, 2, 3, "小明")
demo()  # 传入空元组


# 传入参数作为字典
def demo(**kwargs):
    print(kwargs)


# 不定长参数，作为字典{:}传入
# 关键字参数形式
demo(name="Tom", age=18)  # 字典
demo(name="Tom", age=18, gender="男")
demo()  # 传入空字典
# demo("name"="Tom", "age"=18)  # error 不需要引号，关键字参数形式
# demo("name":"Tom", "age":18)  # 不是字典格式，关键字参数形式
# demo({"name":"Tom", "age":18})  # 不是字典格式，关键字参数形式


# 不定长参数应用
# 元组作为形参
def sum_numbers(args_tuple):  # 直接传递元组
    num = 0
    print(args_tuple)
    for num in args_tuple:
        num += num
    return num


# 直接传递元组
result = sum_numbers((1, 2, 3))
print(result)


# *args 不定长参数作为元组传递
def sum_numbers(*args):  # 多值参数传递元组
    num = 0
    print(args)
    # for遍历
    for n in args:
        num += n
    return num


# 多值参数传递元组
result = sum_numbers(1, 2, 3)
print(result)
