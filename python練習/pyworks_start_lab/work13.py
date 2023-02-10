"""
1.while文を使って、1から30までの数字を表示し、数字が 3の倍数なら数字の横に Fizz、
5の倍数なら Buzz、 3 と 5 のいずれの倍数でもあるなら FizzBuzz と表示してください。

"""
for num1 in range(1,31):
 while num1%3 == 0 and num1%5 == 0:
    print("FizzBuzz")
 if num1%3 == 0:
    print("Fizz")
 elif num1%5 == 0:
    print("Buzz")
 else:
     print(num1)