row = int(input('row='))
col = int(input('col='))
for i in range(1, row + 1):
    # 负责打印前导空格
    for j in range(1, row - i + 1):
        print(' ', end='')
    # 负责打印星号
    for j in range(col):
        print('*', end='')
    # 换行
    print()
