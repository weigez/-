# n = int(input("请输入学生人数："))
# sum = 0
# for i in range(1,n+1):
# 	grade = float(input("请输入学生成绩："))
# 	sum+=grade
# 	 i+=1
# ave = sum/n
# print("学生成绩的平均值为：%.2f"%ave)


n = int(input("请输入学生人数："))
sum = 0
s=1
while s<=n:
	grade = float(input("请输入学生成绩："))
	sum+=grade
	s+=1
ave = sum/n
print("学生成绩的平均值为：%.2f"%ave)