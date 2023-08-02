"""
循环语句中的中断控制: break 和 continue
"""

# continue 示例
for i in range(1, 6):
    print("语句1")
    continue
    print("语句2")  # 因为上面的continue 不会执行本行代码
print("=====================================")

# continue 嵌的嵌套应用
for i in range(1, 6):  # 1
    print("1")
    for j in range(1, 6):  # 2
        print("2")
        continue  # 此处的continue控制的是当前循环 #2
        print("3")  # 本行代码不会执行
    print("4")
print("=====================================")

# break 示例
for i in range(1, 100):
    print("语句1")
    break
    print("语句2")
print("语句3")
# 上面代码在执行了语句1后直接执行语句3
print("=====================================")

# break 嵌套示例
for i in range(1, 6):
    print("语句1")
    for j in range(1, 6):
        print("语句2")
        break
        print("语句3")
print("语句4")
