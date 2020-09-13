
def multiple_table():
    """
    九九乘法表
    :return: 123
    """
    # 1. 打印 9 行小星星
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            # print("*", end="")
            print("{0} * {1} = {2}".format(col, row, col * row), end="\t")
            col += 1
        # print("%d" % row)
        print("")
        row += 1

# import keyword
# print(keyword.kwlist)
# multiple_table()
