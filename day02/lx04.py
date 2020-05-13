"""
在控制台输入一个整数
如果是奇数，则显示奇数，否则显示偶数
"""
int_number = int(input("请输入一个整数:"))
if int_number % 2 == 0:
    print("这是一个偶数:" + str(int_number))
else:
    print("这是一个奇数:" + str(int_number))

"""
练习2
在控制台中输入一个年份
如果是闰年，则显示闰年，否则显示平年
闰年判断：
条件1：年份能被4整除，但是不能被100整除
条件2：年份能被400整除，

"""
int_years = int(input("输入一个年份"))
if int_years % 4 == 0  and int_years % 100 != 0  or  int_years % 400 == 0:
    print(str(int_years)+"年是一个闰年")
else:
    print(str(int_years)+"年是一个平年")
