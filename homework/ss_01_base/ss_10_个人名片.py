"""
在控制台依次提示用户输入：姓名、公司、职位、电话、电子邮箱
"""
name = input("请输入姓名：")
company = input("请输入公司：")
title = input("请输入职位：")
phone = input("请输入电话：")
email = input("请输入邮箱：")

print("*" * 50)
print(company)
print()
print("%s (%s)" % (name, title))  # python2版本格式化输出
print("{0},{1}".format(name, title))  # python3版本格式化输出
print()
print("电话：%s" % phone)
print("电话：{0}".format(phone))
print("邮箱：%s" % email)
print("邮箱：{0}".format(email))
print("*" * 50)

