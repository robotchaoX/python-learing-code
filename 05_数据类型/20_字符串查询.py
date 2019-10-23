# count() 方法用于统计字符串里某个字符出现的次数
"""
count()方法语法：str.count(sub, start= 0,end=len(string))
    sub -- 搜索的子字符串
    start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
    end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
"""
str = "www.runoob.com"
sub = 'o'
print("str.count('o') : ", str.count(sub))
sub = 'run'
print("str.count('run', 0, 10) : ", str.count(sub, 0, 10))
