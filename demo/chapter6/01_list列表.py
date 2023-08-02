"""
list列表示例
"""
name_list = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']

print(name_list)
print(type(name_list))

print("==========================")
my_list = ['zhangsan', 66, True]
print(my_list)
print(type(my_list))

print("==========================")
# 嵌套列表
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list)
print(type(my_list))
print("===========================")

# 通过下标索引取出对应位置的数据 --- 正序取
my_list = ['tom', 'lily', 'rose']
num = len(my_list)
for x in range(num):
    print(my_list[x])

print("==========================")

# 通过下标索引取出对应位置的数据 --- 倒序取
my_list = ['tom', 'lily', 'rose']
num = len(my_list)
for x in range(num):
    print(my_list[-x - 1])

print("==========================")

# 取嵌套列表
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
count = len(my_list)
for x in range(count):
    for j in range(len(my_list[x])):
        print(my_list[x][j])
