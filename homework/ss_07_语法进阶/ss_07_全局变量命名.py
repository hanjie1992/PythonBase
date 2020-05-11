gl_num = 10
# 再定义一个全局变量
gl_title = "我是商师人"
# 再定义一个全局变量
gl_name = "小明"

def demo():

    # 如果局部变量的名字和全局变量的名字相同
    # pycharm会在局部变量下方显示一个灰色的虚线
    num = 99

    print("{0}".format(num))
    print("{0}".format(gl_title))
    print("{0}".format(gl_name))

# # 再定义一个全局变量
# title = "我是商师人"

demo()