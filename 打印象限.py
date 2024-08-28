# x = float(input('请输入x的值：'))
# y = float(input('请输入y的值：'))
# if(x>0 and y>0):
#     print('点在第一象限')
# elif(x<0 and y>0):
#     print('点在第二象限')
# elif(x<0 and y<0):
#     print('点在第三象限')
# elif(x>0 and y<0):
#     print('点在第四象限')
# elif(x==0 and y==0):
#     print('点在原点')
# else:
#     print('点在坐标轴上')
x = float(input('请输入x的值：'))
y = float(input('请输入y的值：'))
if(x>0):
    if(y>0):
        print("点在第一象限")
else:
    if(x<0):
        if(y>0):
            print('点在第二象限')
if(x<0):
    if(y<0):
        print('点在第三象限')
else:
    if(x>0):
        if(y<0):
            print('点在第四象限')
if(x==0):
    if(y==0):
        print('点在原点')
    else:
        print('点在坐标轴上')