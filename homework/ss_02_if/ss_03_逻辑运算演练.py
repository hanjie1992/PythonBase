"""
1. 练习1: 定义一个整数变量 age，编写代码判断年龄是否正确
  要求人的年龄在 0-120 之间
"""
age = 100
if age>=0 and age <=120:
    print("年龄正确")
else:
    print("年龄不正确")

"""
2. 练习2: 定义两个整数变量 python_score、c_score，编写代码判断成绩
 要求只要有一门成绩 > 60 分就算合格
"""
python_score = 50
c_score = 50
if python_score > 60 or c_score > 60:
    print("考试通过")
else:
    print("再接再厉！")

"""
3. 练习3: 定义一个布尔型变量 is_employee，编写代码判断是否是本公司员工
 如果不是提示不允许入内
"""
is_employee = True
# 如果不是提示不允许入内
if not is_employee:
    print("非公勿内")