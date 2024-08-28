lst = ['+','-','*','/']
num1 = float(input("请输入第一个数字："))
fuhao=input("请输入运算符：")
num2 = float(input("请输入第二个数字："))
if fuhao not in lst:
    print("请输入正确的符号")
else:
    if fuhao=='+':
        result = num1+num2
    elif fuhao=='-':
        result = num1-num2
    elif fuhao=='*':
        result = num1*num2
    elif fuhao=='/':
        result = num1/num2
    print(num1,fuhao,num2,'=',result)