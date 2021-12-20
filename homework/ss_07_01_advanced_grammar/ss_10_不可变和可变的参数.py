
gl_num = 99
gl_list = [4, 5, 6]
def demo(gl_num, gl_list):
    print("函数内部的代码")
    # 在函数内部，针对参数使用赋值语句，不会修改到外部的实参变量
    gl_num = 100
    gl_list = [1, 2, 3]
    print(gl_num)
    print(gl_list)
    print("函数执行完成")

demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
