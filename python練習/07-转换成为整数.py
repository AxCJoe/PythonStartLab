#  使用int内置类可以将数据转成为整数

a = '31'
b = int(a)
print(a)
print(b)

# 如果字符串不是一个合法的数字，会直接报错
# x = 'hello'
# y = int(x)
# print(y)

x = '1a2c'
y = int(x,16)  #  把字符串1a2c当做十六进制转化成为整数
print(y)  # 6700 打印一个数字，默认使用十进制输出
print(bin(y))

m = 'abc'
n = int(m,16)
print(n)

a = '12'
b = int(a,8) # 把字符的12 当做八进制转换成为整数
print(b)   # 10

a = '12.34'
# 使用内置 float类可以将其他类型数据转换成为float浮点数
b = float(a)  # b = float(a)  b=float(a)
print(b+1)
# 如果字符串不能被转换成为有效的浮点数，会报错
#c = float('hello')
#print(c)

c = 101
print(float(c)) # 101.0

m = float('12') # 将字符串转换成为浮点数
n = float(12)   # 将整数型数字转换成为浮点数
print(m,n)

# 07-转换成为字符串

# 使用str内置类型将其他类型数据转换成为字符串
a = 34
b = str(a)
print(b)
print(type(a))
print(type(b))

# 08- 转换成为布尔值
# 使用bool内置类可以将其他数据类型转换成为布尔值
print(bool(100)) # 将数字100转换成为100 True
print(bool(-1)) # 将-1转换成为布尔值也是 True
print(bool(0)) # False

# 数字里，只有数字0被转换成为布尔值False，其他数字转换成为True
print(bool('hello')) # True
print(bool('False')) # Ture
print(bool(''))   # False
print(bool(""))  # False

# 字符串里，只有空字符串'' / "" 可以转换成为False，其他字符串都转换成为True
# None 转换成为布尔值是False
print(bool(None)) # False
print(bool('None')) # True

print(bool([])) #False
print(bool(()))  # False
print(bool({}))  # False

#集合
#('name':'zhuangsan','age':18)
#{1,2,3,4}
#{} #空字典
s = set()
print(bool(s))

#  数字0，空字符串，''/"",空列表[],空元祖(),空字典{}，空集合set(),空数据None会被转换成False

# 在计算机里，Ture和False 其实就是使用数字1或数字0来保存
print(True+1) # 2
print(False + 1) #1

# 隐式类型转换
if 3 > 2:
    print('hello')

if 3:
    print('good')

if 3:
    print('good')

#09-算数运算符
# Python 里支持很多运算符
# + 加 - 减  *乘 /除  ** 幂运算 // 整除 % 取余
print(1 + 1)  # 2
print(4 - 2)  # 2
print(3 * 2)  # 6

# 在python3里，两个整数相除，得到的结果会是一个浮点数
# python3例： 10 / 3 = 3.33333333
# 在python2里，两个整数相除，得到得到的结果是整数
# python2例： 10/3 = 3
print(6 / 2)  # 3.0
print(9 / 2) # 4.5
print(3 ** 3) # 27
print(81 ** 1 / 2) # 40.5
#开平方根
print(81 ** (1 / 2)) #9.0

