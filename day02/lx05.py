"""
练习01
温度换算器（华氏度，摄氏度，开氏度）
摄氏度 = （华氏度 - 32） / 1.8
华氏度 =  摄氏度 × 1.8 + 32
开氏度 = 摄氏度 + 273.15
--在控制台中获取华氏度，计算开氏度
--在控制台中获取摄氏度，计算华氏度
--在控制台中获取摄氏度，计算开氏度
"""
float_hsd = float(input("输入华氏度："))
float_ssd = (float_hsd - 32) / 1.8
print("摄氏度为：" + str(float_ssd))

float_ssd = float(input("输入摄氏度："))
float_hsd = float_ssd * 1.8 + 32
print("华氏度为："+str(float_hsd))


float_hsd = float(input("输入摄氏度："))
float_ksd = float_hsd + 273.15
print("开氏度为："+str(float_ksd))