# s = int(input("你要输入几个数："))
# num = []
# for i in range(1,s+1):
#     n = int(input("请输入一个整数："))
#     if n%2==1:
#         num.append(n)
# print("奇数为：",num)


s = int(input("你要输入几个数："))
num = []
a = 1
while a<=s:
    n = int(input("请输入一个整数："))
    if n%2==1:
        num.append(n)
    a+=1
print("奇数为：",num)