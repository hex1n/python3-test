"""
演示input语句
获取键盘的输入信息
"""

name = input("请告诉我你是谁?")
print("我知道了,你是:%s" % name)

# 输入数字类型
num = input("请告诉我你的密码:")
print("你的密码类型是:", type(num))
# 数据类型转换
print("你的密码类型是:", type(int(num)))
