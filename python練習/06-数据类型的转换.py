# 进制转换  将 int 类型以不同的禁止表现出来
# 类型转换  将 一个类型的数据转换为其他类型的数据
# int ==> str  str ==> int  bool == > int  int ==>  floot

age = input('请输入你的年龄：')
# 原因：input接受到的用户输入，都是str 字符串类型
# 在Python里，如果字符串和数字做加法运算，会直接报错
# 把字符串类型的变量age 转换成为数字类型的age
# print(age + 1) 错误
print(type(age))


new_age = int(age)
print(type(new_age))
print(type(new_age+1))

# 为什么要转换数据类型：因为不同的数据类型，进行运算时，他们的运算规则是不一样的。