"""
   练习02
   古代的称约一斤16两
   在控制台中输入两数，换算出是几斤几两
"""
total_liang = int(input("请输入你的总两数："))
int_jing = total_liang // 16
int_liang = total_liang % 16
print(str(int_jing) + "斤零" + str(int_liang) + "两")
