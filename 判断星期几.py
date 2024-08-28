def get_weekday(letter):
    letter = letter.lower()  # 将输入的字母转换为小写
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    for weekday in weekdays:
        if weekday.startswith(letter):
            return weekday

    return "Invalid input"  # 如果输入的字母不是星期几的首字母，则返回无效输入


# 测试代码
letter = input("请输入星期几的第一个字母：")
weekday = get_weekday(letter)
print("输入的字母对应的星期几是：", weekday)