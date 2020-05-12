"""
   练习03
   在控制台中输入姓名，年龄，性别，成绩
   最后在打印汇总输入的信息
"""

my_name = input("请输入你的姓名：")
my_age = input("请输入你的年龄：")
my_sex = input("请输入你的性别:")
my_class = input("请输入你的成绩：")
my_name = str(my_name)
my_age = int(my_age)
my_sex = str(my_sex)
my_class = float(my_class)
print("我的姓名：" + my_name + ",年龄是：" + str(my_age) + ",性别是：" + my_sex + ",成绩是：" + str(my_class))
#format() 格式化字符串
print("你的姓名是{}，年龄是{}，性别是{}，成绩是{}".format(my_name,my_age,my_sex,my_class))
