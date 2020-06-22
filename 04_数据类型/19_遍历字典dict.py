# 遍历字典
dict = {"name": "张三",
        "age": 18,
        "height": 1.75}

print("\nfor key in dict:---")
# 遍历字典,默认按key遍历
for key in dict:  # 默认按key遍历
    print("key :", key)
    # print("%s : %s" % (key, dict[key]))

print("\nfor key in dict.key():---")
# 遍历字典键key
# 变量 key 是每一次循环中，获取到的键值对的key
for key in dict.keys():
    print("key :", key)
    # print("%s : %s " % (key, dict[key]))

print("\nfor key in dict.values():---")
# 遍历字典值value
for value in dict.values():
    print("value :", value)

print("\nfor key in dict.items():---")
# 遍历字典的项item
for item in dict.items():
    print("items : ", item)
    # print("item tuple中的一项 : ", item[0])

print("\nfor key in dict.items():---")
# 遍历字典的 key,value
for key, value in dict.items():  # 返回元组，直接拆包
    print("%s : %s" % (key, value))
