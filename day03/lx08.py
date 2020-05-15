"""
    练习  猜数字游戏
    猜数字，系统产生1--100之间的随机数
    让用户重复猜测，只到才对为止。
    猜数字2.0
    最多只能猜10次
"""
import random

random_number = random.randint(1, 100)
print("系统已随机从1-100中随机分配一个数！\n 请输入你猜测的数字:")
formnumber = 1
while formnumber <= 10:
    number = int(input("请猜第" + str(formnumber) + "次："))
    if number == random_number:
        print("恭喜你，猜对了")
        break
    elif number > random_number:
        print("不好意思，你猜的数有点大哦，请再猜一次！")
    else:
        print("不好意思，你猜的数有点小，请再猜一次")
    formnumber += 1
else:
    print("哎呀！超过10次了，不能再猜了")
