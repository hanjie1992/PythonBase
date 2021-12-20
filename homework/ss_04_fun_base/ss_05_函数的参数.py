def sum_2_num():
    """对两个数字的求和"""
    num1 = 11
    num2 = 21
    result = num1 + num2
    print("{0} + {1} = {2}" .format(num1,num2,result))
sum_2_num()

# def sum_2_num(num1, num2):
#     """对两个数字的求和"""
#     result = num1 + num2
#     print("{0} + {1} = {2}" .format(num1,num2,result))
# sum_2_num(3, 4)

first_num1 = int(input("请输入第1个数字："))
second_num2 = int(input("请输入第2个数字："))
def sum_2_num(num1, num2):
    """对两个数字的求和"""
    result = num1 + num2
    print("{0} + {1} = {2}".format(num1, num2, result))
    return result
a = sum_2_num(first_num1, second_num2)
if a>30:
    print(a*0.8)
else:
    print(a)