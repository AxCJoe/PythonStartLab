
#Pythonチュートリアル

'''
プライマリプロンプト(?)(>>>)
文字列リテラル(?)
ハッシュ記号(?)
#コメント
17//3 = 5 切り下げ除算(じょさん)はを返す
17 % 3　=　2　%演算子は剰余(?)(除算の余り())を返す
**演算子　累乗(るいじょう)
等号(とうごう=)
アンダースコア(?)
リードオンリー(?)
ビルトン変数(?)
バックスラッシュ(\)
クォート文字(?)
エスケープ(?)
シングルクオート('')
ダブルクォート("")
改行(?)
文字列リテラル(?)
インデックス指定(?)
スライシング(?)
変更不能体(immutale)(?)
ビルトイン関数(?)
ライブラリ　リファレンス　(?)
シーケンス(sequence)(IT:連続、一続き、順序、順番、並び、配列)
テキストシーケンス型(?)
シーケンス型(?)
文字列メソッド(?)
メソッド(?)
文字列のフォーマッティング(?)
フォーマッティング(?)
角カッコ(?)
カンマ(?)
カンマ区切りの値(?)
シーケンス型(?)
末尾(まつび)
置換(ちかん)
フィボナッチ級数(?)
引数(?)
抑制(?)
馴染み(なじみ)
インデント(?)
等差級数(?)
制御構文(せいぎょこうぶん)(while if for)
反複可能体(iterable)(?)
約数(やくすう)
素数(そすう)
ビジーウェイト(?)
割込(?)
シンボル表(?)
リネーム(?)
必須(ひっす)
セマンティクス(意味論)(?)
簡潔(かんけつ)
挿入(そうにゅう)
メソッドシグネチャ(定義表記)(?) 
ライブラリリファレンス(?) 
ソート(?)
'''

'''
Python 3.10.1 (main, Dec 11 2021, 17:22:55) [GCC 11.1.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> tax = 12.5 /100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_,2)
113.06
>>> 
#price + _　#対話モードでアンダースコアに代入している
#print(round(price + _ ,2))

终端中要注意的事项，\' 直接屏蔽\ 输出' \t \n直接输出
print下 \t \n 正常做转意字符串
>>> 'dose\'t'　
"dose't"
>>> "dose't"
"dose't"
>>> '"Yes,"he said'
'"Yes,"he said'
>>> "\Yes,\"he said"
'\\Yes,"he said'
>>> "\"Yes,\"he said."
'"Yes,"he said.'

print('C:\some\name') #
C:\some
ame

#raw文字列
print(r'C:\some\name') #引用符の前のrに注目
C:\some\name

'''

'''
print("""
    Usage:Thingy[OPTIONS]
        -h                  Display this usage message
        -H hostname         Hostname to connect to
    """)

    Usage:Thingy[OPTIONS]
        -h                  Display this usage message
        -H hostname         Hostname to connect to

print("""\
    Usage:Thingy[OPTIONS]
        -h                  Display this usage message
        -H hostname         Hostname to connect to
    """)
    Usage:Thingy[OPTIONS]
        -h                  Display this usage message
        -H hostname         Hostname to connect to
\(最小の改行が含まれていないことに注目:)
\(首尾加入\ 起到不换行作用 如果加入 输出结果都会先换一行在输出)

'''

'''
print(3*'un'+'ium')
unununium
print('Py''thon')
Python

'''
'''
prefix = 'py'
prefix 'thon' #変数と文字列リテラルは連携できない
SyntaxError:invalid SyntaxError
(構文エラー:無効な構文)

('un'*3)'ium'
SyntaxError:invalid SyntaxError
(構文エラー:無効な構文)

#正确执行
prefix = 'Py'
print(prefix+'thon')
Python
print('un'*3+'ium')
unununium

'''

