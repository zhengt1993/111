
class Person:

    name:str = "default"
    gender:str ="default"
    #私有类
    __money:float = 1000
    def __init__(self,name,gender,money):
        self.name = name
        self.gender = gender
        self.__money = money
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def run(self):
        print(self.name + " is running")
    def make_money(self):
        print(f"{self.name} cloud make money")

    def get_money(self):
        print(f"获取私有属性money的值 {self.__money}")
        return self.__money

# p = Person("lili","woman",10000)
# print(p.name,p.gender)
# p.eat()
# p.sleep()
# p.run()
# print(p.get_money())

#继承

# class FunnyMan(Person):
#     def fun(self):
#         print(f"{self.name} is very funny")
#
#
# funnyman1 = FunnyMan("st","男",20000)
# print(funnyman1.name)
# funnyman1.sleep()
# funnyman1.fun()

class Singer(Person):
    def make_money(self,moneynum):
        print(f"{self.name} could make money {moneynum} yuan")

singer = Singer("yaya","女",1000)
singer.make_money(5000)


