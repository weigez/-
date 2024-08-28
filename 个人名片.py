
# name='余银媛'
# age=21
# h=160
# print('核对以下信息：')
# print('-'*40)
# print()
# print('姓名','年龄','身高',sep='    ')
# print()
# print(name,age,h,sep='    ',end="/信息核对完毕！")
# print()
# print()
# print('-'*40)
for i in range(5):
    name = str(input("请输入你的姓名："))
    age = int(input("请输入你的年龄："))
    sex = str(input("请输入你的性别："))
    lianxifs = int(input("请输入你的联系方式："))
    print(name,age,sex,lianxifs)
    print("信息输入完毕!")
