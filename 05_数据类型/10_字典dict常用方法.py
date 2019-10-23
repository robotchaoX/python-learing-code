zhangsan = {"name": "张三",
            "age": 18,
            "height": 1.75}


print("取值----" * 20)
# 取值
name_ = zhangsan["name"]  # 字典[key] 取值:
print("字典[key] 取值: ", name_)
age_ = zhangsan.get("age")  # .get 取值:
print(".get 取值: ", age_)


print("修改----" * 20)
# 修改元素
zhangsan["age"] = 23  # 字典[key] 修改:
print("字典[key] 修改: ", zhangsan)


print("增加----" * 20)
# 增加
zhangsan["weight"] = 60  # 字典[key] 增加,键key不存在增加键值对
print("字典[key] 增加: ", zhangsan)
zhangsan.setdefault("gff", "yuer")  # .setdefault 键key不存在增加键值对
print(".setdefault 增加键对: ", zhangsan)
zhangsan.setdefault("age", 80)  # .setdefault 增加键对,键key存在则不修改
print(".setdefault 增加键对: ", zhangsan)
exgff = {"01": "xiao",
         "02": "da"}
zhangsan.update(exgff)  # .update 连接覆盖更新,已存在的键值对会被覆盖
print(".update 连接更新: ", zhangsan)


print("复制----" * 20)
# 复制字典
lisi = {"name": "李四",
        "age": 44,
        "height": 1.44}
wangwu = {"name": "王五",
          "age": 55,
          "height": 1.55}
ls_copy = lisi.copy()
print(".copy 复制的字典: ", ls_copy)  # .copy浅复制的字典与源字典相独立
lisi.clear()  # .clear清除
print("清除源字典后 , .copy复制的字典不受影响: ", ls_copy)
ww_fuzhi = wangwu  # 与原字典相关联  # =赋值的字典与源字典相关联
print("= 对字典赋值: ", ww_fuzhi)
wangwu.clear()  # .clear清除
print("清除源字典后 , =赋值的字典与源字典相关联:", ww_fuzhi)


print("删除----" * 20)
# 删除
zhangsan.pop("age")  # .pop 按键值删除:  ,必须指定key
print(".pop 删除: ", zhangsan)
suiji_ = zhangsan.popitem()  # .popitem 随机(字典无序)删除键对 ,不需要指定key
print("随机返回", suiji_)
print(".popitem 随机删除: ", zhangsan)
del zhangsan["height"]  # del字典[key] 删除
print("del字典[key] 删除:", zhangsan)
# zhangsan.clear()  # .clear清除
# print(".clear删除: ", zhangsan)


print("信息----" * 20)
# 查询字典信息
key_ = zhangsan.keys()  # 返回键key列表 # 常与for连用
print("键keys列表: ", key_)
value_ = zhangsan.values()  # 返回元素值value列表 # 常与for连用
print("元素值values列表: ", value_)
items_ = zhangsan.items()  # 返回键对(key,value)元组列表 # 常与for连用
print("(key,value)键对items元组列表", items_)
dict_len = len(zhangsan)  # 返回字典长度,键值对数量
print("字典长度:", dict_len)
#判断一个键key是否在字典中
#in 或者 not in
is_key = "name" in zhangsan  #键key
print("键key是否在字典中in: ",is_key)


print("fromkeys----" * 20)
# fromkeys创建元素value值相同的新字典,不指定则为none
# dict.fromkeys(seq[, val]),创建一个新字典，以序列seq为字典的键，val为字典所有键对应的初始值
zhaoliu = {"name": "赵六",
           "age": 66}
zl_fromkeys = zhaoliu.fromkeys(("gg","bd","tb"), ("value值相同"))
print("zhaoliu:", zhaoliu)
print("fromkeys:", zl_fromkeys)




