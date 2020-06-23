def testA():
    print("A函数开始...")
    print("这是A函数")
    print("A函数结束...")


def testBB():
    print("--BB函数开始...")
    # 函数的嵌套调用
    testA()
    print("--BB函数结束...")


testBB()
