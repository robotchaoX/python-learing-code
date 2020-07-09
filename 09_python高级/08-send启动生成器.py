def create_num(all_num):
    fib_a, fib_b = 0, 1
    current_num = 0
    while current_num < all_num:
        # send传入参数给yield返回值
        send_arg = yield fib_a  # fib_a为yield生成值
        print(">>>ret>>>>", send_arg)
        fib_a, fib_b = fib_b, fib_a + fib_b
        current_num += 1


# 创建生成器对象
obj = create_num(10)

# send一般不会放到第一次启动生成器，否则报错，如果非要这样做 那么传递None
# send可以传参数
# ret = obj.send(None)  # send第一次启动生成器不传入参数
# print(ret)
# ret = obj.send("---2222---")  # send第一次启动生成器传参报错
# print(ret)

# next不可以传参数
ret = next(obj)
print(ret)
# next不可以传参数
ret = next(obj)
print(ret)

# send里面的数据会 传递给第5行，当做yield a的结果，然后ret保存这个结果,,,
# send的结果是下一次调用yield时 yield后面的值
ret = obj.send("---4444----")
print(ret)
