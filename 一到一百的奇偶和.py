# s=0
# s1=0
# for i in range(1,101):
#     if(i%2==0):
#         s+=i
#     else:
#        s1+=i
# print("一到一百的偶数和为：",s)
# print("一到一百的奇数和为：",s1)

s2=0
s3=0
z=0
while(z<=100):
    if(z%2==0):
        s2+=z
    else:
       s3+=z
    z+=1
print("一到一百的偶数和为：",s2)
print("一到一百的奇数和为：",s3)