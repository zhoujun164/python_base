"""
练习
在控制台中输入圆形的半径
计算面积（3.14 * r的平分） 与周长（2 * 3.14 * r）
"""

float_r = float(input("输入圆形半径:"))
float_d = 3.14 * (float_r ** 2)
float_c = 2 * 3.14 * float_r
print("圆的面积为：{}，圆的周长为：{}".format(str(float_d), str(float_c)))
