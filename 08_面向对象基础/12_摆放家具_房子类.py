# 家具类
class HouseFurniture:
    def __init__(self, name, area):  # 外部形参
        self.name = name  # 定义属性
        self.area = area

    def __str__(self):
        return "(__str__ return 打印对象:) [%s] 占地 %.2f " % (self.name, self.area)


class House:
    def __init__(self, house_type, area):  # 外部参数
        self.house_type = house_type  # 定义属性
        self.area = area
        # 剩余面积
        self.free_area = area  # 初始值
        # 家具名称列表
        self.furniture_list = []  # 空列表

    def __str__(self):
        # 小括号内可换行
        return ("(打印对象：) 户型：%s\n\t\t\t总面积：%s.2f [剩余：%.2f]\n\t\t\t家具：%s"
                % (self.house_type, self.area, self.free_area, self.furniture_list))

    def add_furniture(self, furniture):
        print("要添加 {%s}" % furniture)


# 创建家具对象
bed = HouseFurniture("席梦思", 4)
chest = HouseFurniture("衣柜", 2)
table = HouseFurniture("餐桌", 1.5)
print(bed)
print(chest)
print(table)

# 创建房子对象
my_house = House("两室一厅", 60)
print(my_house)

# 添加家具
my_house.add_furniture(bed)
my_house.add_furniture(chest)
my_house.add_furniture(table)
print(my_house)