'''
word = 'Python'
print(word[0]) #位置のキャラクタ
P
print(word[5]) #位置のキャラクタ
n
print(word[:2] + word[2:])
'Python'
print(word[:4]+word[4:])
'Python'
word[:2] #最初の文字から位置2(2を含まない)まで文字
'Py'  #|p|y|t|h|o|n|
word[4:] #位置4(4を含む)から最後までの文字
'on'  #|p|y|t|h|o|n|
word[-2:] #位置ー2(含む)から最後までの文字
'on'  #|p|y|t|h|o|n|

#非負のインデックスにおいては、
スライシングの長さは2つのインデックスの差だ
例えばword[1:3]の長さは2である。

大きすぎるインデックスを指定するとエラーになる:
word[42] #wordは6文字
IndexError:String　index out of range
(インデックスエラー:文字列インデックスが範囲外(はんいがい))

#避开Error
print(word[4:42])
'on'
print(word[42:])
''
'''

'''
文字列のインデックス位置に代入を行うとエラーが出る:
例えば
word[0] = 'j'
TypeErro:'str'boject does not supprt item assignment
(型エラー:'str'オブジェクトはアイテム代入をサポートしていない)

word[2:]='Py'
TypeErro:'str'boject does not supprt item assignment
(型エラー:'str'オブジェクトはアイテム代入をサポートしていない)

異なる文字列が必要な時は新しい文字列を生成する必要がある:
word = 'Python'
'J' + word[1:] #输出修改1位然后输出----最后一位的内容
Jython
'J' + word[:] #输出添加至0位然后输出----最后一位的内容
JPython
'J' + word[1] #输出修改1位然后输出到第二位的内容
Jy
word[:2] + 'Py' #输出到第二位，然后在第二位添加'py'
'Pypy'

'''
'''
len()関数，文字列の長さを返す:
s='Python'
len(s)
6

'''

'''
リスト
abc = [1,2,3,4,5]
print(abc)
[1,2,3,4,5]
print(abc[0])
1
print(abc[-1])
5
print(abc[-3:])
[3,4,5]
print(abc[:])
[1,2,3,4,5]

#リストは連携なども操作もサポートしている
abc = [1,2,3,4,5]
print(abc + [10,20,30,40])
[1, 2, 3, 4, 5, 10, 20, 30, 40]

#文字列は変更不能体(immutable)であったが、
 リストは変更可能体(mutable)である。
 すなわち内容を入れ替える亊ができる:
abc = [1,2,3,3,5] #多一个3 进行修改
abc[3] = 4
print(abc)
[1, 2, 3, 4, 5]

#append() メソッド使用、リスト末尾にアイテム追加する亊ができる
abc.append(6)
print(abc)
[1, 2, 3, 4, 5, 6]
abc.append(1+6)
print(abc)
[1, 2, 3, 4, 5, 6, 7]

#リスト内容をクリア
word = ['a','b','c','d']
print(word)
['a', 'b', 'c', 'd']

#いくつの値を置換(ちかん)
word[2:4] = ['G','H']
print(word)
['a', 'G', 'H', 'd']

#これらを削除
word[2:4] = []
['a','d']

#リストをクリア(Clear)。空リストで全部の要素を置換する。
word[:] = []
print(word)
[]

#len()関数はリストも使える:
word = ['a','d']
print(len(word))
2

#リストは入れ子にできる(二维，或多维数组)
a = ['ab','ac','ad']
b = [1,2,3]
x = [a,b]
print(x)
[['ab', 'ac', 'ad'], [1, 2, 3]]
print(x[0:1])
[['ab', 'ac', 'ad']]
print(x[0][1])
ac
print(x[0][0])
ab
'''

'''
#フィボナッチ級数
#2項の和により次項が定まる
a,b = 0,1
while b<10:
    print(b)
    a,b = b,a + b
1
1
2
3
5
8

#キーワード引数endを使えば、出力未尾の改行の抑制(?)や、
　出力未尾を他の文字列に変更する亊ができる:
a,b = 0,1
while b<1000:
    print(b,end=',')
    a,b = b,a + b
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,%(?)

'''

