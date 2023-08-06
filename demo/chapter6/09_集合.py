"""
集合示例
"""
# 定义集合
{'你好', '哈哈'}

# 添加新元素
my_set = {'你好', '哈哈', '哈哈'}
my_set.add('呵呵')
print(f"添加新元素:{my_set}")
print("=======================")

# 移除元素
my_set.remove('你好')
print(f"移除元素:{my_set}")
print("=======================")

# 随机取出一个元素
ele = my_set.pop()
print(f"随机取出一个元素:{ele}")
print("=======================")

# 清空集合
my_set1 = {'你好', '哈哈'}
my_set1.clear()
print(f"清空集合:{my_set1}")
print("=======================")

# 取2个集合的差集
my_set2 = {'你好', '哈哈'}
my_set3 = {'你好', '哈哈', '嘻嘻'}
result = my_set3.difference(my_set2)
print(f"取2个集合的差集:{result}")
print("=======================")

# 消除2个集合的差集 - 在集合1 的内部删除 集合2
my_set2 = {'你好', '哈哈'}
my_set3 = {'你好', '哈哈', '嘻嘻'}
my_set3.difference_update(my_set2)
print(f"消除2个集合的差集my_set2:{my_set2}")
print(f"消除2个集合的差集my_set3:{my_set3}")
print("=======================")

# 合并2个集合为一个
my_set2 = {'你好', '哈哈'}
my_set3 = {'你好1', '哈哈1', '嘻嘻'}
result = my_set2.union(my_set3)
print(f"合并2个集合为一个:{result}")
print("=======================")

# 统计集合元素数量
my_set2 = {'你好', '哈哈'}
count = len(my_set2)
print(f"统计集合元素数量:{count}")
print("=======================")
