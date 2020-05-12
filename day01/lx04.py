"""
   练习04
   在控制台中获取一个商品单价
   再获取一个商品的数量
   再获取一个付款金额
   最后计算应找回多少钱？
"""
fl_danjia = input("这个商品的单价为：")
int_shul = input("请输入你所购买商品的数量：")
fl_fuk = input("输入你的付款金额：")
fl_danjia = float(fl_danjia)
int_shul = int(int_shul)
fl_fuk = float(fl_fuk)
fl_js = fl_danjia * int_shul
fl_zl = fl_fuk - fl_js
if fl_fuk == fl_js:
    print("谢谢惠顾！欢迎下次光临！")
elif fl_fuk > fl_js:
    print("您所付款的金额为" + str(fl_fuk) + "元" + '\n'"找您" + str(fl_zl) + "元")

else:
    print("您所付款的金额为" + str(fl_fuk) + "元" + '\n'"您还需要添加" + str(-(fl_zl)) + "元")
