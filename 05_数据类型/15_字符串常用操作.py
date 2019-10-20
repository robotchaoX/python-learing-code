str = "hello world ! hello world ! "

# 统计字符串长度
str_len = len(str)
print("字符串长度len: %d" % str_len)


# 统计子字符串出现的次数
str_count = str.count("llo")
print("子字符串出现的次数count: %d" % str_count)

# 子字符串首次出现的位置,不存在则报错
str_index = str.index("llo")
print("字符串出现的位置index: %d" % str_index)
# rindex() 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间。
str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rindex(str2))

