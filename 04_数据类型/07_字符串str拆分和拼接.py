# 1. 将字符串中的空白字符全部去掉
# 2. 再使用 " " 作为分隔符，拼接成一个整齐的字符串
poem = "\t\n登鹳雀楼 \t王之涣 \r白日依山尽 \n黄河入海流\r  \n欲穷千里目\t \t更上一层楼"
print(poem)

# 1. split()拆分字符串, 字符串-->列表
poem_list = poem.split()  # 以空白字符(空格\t\n\r)都作为分隔符拆分字符串为字符串列表
print("split拆分 : ", poem_list)

and_str = "hello and word and python and you"
# 以and为分隔符分割，丢失分隔符and，split分割返回一个列表
list_list = and_str.split("and")
print("split拆分 : ", list_list)
list_list = and_str.split("and", 2)  # 分割次数
print("split拆分 : ", list_list)

# 2. join()合并字符串, 列表-->字符串
poem_join = " ".join(poem_list)  # 以空格为分隔符,将字符串列表合并连接为一个字符串
print("join合并 : ", poem_join)

seq = ("r", "u", "n", "o", "o", "b")  # 字符串序列
print(" ".join(seq))
print("-".join(seq))
print("***".join(seq))
print("".join(seq))
