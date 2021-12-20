# 全局变量
num = 10
# print(id(num))

def demo1():
    global num
    num = 99
    # print(id(num))
    print("demo1 ==> {0}".format(num))


def demo2():

    print("demo2 ==> {0}".format(num))


demo1()
demo2()
