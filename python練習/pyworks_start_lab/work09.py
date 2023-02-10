import datetime
a = input("何時　または　時刻:")
if a == ("何時"):
    print((datetime.date.today()))
elif a == ("時刻"):
    print((datetime.date.today()))
else:
    print("再度正しい入力お願いします")