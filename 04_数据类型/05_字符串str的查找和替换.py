hello_str = "hello world"

# 1. startswith 判断是否以指定字符串开始
str1 = "hello word and python"
print(str1.startswith("hello"))
print(str1.startswith("hello", 10, 20))  # 指定开始结束位置

# 2. endswith 判断是否以指定字符串结束
str1 = "hello word and python"
print(str1.endswith("python"))
print(str1.endswith("python", 10, 20))  # 指定开始结束位置

# 3. find查找某个子字符串是否包含在字符串内，存在返回首次出现的索引，不存在返回-1
print("find : ", hello_str.find("llo"))  # 返回首次出现的索引
print("find : ", hello_str.find("abc"))  # 不存在返回-1
print("find : ", hello_str.find("llo", 10, 20))  # 指定查找范围[10,20)
# rfind()返回字符串最后一次出现的位置，如果没有匹配项则返回 -1
str1 = "this is is really a string example....wow!!!"
str2 = "is"
print("rfind:", str1.rfind(str2))
print("rfind:", str1.rfind(str2, 0, 10))  # 指定查找范围[0,10)

# find如果指定的字符串不存在，会返回-1
# index如果指定的字符串不存在，会报错

# index查找子字符串首次出现的位置，存在返回首次出现的索引，不存在则报错
print("index : ", hello_str.index("llo"))  # 返回子串首次出现的索引
# print("index : ", hello_str.index("abc"))  # 不存在会报错
print("index : ", hello_str.index("llo", 10, 20))  # 查找范围[10,20)
# rindex()返回子字符串在字符串中最后出现的位置，如果没有匹配项则报错
# 如果没有匹配的字符串会报异常，可以指定可选参数[beg:end]设置查找的区间
str1 = "this is is really a string example....wow!!!"
str2 = "is"
print("rindex:", str1.rindex(str2))
print("rindex:", str1.rindex(str2, 0, 10))  # 指定查找范围[0,10)


# 4. 替换字符replace
# replace方法执行完成之后，会返回一个新的字符串
#! 注意：不会修改原有字符串的内容
# 字符串是不可变类型
hello_str = "hello world ! hello world !"
str_replace = hello_str.replace("world", "python")  # replace不改变原字符串
print("临时替换 : ", str_replace)
print("原字符不变 : ", hello_str)
str_replace = hello_str.replace("world", "python", 2)  # 替换次数,超过替换全部
print("原字符不变 : ", hello_str)
