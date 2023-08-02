"""
list列表常用操作示例
"""

my_list = ['nihao', 'haha', 'haha', 'haha', 'heihei', 'hello']
# 查找某元素在列表内的下标索引
index = my_list.index('haha')
print(f"haha的索引值是:{index}")

print("=========================")

# 修改特定下标索引的值
my_list[0] = 'hehe'
print(f"修改后列表 结果是:{my_list}")
print("=========================")

# 在指定下标位置插入新元素
my_list.insert(0, 'first')
print(f"在指定位置插入新元素:{my_list}")
print("==========================")

# 在列表的尾部追加 ‘单个’新元素
my_list.append('lastEle')
print(f"在列表的尾部追加新元素:{my_list}")
print("==========================")

# 在列表的尾部追加一批新元素
my_list.extend(["new1", "new2", "new3", "new4"])
print(f"在列表的尾部追加一批新元素:{my_list}")
print("==========================")

# 删除指定下标索引的元素(2种方式)
del (my_list[len(my_list) - 1])  # 删除列表最后一个元素
print(f"使用del删除列表最后一个元素:{my_list}")
remove_ele = my_list.pop(0)  # 删除列表第一个元素 并返回删除的元素
print(f"使用pop删除列表第一个元素:{my_list},取出的元素是:{remove_ele}")
print("===========================")

# 删除某元素在列表中的第一个匹配项
my_list.remove('haha')  # 只删除匹配到的第一个
print(f"通过remove删除某元素:{my_list}")
print("===========================")

# 统计列表内某元素的数量
match_num = my_list.count('haha')
print(f"统计列表中haha的数量:{match_num}")
print("===========================")

# 统计列表中全部元素数量
ele_num = len(my_list)
print(f"统计列表中有多少个元素:{ele_num}")
print("===========================")

# 清空列表
my_list.clear()
print(f"清空列表:{my_list}")
print("===========================")
