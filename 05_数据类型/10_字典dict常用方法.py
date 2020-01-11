zhangsan_dict = {"name": "张三",
                 "age": 18}

# 1 取值
# [key]取值
name_ = zhangsan_dict["name"]  # 字典[key] 取值:
print("字典[key] 取值: ", name_)
# 在取值的时候，如果指定的key不存在，程序会报错！
# print(zhangsan_dict["name123"])
# get(key) 取值
age_ = zhangsan_dict.get("age")  # .get 取值:
print(".get 取值: ", age_)

# 2 修改元素
# 如果key存在，会修改已经存在的键值对
zhangsan_dict["age"] = 23  # 字典[key] 修改:
# 如果key不存在，会新增键值对
zhangsan_dict["height"] = 1.75  # key不存在,新增
print("字典[key] 修改: ", zhangsan_dict)

# 3 增加
# [key] 增加
zhangsan_dict["weight"] = 60  # 字典[key] 增加,键key不存在增加键值对
print("字典[key] 增加: ", zhangsan_dict)
# .setdefault() 增加
zhangsan_dict.setdefault("gff", 33)  # .setdefault 键key不存在增加键值对
print(".setdefault 增加键对: ", zhangsan_dict)
zhangsan_dict.setdefault("age", 80)  # .setdefault 增加键对,键key存在则 不修改
print(".setdefault 增加键对: ", zhangsan_dict)
# .update 连接覆盖更新
exgff = {"01": "xiao",
         "02": "da",
         "weight": 60  # 已存在的键值对会被覆盖
         }
zhangsan_dict.update(exgff)  # .update 连接覆盖更新,已存在的键值对会被覆盖
print(".update 连接更新: ", zhangsan_dict)

# 复制字典
lisi_dict = {"name": "李四",
             "age": 44,
             "height": 1.44}
wangwu_dict = {"name": "王五",
               "age": 55,
               "height": 1.55}
# .copy 复制生成新的临时字典
ls_copy = lisi_dict.copy()
print(".copy 复制的字典: ", ls_copy)  # .copy浅复制的字典与源字典相独立
lisi_dict.clear()  # .clear清除
print("清除源字典后 , .copy复制的字典不受影响: ", ls_copy)
# = 赋值的字典与源字典相关联
linked_dict = wangwu_dict  # 与原字典相关联  # =赋值的字典与源字典相关联
print("= 对字典赋值: ", linked_dict)
wangwu_dict.clear()  # .clear清除
print("清除源字典后 , =赋值的字典与源字典相关联:", linked_dict)

# 删除
# .pop(key) 按键删除
zhangsan_dict.pop("age")  # .pop 按键删除,必须指定key
print(".pop 删除: ", zhangsan_dict)
# 在删除指定键值对的时候，如果指定的key不存在，程序会报错！
# zhangsan_dict.pop("name123")
# suiji_ = zhangsan_dict.popitem()  # .popitem 随机删除键对 ,不需要指定key
# print("随机删除的键值对元组: ", suiji_)
# print(".popitem 随机删除: ", zhangsan_dict)
# del zhangsan_dict["height"]  # del字典[key] 删除
# print("del字典[key] 删除:", zhangsan_dict)
# zhangsan.clear()  # .clear清除
# print(".clear删除: ", zhangsan)


# 查询字典信息
# 键key列表
key_ = zhangsan_dict.keys()  # 返回键key列表 # 常与for连用
print("键keys列表: ", key_)
# 值value列表
value_ = zhangsan_dict.values()  # 返回元素值value列表 # 常与for连用
print("元素值values列表: ", value_)
# 键对(key,value)元组列表
items_ = zhangsan_dict.items()  # 返回键对(key,value)元组列表 # 常与for连用
print("(key,value)键对items元组列表", items_)
# 字典长度
dict_len = len(zhangsan_dict)  # 返回字典长度,键值对数量
print("字典长度:", dict_len)
# 判断一个键key是否在字典中
# in 或者 not in
is_key = "name" in zhangsan_dict  # 键key
is_key2 = "name" not in zhangsan_dict
print("键key是否在字典中in: ", is_key, is_key2)

# fromkeys创建元素value值相同的新字典,不指定则为none
# dict.fromkeys(seq[, val]),创建一个新字典，以序列seq为字典的键，val为字典所有键对应的初始值
zhaoliu = {"name": "赵六",
           "age": 66}
zl_fromkeys = zhaoliu.fromkeys(("gg", "bd", "tb"), ("value值相同"))  # ??
print("zhaoliu:", zhaoliu)
print("fromkeys:", zl_fromkeys)

xiaoming_dict = {"name": "小明",
                 "age": 18}
# 1. 统计键值对数量
print(len(xiaoming_dict))

# 2. 合并字典
temp_dict = {"height": 1.75,
             "age": 20}
# 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
xiaoming_dict.update(temp_dict)
print(xiaoming_dict)

# 3. 清空字典
xiaoming_dict.clear()

print(xiaoming_dict)
