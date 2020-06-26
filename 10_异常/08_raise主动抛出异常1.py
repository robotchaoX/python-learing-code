# raise 主动抛出异常
try:
    print("主动抛出异常")
    # 抛出异常
    # 系统定义异常类
    # raise ZeroDivisionError  # 无异常描述信息
    # 创建异常对象,ZeroDivisionError是系统定义异常类
    raise ZeroDivisionError("---ZeroDivisionError异常描述信息---")  # 添加异常描述
    # 创建异常对象,Exception是异常类
    raise Exception("---Exception异常描述信息---")  # 添加异常描述
except ZeroDivisionError as error:  # 捕获到异常
    print(error)
except Exception as error:  # 捕获到异常
    print(error)
    # raise  # 继续抛出异常
