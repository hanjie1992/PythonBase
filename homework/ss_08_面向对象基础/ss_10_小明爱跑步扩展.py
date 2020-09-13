class Person:

    def __init__(self, name, weight):

        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):

        return "我的名字叫 {0} 体重是 {1:.2f} 公斤".format(self.name, self.weight)

    def run(self):
        print("{0} 爱跑步，跑步锻炼身体".format(self.name))

        self.weight -= 1

    def eat(self):
        print("{0} 是吃货，吃完这顿再减肥".format(self.name))

        self.weight += 2

xiaoming = Person("小明", 75.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)

# 小美爱跑步
xiaomei = Person("小美", 45)

xiaomei.eat()
xiaomei.run()

print(xiaomei)
print(xiaoming)
