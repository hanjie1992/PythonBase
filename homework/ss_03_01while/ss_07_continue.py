i = 1
while i <= 5:
    if i == 3:
        print("大虫子，第{0}个不吃了".format(i))
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1
