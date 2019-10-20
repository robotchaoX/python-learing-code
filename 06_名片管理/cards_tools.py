# 记录所有名片字典
card_list = []


def show_menu():
    """
    显示菜单
    """
    print("* " * 17)
    print("*    欢迎使用[名片管理系统]V1.0    *")
    print("*        [1] 新增名片            *")
    print("*        [2] 显示全部            *")
    print("*        [3] 修改名片            *")
    print("*        [0] 退出系统            *")
    print("* " * 17)


def new_card():
    """新增名片"""
    # print("-" * 50)
    print("新增名片")
    # 1.提示用户名片的详细信息
    name_str = input("请输入姓名:")
    phone_str = input("请输入电话:")
    qq_str = input("请输入QQ:")
    email_str = input("请输入邮箱:")
    # 2.使用用户信息建立名片字典
    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str
    }
    # 3.将字典添加到列表
    card_list.append(card_dict)
    # 4.提示用户添加成功
    print("添加%s的名片成功!" % name_str)


def show_all():
    """显示所有"""
    # print("-" * 50)
    print("显示所有")

    # 判断是否存在名片记录
    if len(card_list) == 0:
        print("当前没有任何名片记录,请新增名片!")

        # return 直接返回到调用函数的位置,而不执行本函数后面的代码
        return

    # 打印表头
    for card_title in ["姓名", "电话", "QQ号", "邮箱"]:
        print(card_title, end="\t\t")
    print("")

    # 打印分割线
    print("=" * 40)

    # 遍历名片
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))


def search_card():
    """搜索名片"""
    # print("-" * 50)
    print("搜索名片")

    # 提示用户输入姓名
    find_name = input("请输入搜索的姓名:")
    # 输出搜索信息
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print("=" * 40)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]
                                                ))
            # 对名片执行修改和删除操作
            deal_card(card_dict)
            break
    else:
        print("抱歉没找到 %s " % find_name)


# 函数定义可以在使用之后
def deal_card(find_dict):
    """
    处理查找到的名片
    :param find_dict: 查找到的名片
    """
    # print(find_dict)
    action_str = input("请输入要执行的操作"
                       "[1]修改  [2]删除  [0]返回上级菜单: ")
    if action_str == "1":
        print("您选择的操作是: [1] 修改名片")
        find_dict["name"] = input_card_info(find_dict["name"], "姓名[回车不修改]:")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话[回车不修改]:")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ号[回车不修改]:")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱[回车不修改]:")
        print("修改名片成功")

    elif action_str == "2":
        print("您选择的操作是: [2] 删除名片")
        card_list.remove(find_dict)
        print("删除名片成功!")


def input_card_info(dict_value, tip_message):
    """
    输入名片信息
    :param dict_value: 字典中原有的值
    :param tip_message: 输入提示
    :return: 如果用户输入了内容,就返回内容,否则返回原字典中的值
    """
    # 提示用花输入
    changed_value = input(tip_message)
    # 判断用户输出,有输入返回输入值
    if len(changed_value) > 0:
        return changed_value
    # 没有输入返回原值
    else:
        return dict_value