'''
制御構文(せいぎょこうぶん)

#elifはelse ifの短縮
if...elif...else...

#for
word = ['cat','dog','geed']
for i in word:
    print(i,len(i))
cat 3
dog 3
geed 4

#在数组中查找大于6的字符串，并添加到word数组中起始位[0]。
word = ['cat','dog','geed','defenceall']
#把所有 word数组内容复制给s 
for s in word[:]:  #リスト全体のスライスコピーにループをかける
    #s里的字符串长度开始比对，长度哪些大于6
    if len(s) > 6:
        #长度大于6的字符串将添加到word数组的起始位[0]
        word.insert(0,s)        
#输出word数组里的内容包括刚才在起始为插入的内容
# s的值是len(s)最后对比出来的值        
print(word,s)

['defenceall', 'cat', 'dog', 'geed', 'defenceall']

#如果word数组里有2个6位字符串，那么它将在word的起始数组中，按数组顺序一次添加到word数组中
#len(s)里的 s 在上面的代码里最后停留在‘defenceall’，但在这段代码中 s 最后停留在 We_All_kill_them

word = ['cat','dog','geed','defenceall','We_All_kill_them']
#把所有 word数组内容复制给s 
for s in word[:]:  #リスト全体のスライスコピーにループをかける
    #s里的字符串长度开始比对，长度哪些大于6
    if len(s) > 6:
        #长度大于6的字符串将添加到word数组的起始位[0]
        word.insert(0,s)        
#输出word数组里的内容包括刚才在起始为插入的内容
# s的值是len(s)最后对比出来的值        
print(word,s)
['We_All_kill_them', 'defenceall', 'cat', 'dog', 'geed', 'defenceall', 'We_All_kill_them'] We_All_kill_them



'''


'''
range()関数
for i in range(5):
    print(i,end=',')
0
1
2
3
4  

range(5,10)
-> 5から9まで

range(0,10,3)
-> 0,3,6,9

range(-10,-100,-30)
-> -10,-40,-70

print(range(10))
-> range(0,10)

print(range(5,9))
range(5,9)

abc = ['Mary','Had','a','little','lamb']
for i in range(len(abc)): 
    #len(abc) 是吧abc数组里的字符的位置给标记住了
    print(i,abc[i])

0 Mary
1 Had
2 a
3 little
4 lamb

*range()関数は返すオブジェクトはlist(リスト)ではない為、本当のリストを作らず、それにより空間を節約できる。
　我々はそのようなオブジェクトを反複可能体(iterable)と呼ぶ。
　反複可能体を期待する関数や構造の方、反複子(iterator)と言う。
　for文は反複子の例である。反複可能体からリストを生成するlist()関数も反複子である。

list(range(5))
[0,1,2,3,4]　
　
'''

'''
#break文とcontinue文、ループにおけるelse節
 break文はあC同様、forとwhileのループを抜けるものだ。
 forとwhileはelse節を加えられる。
 else節は、リストを使いはたしたり(for)
 条件式がfalseになるとwhileループが終了する。
 break文で終了した場合には実効されない。

#素数探索ループ

#这里会生成2-9的数字一次带进n里
for n in range(2,10):
    # 一个一个试错，比如（2,5）的情况下会先带2,然后3,然后4，进行算数
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        #ループで約数をみつけられなかった場合
        print(n,'is a prime number')

2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3

else節の所属はif文ではく、forループ
ループでのelse節は、if文のそれよりもtry文でのそれに似たものである。

#continue文はループの残りを飛ばして次回の反復にいく
for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number",num)
        #continue是跳过下面还可执行的内容直接回到第一句反复执行直到条件不成立
        continue
    print("Found a number",num)

Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9

#pass文は何もしない。構文的に文が必要なのに、プログラム的には何もする必要がない時に使う

>>> while True:
    pass:ビジーウェイトでキーボード割込(Ctrl+C)をもつ

これは最小のクラスを生成するのにもよく使われる:

>>> class MyEmptyClass:
    pass 

>>> def initlog(*args):
    pass #実装を忘れないこと!

*passの他の使い方、新しくコードを書いている時関数や条件の本体に
プレースホルダとして置いておき、もっと抽象的なレベルにつて考えつづける
亊を助ける、と言うのがある。passは黙って無視されるのだ:

'''

