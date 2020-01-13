# 家具类
class HouseFurniture():
    def __init__(self, name, area):  # 外部形参
        self.name = name  # 定义属性
        self.area = area

    def __str__(self):
        return "(__str__ return 打印对象:) [%s] 占地 %.2f " % (self.name, self.area)


class House():
    def __init__(self, house_type, area):  # 外部参数
        self.house_type = house_type  # 定义属性
        self.area = area
        # 剩余面积
        self.free_area = area  # 初始值
        # 家具名称列表
        self.furniture_list = []

    def __str__(self):
        # 小括号内可换行
        return ("(打印对象：) 户型：%s\n\t\t\t总面积：%s.2f [剩余：%.2f]\n\t\t\t家具：%s"
                % (self.house_type, self.area, self.free_area, self.furniture_list))

    def add_furniture(self, furniture):
        print("要添加 {%s}" % furniture)
        # 1 判断家具的大小
        if furniture.area > self.free_area:
            print("%s 的面积太大了,无法添加" % furniture.name)
            return  # 忽略后面的代码,直接返回到调用的地方
        # 2 将家具的名称添加到列表中
        self.furniture_list.append(furniture.name)
        # 3 计算剩余面积
        self.free_area -= furniture.area


# 创建家具对象
bed = HouseFurniture("席梦思", 40)
chest = HouseFurniture("衣柜", 2)
table = HouseFurniture("餐桌", 25)
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
