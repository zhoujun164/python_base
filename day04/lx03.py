"""
    练习。：在控制台中获取一个字符串，打印每个字符串的编码值
    练习2：在控制台中循环输入编码值，显示字符，只到输入为负数时，退出
"""
str_str = input("输入个字符串:")
for i in str_str:
    print(ord(i))

# 练习2：在控制台中循环输入编码值，显示字符，只到输入为负数时，退出
while True:
    number = int(input("请输入编码值:"))
    if number < 0:
        break
else:
    print(chr(number))
