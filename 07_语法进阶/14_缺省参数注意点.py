# 缺省参数放在末尾
def print_info(name, title="", gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("[%s] %s 是 %s" % (title, name, gender_text))


print_info("小明")
print_info("老王", "班长")
# 有多个缺省参数时可用形参名=修改缺省值
print_info("小美", gender=False)  # 选择指定某个缺省值