'''
#関数の定義
・・フィボナッチ級数を任意の上限まで書き出す関数・・
def fib(n):
    #n までのフィボナッチ級数を表示する
    a,b = 0,1
    while a < n:
        print(a,end=',')
        a,b = b,a+b
    print()
#ではこの関数を呼び出します。 
fib(2000)
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,

#関数自身也可以进行赋值
f = fib
f(100)
0,1,1,2,3,5,8,13,21,34,55,89

#如果想显示 None
fib(0)
print(fib(0))
None

#関数の結果をリストで返す
def fib2(n):
    #n までのフィボナッチ級数をリストで返す
    result = []
    a,b = 0,1
    while a < n:
        #append() メソッドは result = result+[a]と等価だが、より効率的である。
        result.append(a) #下記参照
        a,b = b,a + b
    return result

f91 = fib2(100)  #　コール
print(f91)  #結果を書き出す

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


'''
'''
#更に関数定義について
引数の個数が可変の関数を定義することもできる。
これは3つの形態があり、組み合わせることも可能だ。

#引数のデフォルト値
個数の引数でコールできる

#
#下面的代码是案例，执行结果看注释
# 这里是関数的定义组合方式，比如直接用（变量=prompt，加入数值retries=4，赋值一句话complaint = 'Yes or no,please!'）
# 在举例 def ask('Hello')  必須(ひっす)の引数だけを与える
# def ask('Hello',2) 　オプション引数を1つ与える
# def('CPU',2,'GPU')　すべての引数を与える
#retries=4 在input里是修改不了这个数值的 retries=4这里把4给成0或负数就可以得到 '非協力的ユーザ'
def ask_ok(prompt,retries=4,complaint = 'Yes or no,please!'):
    while True:
        ok=input(prompt)
        if ok in ('y','ye','yes'):
            return True # 输入y,ye,yes都偶会返还True
        if ok in ('n','no','nop','nope'):
            return False # 输入n,no,nop,nope都会返还Flase
        retries = retries - 1
        if retries < 0: # 输入数字若小于0输出('非協力的ユーザ')
            raise OSError('非協力的ユーザ')
        print(complaint) # 输入字符时若不是上面的提示的字符时，输出comlaint的内容'Yes or no,please!'

print(ask_ok(input)) #print输出用input进行代码检验里面的内容看是否给出输入内容

#デフォルト値の評価は、関数を定義した時点で、定義をかいたスコープで行われる。
i = 5

def f(arg=i):
    print(arg)

i = 6
f()

5


#重要な警告:デフォルト値の評価は一度しか起きない。デフォルト値が可変オブジェクト
　すなわちリスト、ディクショナリ、およびほとんどのクラスのインスタンスである場合影響する

def f(a,L=[]): # 想加入字符串不能在这里设置['']要在结尾设置
    L.append(a)
    return L
print(f(1)) # 这里加入的数字
print(f(2))
print(f(3))
print(f('a')) # 想要加入字符串要在这里把字符串给加进来
print(f('b'))
print(f('c'))

[1, 2]
[1, 2, 3]
[1, 2, 3, 'a']
[1, 2, 3, 'a', 'b']
[1, 2, 3, 'a', 'b', 'c']

# コール間でデフォルト値を共有されたくないなら、こと関数は次のように書く

def f(a,L = None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1)) # 虽然不想共享但是一样可以输出数值
print(f('abc')) 

[1]
['abc']



'''

