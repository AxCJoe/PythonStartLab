num = eval(input('请输入一个四位整数：'))
sd = num%10 # 个位数
tens = num//10%10 #十位数
hundred = num//100%10 #百位数
thousand = num//1000%100 #千位数

print('个位数的数字：',sd)
print('十位上的数字：',tens)
print('百位上的数字：',hundred)
print('千位上的数字：',thousand)
