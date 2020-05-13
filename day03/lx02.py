"""
练习
在控制台中获取一个月份，
返回改月的天数
"""
season = int(input("输入一个月份:"))
if season < 1 or season > 12:
    print("您输入的月份有误！")
elif season == 2:
    print(str(season) + "月" + "有28天")
elif season == 4 or season == 6 or season == 9 or season == 11:
    print(str(season) + "月" + "有30天")
else:
    print(str(season) + "月" + "有31天")
