"""
    练习
    一张纸的厚度是0.01毫米
    请问对折多少次，可以超过珠穆朗玛峰8848.43米
"""
thickness = 0.01 / 1000
number = 0
while thickness < 8844.43:
    thickness *= 2
    number += 1
    print(number)
