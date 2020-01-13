try:
    num = int(input("输入一个整数:"))
    result = 8 / num
    print(result)
except ZeroDivisionError:  # 除0 异常
    print("除0错误")
except ValueError:  # int 异常
    print("请输入正确的整数")
