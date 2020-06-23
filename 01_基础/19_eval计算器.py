
# eval() 将字符串转换为有效对象
str1 = "1"
str2 = "1.1"
str3 = "[1, 2, 3]"
str4 = "(10, 20, 30)"
str5 = "{100, 200, 300}"
print(type(eval(str1)), eval(str1), str1)
print(type(eval(str2)), eval(str2), str2)
print(type(eval(str3)), eval(str3), str3)
print(type(eval(str4)), eval(str4), str4)
print(type(eval(str5)), eval(str5), str5)


# eval() 将字符串表达式，并返回表达式的值
ret = eval("2 + 2")  # 返回 4
print(ret)

input_str = input("请输入算数题")
print(eval(input_str))
# 返回表达式计算结果
