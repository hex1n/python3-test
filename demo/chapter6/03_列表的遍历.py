"""
list列表遍历的示例
"""

# 使用while循环遍历列表
my_list = ['nihao', 'hello', 'haha', 'hehe']
index = 0
while index < len(my_list):
    print(f"使用while遍历列表:{my_list[index]}")
    index += 1

print("====================")

# 使用 for循环 遍历列表
for x in my_list:
    print(f"使用for循环遍历列表:{x}")
