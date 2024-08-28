# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1³ + 5³ + 3³，因此 153 就是一个水仙花数。那么如何求 1000 以内的水仙花数（3 位数）。
def test():
    for num in range(100, 1000):
        i = num // 100
        j = num // 10 % 10
        k = num % 10
        if i ** 3 + j ** 3 + k ** 3 == num:
            print(str(num) + "是水仙花数")
test()