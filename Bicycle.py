import yaml


class Bycicle:
    def run(self,km):
        self.km = km
        print(f"这是自行车骑行的里程数:{km}")
class Ebycicle(Bycicle):
    #定义电量等级
    def __init__(self,bettery_level):
        self.bettery_level = bettery_level
    #定义充电方法
    def fill_charge(self,vol):
        print(f"这是剩余电量:{vol}")
    #定义run方法：
    def run(self,km):
        max_mile = self.bettery_level * 10
        leave_mile= km - max_mile

        if leave_mile > 0:
            print(f"这是电量骑行的里程数:{max_mile}")
            super().run(leave_mile)
        else:
            print(f"这是自行车骑行的里程数:{km}")

myebycilie = Ebycicle(5)
myebycilie.run(200)
# with open ("bycicle_dates.yml") as f:
#     dates = yaml.safe_load(f)