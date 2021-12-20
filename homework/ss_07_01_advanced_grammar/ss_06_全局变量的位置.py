# 注意：在开发时，应该把模块中的所有全局变量
# 定义在所有函数上方，就可以保证所有的函数
# 都能够正常的访问到每一个全局变量了
num = 10
# 再定义一个全局变量
title = "我是商师人"
# 再定义一个全局变量
name = "小明"

def demo():

    print("{0}".format(num))
    print("{0}".format(title))
    print("{0}".format(name))

# # 再定义一个全局变量
# title = "我是商师人"

demo()

# # 再定义一个全局变量
# name = "小明"
