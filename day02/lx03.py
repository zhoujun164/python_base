"""
闰年判断：
条件1：年份能被4整除，但是不能被100整除
条件2：年份能被400整除，
在控制台中获取年份
判断是否为闰年，如果是显示为True ，否则现实False
"""

int_years = int(input("输入一个年份:"))
result = int_years % 4 == 0 and int_years % 100 != 0 or int_years % 400 == 0
print(result)

"""
在控制台中获取一个4位整数1234
计算美味相加和 1 +2+3+4 > 10

"""
int_number = int(input("输入一个四位数的整数，如1234："))#
#方法一：
int_a = int_number // 1000  # 获取千位数
int_b = int_number // 100 % 10  # 获取百位数
int_c = int_number // 10 % 10  # 获取十位数
int_d = int_number % 10  # 获取个位数
result = int_a + int_b + int_c + int_d
print(result)

#方法二：
result = int_number % 10
result += int_number // 10 % 10
result += int_number // 100 % 10
result += int_number // 1000 % 10
print(result)
