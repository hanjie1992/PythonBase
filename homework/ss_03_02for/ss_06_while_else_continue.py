i = 1
while i <= 5:
    if i == 3:
        print('i==3的时候退出当前循环')
        i += 1
        continue
    print(i)
    i += 1
else:
    print('continue时，此句可以打印输出')
