# 定义一个外部函数
def func_out(num1):
    # 定义一个内部函数
    def func_inner(num2):
        # 内部函数使用了外部函数的变量(num1)
        result = num1 + num2
        print("结果是:", result)
    # 外部函数返回了内部函数，这里返回的内部函数就是闭包
    return func_inner

# 创建闭包实例
f = func_out(1)
# 执行闭包
f(2)
f(3)