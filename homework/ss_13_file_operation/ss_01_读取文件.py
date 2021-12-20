# 1. 打开文件
file = open("README")
# file = open("E:\workspace\pyhton_base\homework\ss_13_file_operation\README")
# file = open("E:\\workspace\\pyhton_base\\homework\\ss_13_file_operation\\README")

# 2. 读取文件内容
text = file.read()
print(text)

# 3. 关闭文件
file.close()
