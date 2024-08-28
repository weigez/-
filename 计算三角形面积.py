import math
a = int(input("请输入三角形第一条边："))
b = int(input("请输入三角形第二条边："))
c = int(input("请输入三角形第三条边："))
if(a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a):
    s = 1/2*(a+b+c)
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print('此三角形的面积为：',area)
else:
    print('输入的三边不构成三角形')