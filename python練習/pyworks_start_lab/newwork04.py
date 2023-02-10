# import random

# l = [0, 1, 2, 3, 4]

# print(random.choice(l))
# # 0

# >>>range(10)        # 从 0 开始到 10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> range(1, 11)     # 从 1 开始到 11
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> range(0, 30, 5)  # 步长为 5
# [0, 5, 10, 15, 20, 25]
# >>> range(0, 10, 3)  # 步长为 3
# [0, 3, 6, 9]
# >>> range(0, -10, -1) # 负数
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
# >>> range(0)
# []
# >>> range(1, 0)
# []

# import random
# data =['大吉','中吉','吉','小吉','凶']
# data_choice = random.choice(data)
# print(data_choice)　決められた

#import random
#def bingo(a,b):
import random
a = list(range(1,6))
b = random.choice(a)
    #print(b)
for x in a: 
    if x == b:
          
        print("続きの番号Enterを押してください",b)
    else:
        continue
while True:
  input()
  print(b)
    
             

# #for b in a:
#     if len(b) != 0:
# #if b in a:
#         print("続きの番号Enterを押してください",b)
#     else:
#          return bingo(b)
# while True:
#     input()
#     c = random.sample
#     fortune = bingo(c)
#     print(fortune)


#for b in a:
# while len(b) != 0:
#     print("続きの番号Enterを押してください",b)
#     continue
#     input(enter)
#     #break
# print(a)

#print(b)


# print(l)
# # print(range)

