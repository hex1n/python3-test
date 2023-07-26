"""
演示Python判断语句: if语句的基本格式使用
"""
age = 30
if age == 31:
    print("我已经成年了")
    print("即将步入大学生活")
elif age > 32:
    print("do something 1")
elif age < 50:
    print("do something----")
else:
    print("grow up")
print("时间真快啊")

# 判断语句的嵌套
num = 4
num1 = 2
if num > 0:
    print("do something 2")
    if num < num1:
        print("do something 3")
    else:
        print("......")
else:
    print("end")