'''
#キーワード引数
#[キーワード　=　値]の形っである

#如果voltage = 100 提提前设定好那么输出时 parrot()是可以的反之什么都设置需要在输出的内容里添加数字parrot(1000)等
 即便添加了数字还可以在输出内容里进行修改比如print(parrot(5.2))voltage会被改成5.2

def parrot(voltage,state = 'a stiff',action = 'voom',type = 'Norwegian Blie' ):
    print("--This parrot would",action,end = '') # action = 'voom'
    # キーワード引数1个
    print("if you put",voltage,'volts through i t.' ) # print(parrot(1000))要添加的数字 
    # キーワード引数2个
    print("--lovely plumage,the",type) # type = 'Norwegian Blie' )
    # キーワード引数3个
    print("--Tt's",state,'!') # state = 'a stiff'

print(parrot(1000)) #位置引数1个

--This parrot would voomif you put 1000 volts through it.
--lovely plumage,the Norwegian Blie
--Tt's a stiff !
None

# 位置实参 举例：parrot('abc',1000)
# 关键字实参 举例：parrot(voltage = 'abc',state = 'bcd')
# 默认值 举例：parrot(voltage='willie')


# 错误输出
parrot() #必要な引数がない　里面没有数值或字符串 
parrot(voltage=5.0,'dead')　# キーワード引数の後に非キーワード引数
parrot(110,voltage=220) # 同じ引数に値を2度与えた
parrot(actor='John Cleese') # 未知のキーワード引数

#　引数は一度しか取れない
def function(a):
    pass
function(0,a=1) #引数を二度目取ったのでエラー

function(0,a=1)
TypeError: function() got multiple values for argument 'a'
(型エラー:function()のキーワード引数[a]が複数の値を取ってる)

#传参* 和 **的区别

def cheeseshop(kind,*arguments,**keywords):
    print("--Do you like watching me",kind,"?")
    print("--Fuck you",kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw,":",keywords[kw])
print(cheeseshop("Li Lei",# 注意写法：传入的是字典
"VAN Drack HOME",
"Boy Next Door",
"VAN = MC",
1024, # 注意写法：传入的是字典
Set = "None",# 注意写法：传入的是列表
case = "IG",
gift ='GG')) 

>>>　--Do you like watching me Li Lei ?
>>>　--Fuck you Li Lei
>>>　VAN Drack HOME
>>>　Boy Next Door
>>>　VAN = MC
>>>　Joe = FUCk
>>>　----------------------------------------
>>>　Set : None
>>>　case : IG
>>>　gift : GG

#　任意引数のリスト

def write_mukltiple(file,separator,*arg):
    file.write(separator.join(arg))
print(write_mukltiple("abc","----","uuu7","9999",1024))　???

def concat(*args,sep = '/'):
    return sep.join(args) # 注意 / 插入到args数据的后面啊 

print(concat("abcd","Hello","Tomei","GG"))

>>>　abcd/Hello/Tomei/GG
--------------------------------

def concat(*args,sep = '/'):
    return sep.join(args) # 注意 . 插入到args数据的后面啊 
    
print(concat("abcd","Hello","Tomei","GG",sep = '.'))

>>>　abcd.Hello.Tomei.GG


'''

'''
#　引数リストのアンバック

print(list(range(4,9)))　#　個別の引数を使った普通のコール

>>>　[4, 5, 6, 7, 8]

args = [3,8]
print(list(range(*args)))　#　リストからアンパックした引数でコール

>>>　[3, 4, 5, 6, 7]

*　同じように　**演算子を使えば、[ディクショナリ]をキーワード引数にして渡す亊ができる

def parrot(voltage,state = 'a stiff',action = 'voom'):
    print("--This parrot would",action,end = ' ') 
    print("if you put",voltage,'volts through i t.',end = ' ') 
    print("E's",state,'!') 

d = {"voltage":"four million",   
"state":"bleedin' demised",
"action":"Joe"}   #　学问在这里 （这个符号是{} 字典型）

print(parrot(**d))

>>> --This parrot would Joe if you put four million volts through i t. E's bleedin' demised !

'''

