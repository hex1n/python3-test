"""
定义一个列表,内容是:[1,2,3,4,5,6,7,8,9,10]
  1. 遍历列表,取出列表内的偶数,并存入一个新的列表对象中
  2. 使用while循环和 for 循环各操作一次
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
index = 0
while index < len(my_list):
    if my_list[index] % 2 == 0:
        new_list.append(my_list[index])
    index += 1

print(f"使用while遍历获取列表中的偶数:{new_list}")

print("====================================")
new_list = []
for x in my_list:
    if x % 2 == 0:
        new_list.append(x)

print(f"使用for遍历获取列表中的偶数:{new_list}")
