hello_str = "hello world"

# 1.判断是否以指定字符串开始startswith
print("startswith : ", hello_str.startswith("hell"))

# 2. 判断是否以指定字符串结束endswith
print("endswith : ", hello_str.endswith("world"))

# 3. 查找指定字符串find,类似.index
print("find : ", hello_str.find("llo"))  # 返回首次出现的索引
print("find : ", hello_str.find("abc"))  # 不存在返回-1
# rfind()返回字符串最后一次出现的位置，如果没有匹配项则返回 -1
str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rfind(str2))
print (str1.rfind(str2, 0, 10))


# 4. 替换字符replace
str_replace = hello_str.replace("world", "python")  # replace不改变原字符串
print("临时替换 : ", str_replace)
print("原字符不变 : ", hello_str)
