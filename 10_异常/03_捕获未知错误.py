try:
    num = int(input("输入一个整数:"))
    result = 8 / num
    print(result)
except ZeroDivisionError:  # 除0 异常
    print("除0错误")
except Exception as error:  # 未知异常
    print("未知错误: %s" % error)
