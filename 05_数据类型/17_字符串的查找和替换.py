hello_str = "hello world"

# 1. startswith 判断是否以指定字符串开始
print("startswith : ", hello_str.startswith("hell"))

# 2. endswith 判断是否以指定字符串结束
print("endswith : ", hello_str.endswith("world"))

# 3. 查找指定字符串find,类似.index
# 类似.index同样可以查找指定的字符串在大字符串中的索引
print("find : ", hello_str.find("llo"))  # 返回首次出现的索引
# index如果指定的字符串不存在，会报错
# find如果指定的字符串不存在，会返回-1
print("find : ", hello_str.find("abc"))  # 不存在返回-1
# rfind()返回字符串最后一次出现的位置，如果没有匹配项则返回 -1
str1 = "this is is really a string example....wow!!!"
str2 = "is"
print("rfind:", str1.rfind(str2))
print("rfind:", str1.rfind(str2, 0, 10))

# 4. 替换字符replace
# replace方法执行完成之后，会返回一个新的字符串
# 注意：不会修改原有字符串的内容
str_replace = hello_str.replace("world", "python")  # replace不改变原字符串
print("临时替换 : ", str_replace)
print("原字符不变 : ", hello_str)
