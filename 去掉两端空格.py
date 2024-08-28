import re
def remove_spaces_and_numbers(string):
    # 去除空格
    string = string.replace(" ", "")

    # 去除数字
    string = re.sub(r"\d", "", string)

    return string


# 测试
test_str = '20101 hello python 10310'
result = remove_spaces_and_numbers(test_str)
print(result)  # 输出: "HelloWorld"
