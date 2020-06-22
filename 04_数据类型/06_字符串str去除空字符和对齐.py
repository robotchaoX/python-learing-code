# strip去除空白字符
# strip() 截掉字符串两边的空格或指定字符
str = "     this is string example....wow!!!     "
print("str.strip : ", str.strip())
str = "88888888this is string example....wow!!!8888888"
print("str.strip : ", str.strip('8'))

# lstrip() 截掉字符串左边的空格或指定字符
str = "     this is string example....wow!!!     "
print("str.lstrip : ", str.lstrip())
str = "88888888this is string example....wow!!!8888888"
print("str.lstrip : ", str.lstrip('8'))

# rstrip()方法用于截掉字符串右边的空格或指定字符
str = "     this is string example....wow!!!     "
print("str.rstrip : ", str.rstrip())
str = "88888888this is string example....wow!!!8888888"
print("str.rstrip : ", str.rstrip('8'))

# zfill()方法返回指定长度的字符串，原字符串右对齐，不足前面填充0
str = "this is string example....wow!!!"
print("str.zfill : ", str.zfill(10))
print("str.zfill : ", str.zfill(40))


# 字符串对齐
str = "hello word!"
# 居中对齐,宽度20,填充符为" "
print("|%s|" % str.center(20, "-"))
# 左对齐
print("|%s|" % str.ljust(20, "."))
# 右对齐
print("|%s|" % str.rjust(20, " "))

poem = [
    "\t\n登鹳雀楼",
    "王之涣",
    "白日依山尽",
    "黄河入海流\r\n",
    "欲穷千里目",
    "更上一层楼"]

for poem_str in poem:
    # 去除空白字符
    # poem_strip = poem_str.strip()
    # print(poem_strip)

    # 去除空白字符后居中
    print("|%s|" % poem_str.strip().center(20, " "))
