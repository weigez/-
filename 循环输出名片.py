n = int(input("请输入你要循环的次数："))
i = 1
while(i<=n):
    name = input("请输入你的姓名：")
    age = int(input("请输入你的年龄："))
    height = int(input('请输入你的身高：'))
    print('核对以下信息：')
    print('-'*40)
    print()
    print('姓名','年龄','身高',sep="   ")
    print()
    print(name,age,height,sep='   ',end='/信息输入完毕！')
    i+=1
    print()
    print()
    print('-'*40)