# -*- coding: utf-8 -*-

# 遍历字符串
for i in 'Hello':
    print(i, end=',')
print('\n')

# 内置函数，直接就可以使用range()函数，产生一个[n,m的整数序列]，包含n，不包含m
for i in range(1, 11):  # 1 - 10
    print(i, end=',')
print('\n')
for i in range(1, 11):
    if i % 2 == 0:
        print(i, '是偶数''\n')
print('\n')

# 计算1-10之前的累加和
s = 0  # 用于存储累加和
for i in range(1, 11):
    s += i  # 相当于s = s + i
print('1-10之间的累加和为:', s)  # 不在跟for 进入非循环体

print('------------100-999之间的水仙花数-----------')
'''
153
3*3*3+5*5*5+1*1*1 = 153 这个叫水仙花数

'''

for i in range(100, 1000):
    sd = i % 10  # 获取个位上的数字
    tens = i // 10 % 10  # 获取十位的数字
    hundred = i // 100  # 获取百位上的数字
    if sd ** 3 + tens ** 3 + hundred ** 3 == i:
        print(i)
'''
 for 循环变量 in 遍历对象：
    语句块1          
else
    语句块2
-  else语句只在循环正常结束后才执行
-  通常与break和continue语句一起使用 
'''
y = 0
for i in range(1, 11):
    y += i
else:
    print('1-10之间的累加和为:', y)
