class Cat:

    def __init__(self, new_name):

        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name

    def eat(self):
        print("{0} 爱吃鱼".format(self.name))

# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
# tom = Cat("Tom123")
# print(tom.name)
# print(tom.eat())
#
lazy_cat = Cat("大懒猫")
print(lazy_cat)
# lazy_cat.eat()
