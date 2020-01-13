class HouseFurniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "__str__ return:[%s] 占地 %.2f " % (self.name, self.area)


# 创建家具
bed = HouseFurniture("席梦思", 4)
chest = HouseFurniture("衣柜", 2)
table = HouseFurniture("餐桌", 1.5)
print(bed)
print(chest)
print(table)
