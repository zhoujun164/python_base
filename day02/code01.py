"""
逻辑运算符 与and  或or   非not
身份运算符
"""
# and 只有两个都为真 结果才真
print(True and True)
print(False and False)
print(True and False)
print(False and True)

# or 只有两个都为假 结果才假
print(True or True)
print(False or False)
print(True or False)
print(False or True)

# not  结果取反
print(not True)
print(not False)

# 短路逻辑
# 如果第一个条件不满足，则不再考虑第二个条件
print(1 > 2 and input("请输入：") == "a")

# 如果第一个条件满足，则不再考虑第二个条件
print(1 < 2 or input("请输入：") == "a")

# 建议（启发）：尽量将耗时判断，放在后面，（因为可能不执行）

print("身份运算符")

# 身份运算符
num01 = 800
num02 = 900
num03 = num01
print(num01 is num02)
print(id(num01) == id(num02))
