class Girl:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("{0} 的年龄是 {1}".format(self.name, self.__age))


xiaofang = Girl("小芳")
# 私有属性，在外界不能够被直接访问
print(xiaofang.__age)
# 私有方法，同样不允许在外界直接访问
# xiaofang.__secret()
