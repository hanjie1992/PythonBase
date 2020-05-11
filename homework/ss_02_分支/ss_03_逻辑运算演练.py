# 练习1: 定义一个整数变量 age，编写代码判断年龄是否正确
age = 11

# 要求人的年龄在 0-120 之间
"""
10000
age >= 0 or age <= 120
age >= 0 and age <= 120
"""
# if age >= 0 and age <= 120:
#     print("年龄正确")
# else:
#     print("年龄不正确")
a = 1
b = 1
c = 1
d = 1
if a==1 or b==2 and c==2 or d==2:
    print("年龄正确")
else:
    print("年龄不正确")

if ((a==1) or (b==2)) and ((c==2) or (d==2)):
    print("年龄正确")
else:
    print("年龄不正确")