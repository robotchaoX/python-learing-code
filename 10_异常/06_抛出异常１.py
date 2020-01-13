try:
    print("主动抛出异常")
    raise NameError("HiThere")  # 抛出异常
except NameError:  # 捕获到异常
    print('An exception flew by!')
    # raise  # 继续抛出异常
