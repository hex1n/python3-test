"""
函数的嵌套调用示例
"""


# 定义函数func_b

def func_b():
    print("this is func_b")


# 定义函数func_a 并在内部调用func_b
def func_a():
    func_b()
    print("this is func_a")


func_a()