print(10/3) #3.33333
print(10 // 3) # 整除，只取整数部分

print(10%3) # 1 取余，只取余数部分
print(1928 % 9876) # 1928

# 字符串里有限度的支持加法和惩罚运算符
# 加法运算符：只能用于两个字符串类型的数据，用来拼接两个字符串
print('hello' + 'world')  # 将多个字符串拼接为一个字符串
# 在Python里，数字和字符串之间，不能做加法运算
# print('18' + 1) # 在python里，数字和字符串之间，不能做加法运算。
# 乘法运算符：可以用于数字和字符之间，用来讲一个字符串重复多次
print('hello'* 2) # hellohello
# print('hello'-'yes') 不支持
# print('hello' * 'god') 不支持

# = 等号在计算机编程里，我们称之为赋值运算符，和数学里的等号有一定的区别

# 数学
# 1 + 1 = 2
# 4 = 4

# 在计算机编程里，等号(赋值运算符)作用是将等号右边的值赋值给等号的左边
# 等号的左边一定不能是常量或者表达式
a = 4  # 可以

# 10 = x  不行
# 3 + 3 = m  不行
m = 3 + 3 #可以
x = 1
#x = x + 2
x += 2
print(x) #3
x -= 2
print(x) # 2
x *= 3
print(x) # 6

x /= 2
print(x) # 3.0

x **= 5
print(x) # 243.0

x //= 2
print(x) #121.0
x %= 2 # x = x % 2
print(x)

# 赋值运算符的特殊场景
# 等号连接的变量可以传递赋值
a = b = c = d = 10
print(a,b,c,d)

# x = 'yes' = y = z # 不可以 yes是常量 而且从右往左运算

m,n = 3,5  # 拆包
print(m,n)

x = 'hello','good','yes' # 元祖()括号可以省略
print(x) # ('hello','good'，'yes')

# y,z = 1,2,3,4,5  会报错
# print(y,z)

# 拆包时，变量的个数和值得个数不一致，会报错
# o,p,q = 4,2 会报错
# print(o,p,q)

o,*p,q = 1,2,3,4,5,6
print(o,p,q) # 1 [2, 3, 4, 5] 6

*o,p,q = 1,2,3,4,5,6
print(o,p,q) # [1, 2, 3, 4] 5 6

o,p,*q = 1,2,3,4,5,6
print(o,p,q) # 1,2,[3,4,5,6]

# 比较运算符
# 大于 > 小于 < 大于等于 >= 小于等于 <= 不等于 ！=  等等与 ==
print(2 > 1)  # True

# 比较运算符在字符串里的使用
# 字符串之间使用比较运算符，会根据各个字符的编码值逐一进行比较
# ASCII码表
print('a' > 'b')  # False 97 > 98
print('abc' > 'b')  #False 97 > 98 abc不是字母相加还是以a为基准和b比较

# 数字和字符串之间，做 == 运算的结果是False，做！=结果是True，其他的比较运算会报错
# print('a' > 90)
print('a' == 90)  # False
print('a'!= 90)

# 逻辑运算符  逻辑与and   逻辑或or 逻辑非not
# 逻辑与规则：只要有一个运算数是False，结果就是False；只有所有的运算数都是True，结果才是True

print(2 > 1 and 5 > 3 and 10 > 2)  # Ture
print(3 > 2 and 5 < 4 and 6 > 1)  # False

# 逻辑或规则：只要由一个运算数时True，结果就是True；只有所有的于是暖树都是False，结果才是False
print(3 > 9 or 4 < 7 or 10 > 3)  # True
print(3 > 5 or 4 < 2 or 8 < 7)   # False

# 逻辑非运算：True ===> False False===>True
print(not (5 > 2))  # 答案是True 但是not取反所以是False

#  逻辑运算符的短路
# 逻辑与运算，只由所有的运算书都是True，结果才为True
# 只要由一个运算书是False，结果就是False
4 > 3 and print('hello world')
4 < 3 and print('你好世界')  # 逻辑运算短路
4 > 3 or print('hahaha')
4 < 3 or print('heihei')


# 逻辑运算的结果，一定是布尔值吗？ 不一定
# 逻辑与运算做取值时，取第一个为False的值；如果所有的运算书都是True，取最后一个值
print(3 and 5 and 0 and 'hello')  # 答案是0 因为3，5转化成布尔值都是True 0转换成布尔值是False所以到这里后面的不再执行。
print('good' and 'yes' and 'ok' and 100) # 100

# 逻辑或运算做取值时，取第一个为True的值；如果所有的运算数都是False，取最后一个。
print(0 or [] or 'lisi' or 5 or 'ok')  # lisi 取True的那个
print(0 or [] or {} or ())  # () 都没有正确取最后一个False

# 按位与& 按位或  按位左移<<  按位右移>>  按位取反 ~
a = 23   # bin(23) 0b10111 二进制就是 0001 0111 前面自动补全0
b = 15   # bin(15) 0b1111  二进制就是 0000 1111 前面自动补全0
print(a & b)  # 0001 0111  安位与：同为1则为1，否则为0
              # 0000 1111  答案： 上下对照 0000 0111 答案是7


a = 23       #  按位或：只要有一个为1，就为1
b = 15       #  答案：0001 1111    结果 31
print(a | b)
print(a ^ b)  #  按位异或相同为0，不同为1  0001 1000 24

x = 5         # 算法 5*3的2次方 结果是40
print(x << 3)

y = 15
print(y >> 2) # a >> n ==> a 除以2的2次方  15除以2的内次方 3

