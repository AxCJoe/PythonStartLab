# coding:utf-8
# 保留字不能做变量 不能被赋值 True  False 等
true = '真'
# True = '真' # SyntaxError: cannot assign to True

import keyword

print(keyword.kwlist)

my_name_1 = 'it is'  # my_name_1就是标识符
# 1_my_name = 'it is'  #以数字开头不符合规范报错1_my_name_就是标识符

# 连续赋值

no = number = 1024
print(no, number)
print(id(no))
print(id(number))

# python可以动态的修改数据类型
luck_number = 8
print(type(luck_number))

luck_number = 'it is 8'
print(type(luck_number))

# 浮点数不确定的尾数问题
print(0.1 + 0.2)  # 0.30000000000000004
print(round(0.1 + 0.2, 1))  # 保留一位小数  0.3

# 复数类型在科学计算中十分常见
x = 123 + 465j
print('实数部分:', x.real)
print('虚数部分:', x.imag)

# 单行字符串
info = '谢谢你的关心'
info2 = "谢谢你的关心2"
print(info, info2)

# 多行字符串
info3 = '''我的名字叫JOE
希望你能到这个信息

'''

info4 = """我的名字叫Joe
欢迎与我交流

"""
print(info3, info4)
