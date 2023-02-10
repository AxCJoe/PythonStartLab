"""
2.数値を要素とするリストを受け取り平均値を計算する
関数 calc_ave を作ってください。それを使って、
次に与えるリストの平均値を計算してください。
リスト：[40, 61, 52, 38, 45]

"""
def calc_ave():
    numlist = [40, 61, 52, 38, 45]
    ave = sum(numlist) / len(numlist)
    print(ave) 
print(calc_ave())

