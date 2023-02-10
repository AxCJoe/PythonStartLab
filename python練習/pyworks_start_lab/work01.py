num1 = input("1番目の数字を入力: ")
num2 = input("四則演算の記号（+ - * /）のいづれか入力: ")
num3 = input("2番目の数字を入力: ")
num4 = int(num1) + int(num3)
num5 = int(num1) - int(num3)
num6 = int(num1) * int(num3)
num7 = int(num1) / int(num3)
if num2 == ("+"):
 print(num4)
elif num2 == ("-"):
 print(num5)
elif num2 == ("*"):
 print(num6)
elif num2 == ("/"):
 print(num7)
else
 print()        
   