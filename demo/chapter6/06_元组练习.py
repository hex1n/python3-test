"""
元组练习:
    需求: 定义一个元组, 内容是:('周杰伦',11,['football','music']),记录的是一个学生的信息(姓名、年龄、爱好)

    通过元组的功能(方法) 对其进行:
        1. 查询其年龄所在的下标位置
        2. 查询学生的姓名
        3. 删除学生爱好中的football
        4. 增加爱好:conding到爱好list内

"""

my_tuple = ('周杰伦', 11, ['football', 'music'])

# 查询其年龄所在的下标位置
stu_age_index = my_tuple.index(11)
print(f"年龄的下标位置是:{stu_age_index}")

# 查询学生的姓名
stu_name = my_tuple[0]
print(f"学生的姓名是:{stu_name}")

# 删除学生爱好中的football
my_tuple[2].remove('football')
print(f"删除学生爱好中的football:{my_tuple}")

# 增加爱好:conding到爱好list内
my_tuple[2].append('conding')
print(f"增加爱好:conding到爱好list内:{my_tuple}")
