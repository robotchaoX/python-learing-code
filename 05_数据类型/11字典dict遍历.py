dict = {"name": "张三",
        "age": 18,
        "height": 1.75}

# 遍历字典
# for key in dict :
#     print("%s : %s" % (key,dict[key]))

for key in dict.keys() :
    print(key,dict[key])

# 遍历字典键key
# for key in dict.keys() :
#     print("%s : %s " %(key,dict[key]))


# 遍历字典值value
# for value in dict.values():
#     print("value :", value)

# 遍历字典的项item
# for item in dict.items():
#     print("items : ", item)
#     print("tuple中的一项 : ",item[0])

# 遍历字典的 key,value
# for key, value in dict.items():
#     print("%s : %s" % (key, value))
