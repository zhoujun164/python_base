"""
    练习 计算最大数

    num01 = 8
    num02 = 6
    num03 = 10
    num04 = 5
"""
num01 = 8
num02 = 6
num03 = 10
num04 = 5

max_value = num01
if max_value < num02:
    max_value = num02
    if max_value < num03:
        max_value = num03
        if max_value < num04:
            max_value = num04
            print(max_value)
