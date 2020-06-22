# 单引号
str1 = 'hello word'
print(str1)
print(type(str1))

# 双引号
str2 = "hello word"
print(str2)
print(type(str2))

# 三单引号
str3 = '''hello word'''
print(str3)
print(type(str3))

# 三双引号
str4 = """hello word"""
print(str4)
print(type(str4))


# 双引号 续行符\换行书写,实际是一行
str2 = "hello wo\
    rd"
print(str2)
print(type(str2))

# 三引号 支持文本换行,实际是多行
str4 = """hello wo
rd"""
print(str4)
print(type(str4))

# 输出"
str1 = '我是"大西瓜"'  # 字符串包含双引号,用单引号定义
print(str1)

# 输出'
str1 = "I'm Tom"
print(str1)

# 转义\'输出'
str1 = 'I\'m Tom'
print(str1)
