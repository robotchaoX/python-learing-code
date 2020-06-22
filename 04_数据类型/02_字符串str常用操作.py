str = "hello world ! hello world ! "

# len统计字符串长度
str_len = len(str)
print("字符串长度len: %d" % str_len)


# count 统计字符串里某个字符出现的次数
"""
count()方法语法：str.count(sub, start= 0,end=len(string))
    sub -- 搜索的子字符串
    start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
    end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
"""
str = "hello world ! hello world ! "
str_count = str.count("llo")
print("子字符串出现的次数count: %d" % str_count)  # 2
str_count = str.count("llo", 10, 20)  # 指定查找范围[10,20)
print("子字符串出现的次数count: %d" % str_count)  # 1
str_count = str.count("no exist")
print("子字符串出现的次数count: %d" % str_count)  # 0

# find查找某个子字符串是否包含在字符串内，存在返回首次出现的索引，不存在返回-1
print("find : ", str.find("llo"))  # 返回首次出现的索引
print("find : ", str.find("abc"))  # 不存在返回-1
print("find : ", str.find("llo", 10, 20))  # 指定查找范围[10,20)
# rfind()返回字符串最后一次出现的位置，如果没有匹配项则返回 -1
str1 = "this is is really a string example....wow!!!"
str2 = "is"
print("rfind:", str1.rfind(str2))
print("rfind:", str1.rfind(str2, 0, 10))  # 指定查找范围[0,10)

# find如果指定的字符串不存在，会返回-1
# index如果指定的字符串不存在，会报错

# index查找子字符串首次出现的位置，存在返回首次出现的索引，不存在则报错
print("index : ", str.index("llo"))  # 返回子串首次出现的索引
# print("index : ", str.index("abc"))  # 不存在会报错
print("index : ", str.index("llo", 10, 20))  # 查找范围[10,20)
# rindex()返回子字符串在字符串中最后出现的位置，如果没有匹配项则报错
# 如果没有匹配的字符串会报异常，可以指定可选参数[beg:end]设置查找的区间
str1 = "this is is really a string example....wow!!!"
str2 = "is"
print("rindex:", str1.rindex(str2))
print("rindex:", str1.rindex(str2, 0, 10))  # 指定查找范围[0,10)


# for in : 遍历字符串中字符
str = "hello"
for elem in str:  # 遍历字符串
    print(elem)

# 大小写转换
# lower()方法转换字符串中所有大写字符为小写。
str = "Runoob EXAMPLE....WOW!!!"
print(str.lower())

# upper()方法转换字符串中所有大写字符为小写。
str = "this is string example ....wow!!!"
print(str.upper())

# swapcase() 方法用于对字符串的大小写字母进行转换。
str = "This Is String Example....WOW!!!"
print(str.swapcase())

# capitalize()将字符串的第一个字母变成大写, 其他字母变小写。
str = "this is string example ....wow!!!"
print("str.capitalize() : ", str.capitalize())

# title()方法返回"标题化"的字符串, 就是说所有单词的首个字母转化为大写，其余字母均为小写
str = "this is string example from runoob....wow!!!"
print(str.title())
