str1 = 'abcdefg'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        break
    print(i)
else:
    print('break时，此句无法打印输出')