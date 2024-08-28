# n = int(input("请输入一个整数："))
# s = 0
# for i in range(1,n+1):
#     s+=i
# print("1到n的整数和为：",s)

n = int(input("请输入一个整数："))
s = 0
a = 1
while a<=n:
    s+=a
    a+=1
print("1到n的整数和为：",s)