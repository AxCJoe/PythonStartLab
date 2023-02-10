"""
1.for文を使って次に与えるリスト内データの和と平均値を計算してください。
 [40, 61, 52, 38, 45]
2.for文を使わずに組み込み関数 sum() と len() を使って平均値を計算してください。
3.1から50までの数字を表示してください。ただし、数字が 3の倍数なら Fizz、5の倍数なら Buzz、 
3 と 5 のいずれの倍数でもあるなら FizzBuzz と表示してください。
"""
#break

#else

"""
def student(name,age,tall):
    dic = {
        "名前":name,
        "年齢":age,
        "身長":tall,

    }
    return dic

print(student("山田","25","168"))
print(student("168","山田","25"))
print(student(tall="168",name="山田",age="25"))"""


"""
def show_kwargs(**show_kwargs): #キーワード引数の辞書の例 タプル化とは
    print("keyword args:",kwargs)
    return kwargs
print(show_kwargs(a="パスタ"),b="赤ワイン",c="肉料理")"""


"""
animal = 'cat'
print("animal   in global:",animal)
def my_func():
    animal = 'dog'
    print("animal   in my_func:",animal)
my_func
print("animal global after my_func:",animal)"""

"""
animal = 'cat'
print("animal   in global:",animal)
def my_func():
    global animal
    animal = 'dog'
    print("animal   in my_func:",animal)
my_func
print("animal global after my_func:",animal)"""

"""
def modify_list(x):#受け取ったリストに要素追加
    x.append(1)
my_list = [0,1,2,3]
print("before:",my_list)
modify_list(my_list)
print("after:",my_list)"""

"""
def gen_list(n):  #受け取った要素数のリストを生成
    my_list = [1]
    return my_list * n
print(gen_list(5))"""

"""
def print_upto(num):    #あたえら数未満の数を表示
    num_str = ""
    for i in range(num):
        num_str += " " + str(i)
    print(num_str)
if _name_ = "_main_":
    print(10)


    import my_module    #モジュールを読み込む
    if_name_ == "_main_":
        my_module.print_upto(10)

    import my_module as mo     　# モジュール名に別名をつける　モジュール名を短くできる
        if_name_ == "_main_":
        my_module.print_upto(10)

    from import 