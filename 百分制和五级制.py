score = int(input("请输入你的成绩："))
if score>100 or score<10:
    print("没和你开玩笑，认真点")
elif score>=90:
    print("优")
elif score>=80:
    print("良")
elif score>=70:
    print("中")
elif score>=60:
    print("及格")
else:
    print("不及格，下次努力考好点")