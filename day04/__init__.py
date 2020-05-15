"""
    练习
    累加1--100 之间能被3 整除的整和数
"""
sum = 0
for item in range(1, 100):
    if item % 3 == 0:
        sum += item
print(sum)
