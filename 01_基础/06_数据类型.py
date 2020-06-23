# 基本数据类型 整型:int
#            浮点型:float 没有double
#            布尔:bool ,值 True False
# 高级数据类型 字符串:str
#            列表:list
#            元组:tuple
#            集合:set
#            字典:dict

# 在 Python 中，定义变量时是不需要指定变量的类型的
# 在运行的时候，Python 解释器，会根据赋值语句等号右侧的数据
# 自动推导 出变量中保存数据的准确类型


# 整型:int
age = 18
print(type(age))

# 浮点型:float
height = 1.75
print(type(height))

# 布尔:bool ，真 True ,假 False
gender = False  # 假
print(type(gender))

# 字符串:str
name = "小明"
print(type(name))

# 列表: list
li = [1, 2, 3]
print(type(li))

# 元组: tuple
tp = (10, 20, 30)
print(type(tp))

# 集合: set
st = {100, 200, 300}
print(type(st))

# 字典: dict
dt = {'name': 'Tom', 'age': 18}
print(type(dt))

print("-" * 50)

# python3 不区分 int 和 long, 都是int, python2 区分
print(type(2 ** 32), 2 ** 32)  # python3 int , python2 int
print(type(2 ** 64), 2 ** 64)  # python3 int , python2 long
print(type(2 ** 1000), 2 ** 1000)  # python 不会溢出??

# 字符串拼接 +
first_name = "三丰"
last_name = "张"
name = first_name + last_name
print(name)

# 重复拼接字符串
print("-" * 50)
