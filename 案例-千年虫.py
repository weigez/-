# lst=[96,97,98,00,99]
# print(lst)
# for index in range(len(lst)):
#     if(str(lst[index])!='0'):
#         lst[index]='19'+str(lst[index])
#     else:
#         lst[index]='200'+str(lst[index])
#
# print('修改后的年份列表：',lst)

lst=[96,97,98,00,99]
lit = []
for i in lst:
    if i!=0:
        i = '19'+str(i)
        lit.append(i)
    else:
        i = '200'+str(i)
        lit.append(i)
print(lit)