"""
练习
温度换算器（华氏度，摄氏度，开氏度）
摄氏度 = （华氏度 - 32） / 1.8
华氏度 =  摄氏度 × 1.8 + 32
开氏度 = 摄氏度 + 273.15
--在控制台中获取华氏度，计算开氏度
--在控制台中获取摄氏度，计算华氏度
--在控制台中获取摄氏度，计算开氏度
"""
fahrenheit = float(input("输入华氏度："))
centigrade = (fahrenheit - 32) / 1.8
print("摄氏度为：" + str(centigrade))

centigrade = float(input("输入摄氏度："))
fahrenheit = centigrade * 1.8 + 32
print("华氏度为："+str(fahrenheit))


fahrenheit = float(input("输入摄氏度："))
kelvin = fahrenheit + 273.15
print("开氏度为："+str(kelvin))