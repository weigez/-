n=int(input("随机数: "))
print("%d的因数是:"%n,end="")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
print()



# a = int(input("请输入第一个正整数："))
#
# b = int(input("请输入第一个正整数："))
#
# while (a):
#
#     if a < b:
#         t = a
#
#         a = b
#
#         b = t
#
#     a %= b
#
# print("这两个正整数的最大公约数为：", b)