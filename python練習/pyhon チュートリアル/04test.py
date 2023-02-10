number = eval(input('请输入您的6位中奖号码：'))
if number == 987654:
    print('恭喜你中奖了')
else:
    print('不好意思，您没有中奖')

#eval 不能0开头否则报错

n = 98   #赋值
if n%2: #98%2的余数为0,0的布尔值为False, 非0的布尔值为True
    print(n,'为奇数')

if not n%2: #98%2的余数为0 0的布尔值为False,not False结果为True
    print(n,'为偶数')

print('------判断一个字符串是否是空字符串---------')
x = input('请输入一个内容：') #空字符串的布尔值为False,非空字符串的布尔值为True
if x:
    print('x是一个非空的字符串')
if not x:
    print('x是一个空字符串')

print('-------表达式也可以是一个单纯的变量---------')
flag =  eval(input('请输入一个布尔类型--True或False：'))
print(flag,type(flag))
if flag:
    print('flage的值是True')
if not flag:
    print('flag的值是False')

print('------使用if语句时,如果语块只有一句代码,可以将语句块直接写在冒号的后面')
a = 10
b = 5
if a>b:max=a # :max = a 写完后下面的print不用缩进
print('a和b的最大值为：',max)

print('-----以上代码还可以使用条件表达式简化-----')
number2 = eval(input('请输入您的4位中奖号码：'))
print('恭喜你中奖了'if number2 == 4321 else'您没中奖')
