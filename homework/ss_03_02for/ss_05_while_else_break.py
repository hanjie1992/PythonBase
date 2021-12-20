i = 1
while i <= 5:
    if i == 3:
        print('i==3的时候退出循环')
        break
    print(i)
    i += 1
else:
    print('break时，此句无法打印输出')