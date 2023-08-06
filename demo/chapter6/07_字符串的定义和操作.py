"""
字符串的操作示例
"""

# 通过下标获取特定位置字符
name = "zhangsan"
print(f"获取第一个z:{name[0]}")
print(f"获取最后一个n:{name[-1]}")
print("===========================")

# index 方法 -  查询某个字符的下标
index = name.index('s')
print(f"s 的起始下标是:{index}")
print("===========================")

#  replace 方法
# 将zh 替换为li
new_name = name.replace('zh', 'li')
print(f"将zh替换为li:{new_name}")
print("===========================")

# split 方法
org_str = 'zhangsan lishi wangwu'
split_str = org_str.split(' ')
print(f"将字符串切分为list:{split_str}")
print("===========================")

# strip方法 - 去前后空格
strip_str = ' nihao hello  '.strip()
print(f"去前后空格:{strip_str}")
print("===========================")

# strip方法 - 去前后指定字符串
org_str = '12zhangsan lishi wangwu21'
strip_str = org_str.strip('12')
print(f"去前后指定字符串:{strip_str}")
print("===========================")

# 统计字符串中某字符串的出现次数
org_str = 'zhangsan lishi wangwu'
count = org_str.count('an')
print(f"统计字符串中an出现次数:{count}")
print("===========================")

# 统计字符串的长度
str_len = len(org_str)
print(f"统计字符串长度:{str_len}")
print("===========================")
