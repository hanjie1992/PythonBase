# 重复打印5行星星
# j表示行号
j = 0
while j <= 4:
    # 一行星星的打印
    i = 0
    # i表示每行里面星星的个数，这个数字要和行号相等所以i要和j联动
    while i <= j:
        print('*', end='')
        i += 1
    print()
    j += 1