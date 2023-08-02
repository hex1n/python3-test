"""
tuple 示例
"""
# 定义元组字面量
('元素1', '元素2', 1, 2, False)
# 定义元组变量
t1 = ('元素1', '元素2', 1, 2, False)
# 定义空元组
t2 = ()  # 方式1
t3 = tuple()  # 方式2

print(f"t1的类型是:{type(t1)},{t1}")
print(f"t2的类型是:{type(t2)},{t2}")
print(f"t3的类型是:{type(t3)},{t3}")

print("===========================")
# 定义单个元素的元组  后面需要加 逗号
t4 = ("haha",)
print(f"定义单个元素的元组:{t4}")
print("===========================")

# 元组的嵌套
t5 = ((1, 2, 3), ('haha', 'xixi', 'hehe'), (True, False))
print(f"嵌套元组:{t5}")
print("===========================")

# 下标索引取出内容
ele = t5[1][0]
print(f"取出t5中的haha:{ele}")
# 元组的操作: index() 查找特定元素的第一匹配项- 返回的是索引
t6 = (1, 2, 3, 3, 5, 8, 6)
ele = t6.index(5)
print(f"使用index()取出元组中的5的索引:{ele}")
print("===========================")

# 元组的操作: count 统计方法 统计某个元素在元组内出现的次数
match_num = t6.count(3)
print(f"使用count()统计3在元组中出现的次数:{match_num}")
print("===========================")

# while 遍历元组
index = 0
while index < len(t6):
    print(f"使用while遍历元组数据:{t6[index]}")
    index += 1
print("===========================")

# for 遍历元组
for x in t6:
    print(f"使用for遍历元组数据:{x}")

print("===========================")
