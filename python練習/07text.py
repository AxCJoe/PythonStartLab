print("你好我是\n我是\n我是")

print(r"你好我是\n我是\n我是")  # 于大写的R效果一样 你好我是\n我是\n我是

print(R"你好我是\n我是\n我是")  # 于小写的r效果一样 你好我是\n我是\n我是

# -------------------------------------------------------------------------
s = '3.14+3'
print(s, type(s))
x = eval(s)  # 执行了加法运算
print(x, type(x))  # 3.14+3 <class 'str'>  6.140000000000001 <class 'float'>

print(s, eval(s))

# eval()函数经常和input()函数一起使用，用来获取用户输入的数值型
age = eval(input("请输入你的年龄："))  # 将字符串类型转成int类型，相当于int(age)
print(age, type(age))

height = eval(input('你的身高是多少：'))  # 将字符串类型转换成了float类型，相当于float(height)
print(height, type(height))

# 使用eval报错的情况
hello = '北京欢迎你'
print(hello) # 北京欢迎你
print(eval('hello'))  # 如果这么写会报 NameError: name 'hello' is not defined 错误
'''
理由是 eval 去掉了'' 变成了hello变量，而hello这个变量没有定义，
想正常定义需要在上面生成就不报错了

'''

