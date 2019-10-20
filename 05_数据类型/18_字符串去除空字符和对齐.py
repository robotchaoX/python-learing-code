poem = [
    "\t\n登鹳雀楼",
    "王之涣",
    "白日依山尽",
    "黄河入海流\r\n",
    "欲穷千里目",
    "更上一层楼"]

for poem_str in poem:
    # print("|%s|" % poem_str.center(10," "))  #居中对齐,10为宽度," "为填充符
    # print("|%s|" % poem_str.ljust(10," "))  # 左对齐
    # print("|%s|" % poem_str.rjust(10, " "))  # 右对齐

    poem_strip = poem_str.strip()  # 去除空白字符
    print(poem_strip)
    # print("|%s|" % poem_str.strip().center(10, " "))  # 去除空白字符后居中

# lstrip()方法用于截掉字符串左边的空格或指定字符。
str = "     this is string example....wow!!!     "
print(str.lstrip())
str = "88888888this is string example....wow!!!8888888"
print(str.lstrip('8'))

# zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
str = "this is string example from runoob....wow!!!"
print ("str.zfill : ",str.zfill(40))
print ("str.zfill : ",str.zfill(50))