'''
#　lambda(ラムダ)式
# lambdaを使うと小さい無名関数がかける。[lambda a,b: a+b]は、2つの引数の和
　を返す関数である。ラムダ関数は関数オブジェクトが必要な場所すべてに使用できる。
　ただしこの形式には、単一の式しか持ってないと言う構文上の制限がある。

def make_incrementor(n):
    return lambda x: x+n
f = make_incrementor(42)
print(f(0))
print(f(2))

>>> 42
>>> 44

#上記はラムダ式を使って関数を返す例だ。他の用途としは、小さな関数を引数として渡すときにも使える

pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(key=lambda pair: pair[1])

# 相当与跟旁边的数值换位置
print(pairs) # 反复执行都是一个结果 [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

>>> [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

'''

'''
#ドキュメンテーション文字列(docstring)
とにかく簡潔(かんけつ)に要約することべきである。

def my_function():
    """Do nothing,but document it.

    No,really,it doesn't do anything    
    """
    pass

print(my_function.__doc__) # 注意后面要跟__doc__ 否则显示出错

Do nothing,but document it.

    No,really,it doesn't do anything 

'''

'''
#　関数注釈(関数アノテーション)
这块有点问回头在看
def f(ham:str,eggs: str = 'eggs') -> str:

'''

'''
# 5章データ
# リストにつての補足
リストのデータ型にはもう少しメソッドがある。以下はリストオブジェクトの全メソッドである。

list.append(x)
　リストの末尾に、アイテムを1つ追加する。a[len(a):] = [x]と等価

list.extend(L)
  リストの末尾(まつび)に、与えられたリストLの全アイテムを追加する亊で、リストを伸長する。a[len(a):] = L

list.insert(i,x)
   指定された位置にアイテムを挿入(そうにゅう)第一引数は要素のインデックスである。
　　つまり挿入はこの要素の前に行われる。a.insert(0,x)とするとリストの先頭に挿入される
　　a.insert(len(a),x)は、a.append(x)と等価である

list.remove(x)
 　値がxである最初のアイテムを削除する。
 　*そのそうなアイテムが存在しないとえらーになる

list.pop([i])
  指定された位置のアイテムをリストから削除し、このアイテムを返す。
  インデックスが指定されいないと、a.pop()はリストの最後のアイテムを返し、リストから削除する。

list.clear()
  リストからすべえてのアイテムを削除する。del a[:]と等価

list.index(x)
  値がxである最初のアイテムのインデックスを返す。
  *そのようなアイテムが存在しなければエラーになる

list.count(x)
  リスト中のxの個数を返す

list.sort(key=None,reverse=False)
   リストをインプレースで(=コピーを取らず、そのリストオブジェクトを直接)
   ソースする。引数でソートのカスタマイズができる。sorted()の項の参照のこと。

list.reverse()
   リストの要素をインプレースで逆順にする

list.copy()

    リストのシャローコピー(浅いコピー)を返す。a[:]と等価。

a = [66.25,333,333,1,1234.5]
print(a.count(333),a.count(66.25),a.count('x')) #查找在数组中有几个
>>> 2 1 0

a.insert(2,-1)
print(a)
>>> [66.25, 333, -1, 333, 1, 1234.5]

a.append(333)
print(a)
>>> [66.25, 333, -1, 333, 1, 1234.5, 333]

a.index(333)
print(a)
>>> [66.25, 333, -1, 333, 1, 1234.5, 333]

a.remove(333)
print(a)
>>> [66.25, -1, 333, 1, 1234.5, 333]

a.reverse()
print(a)
>>> [333, 1234.5, 1, 333, -1, 66.25]

a.sort()
print(a)
>>> [-1, 1, 66.25, 333, 333, 1234.5]

a.pop()
print(a)
>>> [-1, 1, 66.25, 333, 333]


'''
