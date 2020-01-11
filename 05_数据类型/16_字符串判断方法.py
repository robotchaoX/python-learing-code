# 1. 判断空白字符(包含空格,回车\r,换行\n,制表符\t)isstring
space_str = "   \t\n\r   "
print("isspace : ", space_str.isspace())

# 2. 判断字符串是否只包含数字
# num_str = "1.1"  # 2.1 都不能判断小数
# num_str = "\u00b2" # 2.2 unicode 字符串
num_str = "一千零一"  # 2.3 中文数字
print("num_str : ", num_str)
print("isdecimal : ", num_str.isdecimal())  # 只能是整数字,不能是小数,推荐
print("isdigit : ", num_str.isdigit())  # 能判断包含 数字 + unicode字符串
print("isnumeric : ", num_str.isnumeric())  # 能判断包含 数字 + unicode字符串 + 中文数字

print("判断----" * 10)
str = "runoob"
print(str.isalpha())  # 字符
str = "runoob2016"  # 字符串没有空格
print(str.isalnum())  # 字符 + 数字
str = "www.runoob.com"
print(str.isalnum())

print("判断----" * 10)
# islower() 方法检测字符串是否由小写字母组成。
str = "runoob example....wow!!!"
print(str.islower())
# isupper() 方法检测字符串中所有的字母是否都为大写。
str = "THIS IS STRING EXAMPLE....WOW!!!"
print(str.isupper())
# istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
str = "This Is String Example...Wow!!!"
print(str.istitle())
