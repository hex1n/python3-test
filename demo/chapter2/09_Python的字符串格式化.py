# 通过占位的形式,完成拼接
name = "张三"
message = "你好:%s" % name
print(message)

# 通过占位的形式,完成数字和字符串的拼接
class_num = 57
avg_salary = 10000
message = "哈哈:%s,嘿嘿:%s" % (class_num, avg_salary)
print(message)

name = "可乐"
setup_year = 2000
stock_price = 19.11
message = "%s,成立于:%d,股价是:%f" % (name, setup_year, stock_price)
print(message)

# 数字精度控制
num1 = 11
num2 = 11.345
print("数字11宽度限制5,结果:%5d" % num1)
print("数字11宽度限制1,结果:%1d" % num1)
print("数字11.345宽度限制7,小数精度2,结果:%7.2f" % num2)
print("数字11.345不限制宽度,小数精度2,结果:%.2f" % num2)

# 快速写法
name = "张三"
setup_year = 2000
stock_price = 19.99
print(f"我是{name},哈哈哈哈{stock_price},你好{stock_price}")

# 表达式的格式化
print("1*1的结果是:%d" % (1 * 1))
print(f"1*1的结果是:{1 * 1}")
print("字符串在Python中的类型是:%s" % type('字符串'))
