"""
   练习01
   在控制台中获取小时/分钟/秒，计算总秒数
"""
hour = int(input("请输入小时"))
minute = int(input("请输入分钟"))
second = int(input("请输入秒数"))
result = hour * 3600 + minute * 60 + second
print("你的总秒数为：" + str(result))

"""
在控制台中获取一个总秒数
计算几个调式零几分钟零几秒
"""

int_second = int(input("请输入一个总秒数："))
int_hour = int_second // 3600
int_minute = int_second % 3600 // 60
int_second = int_second % 3600 % 60
print(str(int_hour) + "时" + str(int_minute) + "分" + str(int_second) + "秒")
