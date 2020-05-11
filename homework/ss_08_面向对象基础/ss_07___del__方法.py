class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("{0} 来了".format(self.name))

    def __del__(self):

        print("{0} 我去了".format(self.name))

# tom 是一个全局变量
tom = Cat("Tom")
print(tom)

# del 关键字可以删除一个对象
del tom

print("-" * 50)
