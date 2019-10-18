def tes1():
    """内"""
    print("-" * 50)


def tes2():
    """外"""
    print("*" * 50)
    tes1()
    print("+" * 50)


tes2()
