#赋值运算符的执行顺寻，从右到左

name = '张三' #将’张三‘赋值给变量name
age = 20 #将20赋值给变量age

a=b=c=d=100 #a,b,c,d的值同时赋值为100,链式赋值
print(name,age,a,b,c,d)

# 系列解包赋值
name1,age1='乌克兰',2022  #元组分解赋值
print(name1,age1)

[name2,age2] = ['俄罗斯',2022] #列表分解赋值
print(name2,age2)

e,f,g,h = 'room'  #字符串分解赋值
print(e,f,g,h)

#扩展的字符串解包赋值
t,*o = 'about us'
print(t,o)
