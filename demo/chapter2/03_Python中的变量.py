"""
演示Python中的变量的相关操作
"""
# 定义一个变量，用来记录钱包余额
money = 50
# 通过print 语句输出变量记录的内容
print("钱包还有：", money)

# 买了一个冰激凌，花费10元
money = money-10
print("买了冰淇淋花费10元，还剩余：", money, "元")

# 练习 钱包余额(变量名：money)，初始余额 50 在购买了冰淇淋10元 可乐5元 后钱包余额还剩多少元

money = 50
ice = 10
cola = 5
money = money-ice-cola
print("当前钱包余额:", money, "元")
print("购买了冰淇淋，花费：", ice, "元")
print("购买了可乐，花费：", cola, "元")
print("最终，钱包剩余：", money, "元")

