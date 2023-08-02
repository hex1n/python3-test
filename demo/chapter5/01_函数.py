"""
函数示例
"""

# 统计字符串长度,不使用内置函数len()
str1 = "hi"
str2 = "hello"
str3 = "python"
str4 = "good luck"


def count_str(data):
    count = 0
    for e in data:
        count += 1
    print(f"传入的字符长度是:{count}")


count_str(str1)
count_str(str2)
count_str(str3)
count_str(str4)
print("======================")


# 定义一个函数输出相关信息
def say_hi():
    print("hi")


# 调用函数
say_hi()

print("=======================")


# 函数传入参数
def add(x, y):
    result = x + y
    print(f"{x}+{y}的结果是:{result}")


add(5, 6)

print("==========================")


# 返回值
def add(x, y, z):

    return x + y + z


total = add(1, 2, 3)
print(f"total:{total}")

print("===========================")


# 返回None类型
def test_none():
    return None


none_ = test_none()
print(f"None类型:{type(none_)}")

print("==========================")


# None用于if判断
def check_age(age):
    if age > 18:
        return "success"
    else:
        return None


result = check_age(16)
if not result:
    # 进入if表示result是None 也就是False
    print("年龄小于18")

print("=====================")

# None 用于声明无初始内容的变量
name = None

