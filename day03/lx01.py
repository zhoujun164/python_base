"""
联系
在控制台中获取一个月份
打印季节（春1-3 夏4-6，秋7-9，冬10-12）
"""
month = int(input("请输入月份："))
#
# if 1 <= month <= 3:
#     print("春天")
# elif 4 <= month <= 6:
#     print("夏天")
# elif 7 <= month <= 9:
#     print("秋天")
# elif 10 <= month <= 12:
#     print("冬天")
# else:
#     print("您输入的月份有问题")

# 代码优化
if month < 1 or month > 12:
    print("您输入的月份有问题")
elif month <= 3:
    print("这是春天")
elif month <= 6:
    print("这是夏天")
elif month <= 9:
    print("这是秋天")
else:
    print("这是冬天")
