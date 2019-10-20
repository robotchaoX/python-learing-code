poem = "\t\n登鹳雀楼 \t王之涣 \r白日依山尽 \n黄河入海流\r  \n欲穷千里目\t \t更上一层楼"
print(poem)

# 1. 拆分字符串, 字符串-->列表
poem_split = poem.split()  # 以空白字符(空格\t\n\r)都作为分隔符拆分字符串为字符串列表
print("split拆分 : ",poem_split)

# 2. 合并字符串, 列表-->字符串
poem_join = " ".join(poem_split)  # 以空格为分隔符,将字符串列表合并连接为一个字符串
print("join合并 : ",poem_join)
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))



