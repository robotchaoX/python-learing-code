
# isalpha 是否都是字母
str = "runoob"
print(str.isalpha())  # 字母
str = "hello word"  # 空格不是字母
print(str.isalpha())  # False

# isalnum 是否都是字母或数字
str = "runoob2016"  # 字符串没有空格
print(str.isalnum())  # 字母 + 数字
str = "www.runoob.com"  # .不是字母或数字
print(str.isalnum())  # False

print("--1--" * 10)

# 判断字符串是否只包含数字
num_str = "999"  # 数字
# num_str = "1.1"  # 都不能判断小数
# num_str = "\u00b2" # unicode 字符串
# num_str = "一千零一"  # 中文数字

print("num_str : ", num_str)
# isdecimal 只能是整数字,不能是小数,推荐
print("isdecimal : ", num_str.isdecimal())
# isdigit 能判断包含 数字 + unicode字符串
print("isdigit : ", num_str.isdigit())
# isnumeric 能判断包含 数字 + unicode字符串 + 中文数字
print("isnumeric : ", num_str.isnumeric())

print("--2--" * 10)

# isspace判断是否是空白字符 (包含空格,回车\r,换行\n,制表符\t)
space_str = "   \t\n\r   "
print("isspace : ", space_str.isspace())


# islower() 方法检测字符串是否由小写字母组成。
str = "runoob example....wow!!!"
print(str.islower())
# isupper() 方法检测字符串中所有的字母是否都为大写。
str = "THIS IS STRING EXAMPLE....WOW!!!"
print(str.isupper())
# istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
str = "This Is String Example...Wow!!!"
print(str.istitle())


