# 字典
dict1 = {"name": "张三", "age": 18, "gender": "男"}

# 1 取键值对的值
# [key]取值
name_ = dict1["name"]  # 字典[key] 取值:
print("字典[key] 取值: ", name_)
# 在取值的时候，如果指定的key不存在，程序会报错！
# print(dict1["name123"])
# .get(key) 取值
age_ = dict1.get("age")  # .get 取值
print(".get 取值: ", age_)
# 如果查找的key不存在，则返回第二个参数，默认值None
id_ = dict1.get("ID")  # key不存在，返回默认值None
print(".get 取值: ", id_)
id_ = dict1.get("ID", -99)  # key不存在，则返回第二个参数
print(".get 取值: ", id_)


# 2 修改键值对的值
# 如果key存在，会修改已经存在的键值对
dict1["age"] = 23  # 字典[key] 修改:
print("字典[key] 修改: ", dict1)
# 如果key不存在，会新增键值对


# 3 增加键值对
# [key] 增加键值对
# 如果key不存在，会新增键值对
dict1["weight"] = 60  # 字典[key]key不存在,增加键值对
print("字典[key] 增加: ", dict1)
# .setdefault 键key不存在，则增加键值对
dict1.setdefault("newKey", 33)  # 键key不存在，增加键值对
print(".setdefault 增加键对: ", dict1)
# .setdefault 键key存在则，不执行，不修改字典
dict1.setdefault("name", "王八")  # 键key存在，不修改字典
print(".setdefault 增加键对: ", dict1)

# 合并字典
# .update 合并覆盖更新字典
# 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
dict1 = {"name": "张三", "age": 18, "gender": "男"}
newDict = {"ID": 13579,  # 不存在的键值会新增
           "passwd": "mima",
           "gender": "女"  # 已存在的键值对会被覆盖
           }
dict1.update(newDict)  # .update 连接覆盖更新,已存在的键值对会被覆盖
print("update 合并字典: ", dict1)

# 复制字典 独立/关联
ori_dict = {"name": "李四",
            "age": 44,
            "height": 1.44}
# .copy 复制生成新的临时字典
#! .copy浅复制的字典与源字典相独立
copy_dict = ori_dict.copy()
print(".copy 复制的字典: ", copy_dict)  # .copy浅复制的字典与源字典相独立
ori_dict.clear()  # .clear清除
# 清除源字典后，.copy复制的字典不受影响
print(".copy 复制的源字典: ", copy_dict)

ori_dict = {"name": "李四",
            "age": 44,
            "height": 1.44}
#! = 赋值的字典与源字典相关联
linked_dict = ori_dict  # =赋值与原字典相关联
print("=赋值相关联: ", linked_dict)
# 清除源字典后，=赋值的字典受影响
ori_dict.clear()  # .clear清除
print("=赋值关联的源字典:", linked_dict)


# 删除键值对
dict1 = {"name": "张三", "age": 18, "height": 175, "gender": "男"}
# .pop(key) 按键删除
dict1.pop("age")  # .pop 按键删除,必须指定key
print(".pop 删除: ", dict1)
# .pop(key) 按键删除键值对，如果指定的key不存在，程序会报错！
# dict1.pop("name123")
# del 删除键值对
del dict1["gender"]  # del字典[key] 删除
print("del字典[key] 删除:", dict1)
# .popitem 随机删除键对 ,不需要指定key
deled = dict1.popitem()
print("随机删除的键值对元组: ", deled)
print(".popitem 随机删除: ", dict1)
# .clear 清空字典
dict1.clear()
print(".clear删除: ", dict1)


# 查询字典信息
dict1 = {"name": "张三", "age": 18, "gender": "男"}
# .keys() 键的列表
key_ = dict1.keys()  # 返回键key列表 # 常与for连用
print("键keys列表: ", key_)
# .values() 值的列表
value_ = dict1.values()  # 返回元素值value列表 # 常与for连用
print("元素值values列表: ", value_)
# .items() 键对(key,value)元组的列表
items_ = dict1.items()  # 返回键对(key,value)元组列表 # 常与for连用
print("键对items元组列表: ", items_)

# 字典长度
# len统计键值对数量
dict_len = len(dict1)  # 返回字典长度,键值对数量
print("字典长度:", dict_len)

# in 或者 not in
# 判断一个键key是否在字典中，返回True，False
is_key_in = "name" in dict1  # 键key
print("in键key在字典中: ", is_key_in)
is_key_not_in = "name" not in dict1
print("not in键key不在字典中: ", is_key_not_in)


# fromkeys创建元素value值相同的新字典,不指定则为None
# dict.fromkeys(seq[, val]),创建一个新字典，以序列seq为字典的键，val为字典所有键对应的初始值
zhaoliu = {"name": "赵六", "age": 66}
# 返回值和源字典没有关系？
zl_fromkeys = zhaoliu.fromkeys(("gg", "bd", "tb"), ("相同初值"))  # ??
print("zhaoliu:", zhaoliu)
print("fromkeys:", zl_fromkeys)
