# Pythonチュートリアル

# “pycharm使用快捷键自动对齐代码(Ctrl + Alt + L)”
'''
[] 这是列表 list
プライマリプロンプト(primary prompt)(>>>)
プロンプト (prompt)(プロンプトとは、利用者がコンピュータに文字で命令を打ち込んで操作するコマンドラインインターフェース（CLI：Command Line Interface）において、システムが入力を受け付けられる状態であることを示す短い文字や記号の並び。)
文字列リテラル(literal)(特定のデータ型の値を直に記載したもの)
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
ビルトイン関数(内置函数)(built-in)
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
除去（じょきょ）
格納(かくのう)(パソコン上の言葉ではファイルを収納するではなく、格納するといいますがファイル自体の役割を見てのものと言えるでしょう。)
スクリプト(脚本)
インタープリター(解释器)
テキストエディタ(文本编辑器)
ディレクトリ(目录)
標準ライブラリ(标准系统自带的)
コンパイル (编译)(compile)
プラットフォーム (platform）(動作環境)（开发环境、运行环境，包括硬件、操作系统、开发语言、编译调式、运行时库等各种所需。）
アーキテクチャ (architecture)(基本設計や共通仕様、設計思想などを指すことが多い)(体系结构,架构)
キャッシュ(cache)(缓存)
ライブラリリファレンス(库参考手册)
モジュールセット(模块组)
システムコール(系统调用)(system call)
インタプリタ (interpreter)(翻译解释)(インタプリタとは、人間に分かりやすい高水準プログラミング言語（高級言語）で書かれたコンピュータプログラムを、コンピュータが解釈・実行できる形式に変換しながら同時に少しずつ実行していくソフトウェア。英語の原義は「通訳者」。)
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
>>> 2 1 0  # 333有两个 ， 66.25 有1个   x 一个都没有
>>> 2 1 0  # 333有两个 ， 66.25 有1个   x 一个都没有

a.insert(2,-1) 
print(a)
>>> [66.25, 333, -1, 333, 1, 1234.5]  # 在数组的第二个位置插入 -1

a.append(333)
print(a)
>>> [66.25, 333, -1, 333, 1, 1234.5, 333] #在数组的末尾添加 333

a = [66.25,333,333,1,1234.5,333] # [] 这是列表 list
print(a.index(1)) # 数字 1 在列表的中索引位置
>>> 3
print(a.index(333)) # 333 在列表中有几处但这里默认指向第一个333 结果也就是1
>>> 1

a.remove(333)
print(a)
>>> [66.25, -1, 333, 1, 1234.5, 333] # 删掉从0开始的第一位的 333

a.reverse()
print(a)
>>> [333, 1234.5, 1, 333, -1, 66.25] # 数据反向实现

a.sort()
print(a)
>>> [-1, 1, 66.25, 333, 333, 1234.5] # 列表里的数据按大小排列

a.pop()
print(a)
>>> [-1, 1, 66.25, 333, 333] # 删掉最后一个列表 数据

# リストをスタックとして使う
　後入れ先だし（last-in,fast-out）.
  append()和pop()的组合
  
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
>>> [3, 4, 5, 6, 7]

stack.pop()
print(stack)
>>> [3, 4, 5, 6]

stack.pop()
print(stack)
>>> [3, 4, 5]

stack.pop()
print(stack)
>>> [3, 4]

# リストをキューとして使う
＃　先入れ先だし(first-in,first-out)では、リストの用途として効率が悪。
　　ただリスト末尾(まつび)としてappend()やpop()は効率だが、リストの先頭でのinsert()やpopは低速なのだ
　　キューの実装より(collection.deque)、を使うべきである、先頭と末尾の両方で要素の追加とpop()が高速に
　　設計されている。

from collections import deque

queue = deque(["Eric","Joe",'VAN'])
queue.append("JACK")
queue.append("Rose")
queue.popleft()  #从起始位左边删除 "Eric"
print(queue)

>>> deque(['Joe', 'VAN', 'JACK', 'Rose'])

queue.popleft() #在从左边起始位删除 "Joe"
print(queue)

>>> deque(['VAN', 'JACK', 'Rose'])

squares = []
for x in range(10):
    squares.append(x**2) # range 生成的列表[0,1,2,3,4,5,6,7,8,9]每个数据都2次方
print(squares)

>>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

＃　簡単に書く方法

squaresA = [x**2 for x in range(10)]
print(squaresA)

>>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squaresB = list(map(lambda x: x**2,range(10)))
print(squaresB)

>>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 经典案列，可以做数据对比

combs = []
for x in [1,2,3]:  # 注意不是一气呵成的把列表[1,2,3]都赋给x 而是 先1 后2 在3 一个一个赋给x
    for y in [3,1,4]: # 注意因上面一个for存在导致 上面列表 1 要跟这句for里的所有数据进行对比
        if x != y: # 列表数据不相等就执行下面的语句进行添加
            combs.append((x,y)) # 添加

print(combs)

>>> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

* 但要注意因为两个 for 中 考虑有 x,y 两个变量存在 
  所以在写的加入或删除语句的时候要加入双括号 例如:append((x,y)) pop((x,y)) 
  在多一个z的话相信是append((x,y,z))
  式がタプルであるときは丸カッコが必須である(上例の(x,y)のように)。 

# 进一步简化（不太建议，不好理解）
[(x,y) for x in [1,2,3]for y in [3,1,4] if x ! = y]

vec = [-4,-2,0,2,4]
# 値を2倍もした新しいリストを生成
vec = [x*2 for x in vec]
print(vec)

>>> [-8, -4, 0, 4, 8]

# 負の数を除去（じょきょ）するようにフィルタをかける
vec = [x for x in vec if x >=0 ]
print(vec)

>>> [-8, -4, 0, 4, 8]

# 全ての要素に関数を適用
vec = [-4,-2,0,2,4]
vec = [abs(x) for x in vec] # 绝对值 所有负数变正数
print(vec)

>>> [4, 2, 0, 2, 4]

fp = [' banana',' loganberry','passion fruita ']  # 注意单词 开头结尾有空格,并返回前后不带空格的相同字符串。
fp = [weapon.strip()for weapon in fp]  # strip()默认是删除单词的开始和结尾空格
print(fp)

>>> ['banana', 'loganberry', 'passion fruit']

fp = ['abanana','loganberry','passion fruita'] # 开头和结尾的单词都加了 a 
fp = [weapon.strip('a')for weapon in fp] # 删掉开头和结尾的 a
print(fp)

>>> ['banan', 'loganberry', 'passion fruit']

# 2值のタプル(数値，2乗値)のリストを生成
ngi = [(x,x**2)for x in range(6)] # 这里的(x,x**2)需要注意不是 所有的 x 都开方
print(ngi)

>>> [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)] # 结果来看只对第二个 x 进行了开方

# 2值のタプル(数値，2乗値)のリストを生成
ngi = [(x**2,x**2)for x in range(6)] # 这里的(x,x**2)需要注意不是 所有的 x 都开方
print(ngi)

>>> [(0, 0), (1, 1), (4, 4), (9, 9), (16, 16), (25, 25)]

# （扩充到二维数组）2值のタプル(2乗値，2乗値)のリストを生成 
ngi = [(x**2,x**2)for x in range(6)] # 这里的(x**2,x**2)所有的两边 x 都开方
print(ngi)

>>> [(0, 0), (1, 1), (4, 4), (9, 9), (16, 16), (25, 25)] # (x**2,x**2) 会扩充到二维数组

# （扩充到三维数组）2值のタプル(2乗値，2乗値)のリストを生成
ngi = [(x**2,x**2,x**2)for x in range(6)] # 这里的(x**2,x**2,x**2)所有的三边 x 都开方
print(ngi)

#不加括号会报错
ngi = [x,x**2 for x in range(6)]
  File "C:/Users/Joker/Desktop/python练习/pyhon チュートリアル/05test.py", line 997
    ngi = [x,x**2 for x in range(6)]
                  ^
SyntaxError: invalid syntax
(構文エーラ:無効な構文)

# (二维转一维数组)forを2つ使ってリストを平滑化(へいかつか)  
vec = [(1, 2), (3, 4), (5, 6), (7, 8)]
vec = [num for elem in vec for num in elem]
print(vec)

>>> [1, 2, 3, 4, 5, 6, 7, 8]

ecl = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
ecl = [sle for ele in ecl for sle in ele]
print(ecl)

>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# (取竖排头一位,从新组合)入れ子のリスト内包　

# 注意 []，要有逗号
max = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
max = [[row[i] for row in max] for i in range(4)]
print(max)

>>> [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


max = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# 想要指定的第三组数据
max = [[row[i] for row in max] for i in range(2,3)] # range(2,3) 可指定哪组数列数据
print(max)

>>> [[3, 7, 11]]

max = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# 拓展版本 稍加拓展效果相同
transposed = []
for i in range(4):
    transposed.append([row[i] for row in max])
print(transposed)

# 但在现实中不使用这么复杂的写法

max = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
max = list(zip(*max))

print(max)

>>> [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

'''

'''
# del文
# delはリストのアイテムを削除する際に、値でなくインデックスで指定する方法がある。
　pop()と違い、値を返さないが異なる。リストを全体の削除、スラスラで削除したり。

a = [-1, 1, 66.25, 333, 333, 1245.5]
del a[0]
print(a)

>>> [1, 66.25, 333, 333, 1245.5]

del a[2:4]
print(a)
>>> [1, 66.25, 1245.5]

del a[:]
print(a)
>>> []

# (del可以删除变量)delは変数丸ごと削除するのも使える

a = [-1, 1, 66.25, 333, 333, 1245.5]
del a
print(a)

NameError: name 'a' is not defined
(找不到a了 可以看出完全删除了)

# タプルとシーケンス
t = 1234, 54321, 'hello'
print(t)
>>> (1234, 54321, 'hello')

print(t[0])
>>> 1234

# タプルは入れ子にできる
u = t, (1, 2, 3, 4, 5)
print(u)

>>> ((1234, 54321, 'hello'), (1, 2, 3, 4, 5))
# タプルは変更不可
t[0] = 88888
print(t)

t[0] = 88888
TypeError: 'tuple' object does not support item assignment

# しかし変更可能オブジェクトを格納(かくのう)できる

v = ([1,2,3],[4,5,6])
print(v)

# 关于 タプル 的理解
empty = ()
sing = 'Hello',  # 要注意后面有个逗号
print(len(empty))  # 输出是 0 没有数据
>>> 0

print(len(sing))  # 输出是 1 有一个タプル ('Hello',) 这里说タプル单指这个括号只有一个括号就是一个タプル
>>> 1

print(sing)
>>> ('Hello',)

# 虽然看似很多但都括在一起了，所以日语叫タプル・パッキング
  len(t)的结果是3 但タプル还是1

t = 1234, 54321, 'hello'  
print(t)
>>> (1234, 54321, 'hello')

print(len(t))
>>> 3

t = 1234, 54321, 'hello'
x, y, z = t
print(x)  # t的第一个数值赋值给 x
>>> 1234
print(x, y, z)  # t 的数值集合 分别赋值给 x y z
>>> 1234 54321 hello

# 如果少于t集合的数值将会报错

t = 1234, 54321, 'hello',555
x, y, z = t
print(x,y,z)  

x, y, z = t
ValueError: too many values to unpack (expected 3)

'''

'''
# 集合(set)
# pythonには集合の為のデータ型まである。
  集合とは＊重複しない要素を順不同で集めたものいである。
  基本的な用途としては＊存在判定(membership testing)や、＊重複エントリの排除がある。
  集合オブジェクトはまた、和、交差、差、対称差の数学的演算をサポートすている。
  ＊集合の生成にはカッコ{}またはset()関数を使用する。
  空の集合を生成するには{}でなくset()を使う必要

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 重複が除去されている
>>> {'orange', 'apple', 'banana', 'pear'}

print('orange' in basket)  # 集合中查找 是否有'orange'  有输出 True 没有输出 False
>>> True

print('crabgrass' in basket)  # 高速な存在判定
>>> False

# 2つの単語から非重複(ユニーク)文字を取って集合演算を実演
a = set('abracadabra')
b = set('alacazam')
print(a)
>>> {'a', 'd', 'c', 'b', 'r'}

# 2つの単語から非重複(ユニーク)文字を取って集合演算を実演
a = set('abracadabra')
b = set('alacazam')
print(a)  # aのユニーク文字
>>> {'c', 'a', 'd', 'r', 'b'}

print(a - b)  # (a有，b没有的文字)aに存在し、bにはない文字　
>>> {'d', 'r', 'b'}

print(a | b)  # (a 或 b都有的文字)aまたはbに存在する文字
>>> {'c', 'z', 'm', 'l', 'a', 'd', 'r', 'b'}

print(a & b)  # (a 和 b都有的文字)aにもbにも存在する文字
>>> {'a', 'c'}

print(a ^ b)  # (a和b不共通的文字)aまたはbにある共通しない文字
>>> {'z', 'r', 'm', 'd', 'l', 'b'}

# リスト内包とよく似た集合内包もサポートされている：
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
>>> {'r', 'd'}

'''
'''
# ディクショナリ　字典
# pythonもう一つの有用なデータ型がディクショナリ
  ＊可変型のオブジェクトが直接間接も含まれているタプルは、キーとして使えない。
  ＊リストもキーとして使えない
  ＊ディクショナリは、キーの唯一性（ひとつのディクショナリの中で重複しないと）
  ＊「キー:値」
  ＊中カッコ対「｛｝」を書けばク空のディクショナリになる
　＊del により「キー:値」をペアごと削除する事もできる、そして値は失われる。

# 以下はディクショナリのささやかな用例である：

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 1234
print(tel)
>>> {'jack': 4098, 'sape': 4139, 'guido': 1234}

print(tel['jack'])
>>> 4098

del tel['sape']
tel['irv'] = 4127
>>> {'jack': 4098, 'guido': 1234, 'irv': 4127}

print(tel)
>>> ['guido', 'irv', 'jack']

print(list(tel.keys()))
>>> ['jack', 'guido', 'irv']

print(sorted(tel.keys()))
>>> ['guido', 'irv', 'jack']

print('jack' in tel)
>>> True

print('jack' not in tel)
>>> False

# dict()コンストラクチタは、「キー:値」ペアのタプルからなるシーケンスからディクショナリを構築
a = dict([('space', 4332), ('guido', 5448), ('jack', 9875)])
print(a)

>>>{'space': 4332, 'guido': 5448, 'jack': 9875}

# また、辞書内包を使えばキーと値を与える任意の式からディクショナリが生成できる
a = {x: x ** 2 for x in (2, 4, 6)}
print(a)

>>> {2: 4, 4: 16, 6: 36}

# ループのテクニック

# ディクショナリにループをかける時、items()メソッドを使えば、キーとそれに対応した値を同時に得られる
# items() 函数以列表返回可遍历的(键, 值) 元组数组。返回可遍历的(键, 值) 元组数组。
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v) # 输出集合里的内容(不带集合本身)

>>> gallahad the pure
    robin the brave

# シーケンスにループをかけるとき、enumerate()関数を使うと位置インデックスとそれに対応した値を同時に得る事ができる
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
>>> 0 tic # 读取前面的 存储位置和存储内容
>>> 1 tac
>>> 2 toe

# 2つ以上のシーケンスに同時にループをかけるとき、zip()関数を使うと両者のエントリをペアにできる
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。 
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

# *返回元组列表。
# 以下实例展示了 zip 的使用方法：
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 打包为元组的列表 ()元祖
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]

# Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
# 基本语法是通过 {} 和 : 来代替以前的 % 。
# format 函数可以接受不限个参数，位置可以不按顺序。
# 实例
# >>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
# 'hello world'
#  
# >>> "{0} {1}".format("hello", "world")  # 设置指定位置
# 'hello world'
#  
# >>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
# 'world hello world'

# 实例2
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
 
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

question = ['name', 'quest', 'favorute color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(question, answers): # zip会把集合中的单词 全部解压出来 变成单纯的字符串 
    print(a) # 会输 lancelot
    print(q) # 会输出 name
    print('what is your {0}? It is {1}.'.format(q, a)) # 输出结果来看 {0} {1}不代表元素位置只代表format里q,a顺序

>>> what is your name? It is lancelot.
>>> what is your quest? It is the holy grail.
>>> what is your favorute color? It is blue.

# 在谈 range()
a = list(range(1, 10, 2)) #  理解的方式（第一个（包括自身））+（最后排那个）得出的数
print(a)
>>> [1, 3, 5, 7, 9]

# シーケンスにを逆順にループするには、まずシーケンスを正順で指定し、これをreversed()関数をコールする:
for i in reversed(range(1, 10, 2)):
    print(i, end=' ')

# >>> 9 7 5 3 1 

# シーケンスをソート順にループするにはsorted()関数を使う
  この関数は元のシーケンスには触れず、新たなにシート済みのリストを返す:
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)): #
    print(f, end=' ')
    
>>> apple banana orange pear  

# 逻辑运算(比較はブール演算子)
string1, string2, string3 = '', 'Trondheim', 'Harmmer'
non_null = string1 or string2 or string3
print(bool(string1))
>>> False
print(bool(string2))
>>> True
print(bool(string3))
>>> True
print(bool(string1 or string2))
>>> True
print(bool(string2 or string3))
>>> True
print(string1 or string2)
>>> Trondheim
print(string2 or string3)
>>> Trondheim
print(non_null)　# 可以理解为两个 True 相比较是真的话取第一个True的数据，反之False跟True相比也是取True
>>> Trondheim

# 比较序列和其它类型
# 注意，元组中如果只有一个元素，必须在元素后面加上一个逗号，否则会被做为元素的对应类型，
a = (1, 2, 3) < (1, 2, 4)
print(a)
>>> True

b = [1, 2, 3] < [1, 2, 4]
print(b)
>>> True

b = [1, 2, 3] == [1, 2, 4]
print(b)
>>> False

c = 'ABC' < 'C' < 'Pythoa' < 'Python'
print(c)
>>> True

d = 'ABC' < 'C' < 'Pythoz' < 'Python'
print(c)
>>> True

e = (1, 2, 3, 4) < (1, 2, 4)
print(e)
>>> True

f = (1, 2) < (1, 2, -1)  # 问题
print(f)
>>> True

g = (1, 2, 3) == (1.0, 2.0, 3.0)  # 1 和 1.0相等以此类推
print(g)
>>> True

h = (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)  # 'aa'和 'abc'对比 第二个a小于b所以不比了返回真
print(h)
>>> True


'''

'''
# （模块）モジュール  
# 以菲波那切数列做例子：先建立一个 fibo.py的py文件，然后在里面写相关的函数
  比如 def fib(n) def fib(2),接下来用import导入fibo 写法是 import fibo 执行
  时用 fibo.fib(100) fibo.fib2(100) 等，如果平凡使用函数则需要本地化 先赋值fib = fibo.fib
  在执行 fib(500) 
# 再谈import导入写法
  from fibo import fib,fib2
  fib(500)
  
  from fibo import * (引用所有模块，正规不建议，有用没用都加载程序容易变慢)
  fib(500)    

# 出于性能考虑，每个模块在每个解释器会话中只导入一遍。
  因此，如果你修改了你的模块，需要重启解释器；或者，如果你就是想交互式的测试这么一个模块，
  可以用 imp.reload() 重新加载，例如 import imp; imp.reload(modulename)。

# モジュールをスクリプトとして実行する
　python fibo.py <arguments>　相当于  python fibo.py 50 或 100 后面接的是引数
  python fibo.py 引数 （日版）
  
  模块中的代码会被执行，就像导入它一样，
  不过此时 __name__ 被设置为 "__main__"。这相当于，如果你在模块后加入如下代码:
  if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
  
  就可以让此文件像作为模块导入时一样作为脚本执行。此代码只有在模块作为
   “main” 文件执行时才被调用:
    $ python fibo.py 50
>>> 1 1 2 3 5 8 13 21 34
  
   * 这通常用来为模块提供一个便于测试的用户接口（将模块作为脚本执行测试需求）。
   

# 有一个具体的模块值得注意： sys ，这个模块内置于所有的 Python 解释器。
  变量 sys.ps1 和 sys.ps2 定义了主提示符和辅助提示符字符串:
import sys
sys.ps1
'>>> '
sys.ps2
'... '
sys.ps1 = 'C> '
C> print('Yuck!') #就是把最原始的符号给替换掉了 比如在终端模式下 正常看到是 >>> 但是改成 C>
Yuck!
C>
   * 这两个变量只在解释器的交互模式下有意义。
   
# dir()関数　
# 内置函数 dir() 用于按模块名搜索模块定义，它返回一个字符串类型的存储列表:

import fibo, sys
dir(fibo)
['__name__', 'fib', 'fib2']
dir(sys)  
['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
 '__package__', '__stderr__', '__stdin__', '__stdout__'.......(还有很多所以省略了)

# 无参数调用时，dir() 函数返回当前定义的命名:
a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()
>>> ['__builtins__', '__doc__', '__file__', '__name__', 'a', 'fib', 'fibo', 'sys']
* 注意该列表列出了所有类型的名称：变量，模块，函数，等等。

# dir() 不会列出内置函数和变量名。如果你想列出这些内容，它们在标准模块 builtins 中定义:
import builtins
dir(builtins) 
>>> ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError'......(还有很多所以省略了)
为了让 Python 将目录当做内容包，目录中必须包含 __init__.py 文件。
# (包)パッケージ
　包通常是使用用“圆点模块名”的结构化模块命名空间。
　例如，名为 A.B 的模块表示了名为 A 的包中名为 B 的子模块。
　* 为了让 Python 将目录当做内容包，目录中必须包含 __init__.py 文件。
    用户可以每次只导入包里的特定模块，例如:
    import sound.effects.echo
    
    这样就导入了 sound.effects.echo 子模块。它必需通过完整的名称来引用:
    sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
    
    *导入包时有一个可以选择的方式:
    from sound.effects import echo

    *import 语句首先核对是否包中有这个子项，如果没有，它假定这是一个模块，并尝试加载它。
     如果没有找到它，会引发一个 ImportError 异常。
     
# 那么当用户写下 from sound.effects import * 时会发生什么事？
  这可能会花掉很长时间，并且出现期待之外的边界效应，导出了希望只能显式导入的包。

  如果包作者不想 import * 的时候导入他们的包中所有模块，那么也可能会决定不支持它（ import * ）。
  例如， sound/effects/__init__.py 这个文件可能包括如下代码:
  
  __all__ = ["echo", "surround", "reverse"]
  这意味着 from sound.effects import * 语句会从 sound 包中导入以上三个已命名的子模块。
  如果没有定义 __all__ ， from sound.effects import * 语句 不会 从 sound.effects 包中导入所有的子模块。
  
  import sound.effects.echo
  import sound.effects.surround
  from sound.effects import *

如果包中使用了子包结构（就像示例中的 sound 包），可以按绝对位置从相邻的包中引入子模块。
例如，如果 sound.filters.vocoder 包需要使用 sound.effects 包中的 echo 模块，
它可以 from sound.Effects import echo。

你可以用这样的形式 from module import name 来写显式的相对位置导入。
那些显式相对导入用点号标明关联导入当前和上级包。
以 surround 模块为例，你可以这样用:  

from . import echo
from .. import formats
from ..filters import equalizer


'''

'''
# (输入和输出)入出力

# 格式化输出
a = 'hello \nworld'
print(repr(a))
print(str(a))
print(str(1/7))
print(type(str(1/7)))

>>> 'hello \nworld'
>>> hello 
>>> world
>>> 0.14285714285714285  #虽然没有引号但是是字符串
>>> <class 'str'>

# 2種類の方法と平方の表を書く
for x in range(1,11):
    print(repr(x).rjust(10),repr(x*x).rjust(4),end=' ') # repr(x).rjust(10) 输入第一个数字的头排空10个空格
    #  repr(x*x).rjust(4) 输出第二个的数字的时候空4个格
    # 上の行でendを使っている事に注目 
    print(repr(x*x*x).rjust(2)) #第三个输出空2个   #但需要注意的是27 64 125 等空格只有一个
>>>         1    1  1
>>>         2    4  8
>>>         3    9 27
>>>         4   16 64
>>>         5   25 125    

for x in range(1, 11):
    # 0 , 1 , 2 分别各个位置 x, x* x, x*x*x
    print('{0:2d}{1:3d}{2:4d}'.format(x, x * x, x * x * x))  # 2d 3d 4d 分别代表空几个格

 >>>  1  1   1
 >>>  2  4   8
 >>>  3  9  27
 >>>  4 16  64
 >>>  5 25 125
 >>>  6 36 216
 >>>  7 49 343
 >>>  8 64 512
 >>>  9 81 729
 >>>  101001000
 
 # 以上是一个 str.rjust() 方法的演示，它把字符串输出到一列，
 # 并通过向左侧填充空格来使其右对齐。类似的方法还有 str.ljust() 和 str.center()。

a = '12'.zfill(5)
print(a)
print(type(a))
>>> 00012  # 不足的位数填充0 因为是 12 是2位 zfill(5)需要5位 所以补了000
>>> <class 'str'> # 输出结果是字符串

a = '-3.14'.zfill(7)
print(a)
>>> -003.14 # 不足的位数填充0 因为是 -3.14 是5位 zfill(7)需要7位 所以补了00

a = '3.14159265359'.zfill(5)
print(a)
>>> 3.14159265359  超过的位数不补

# 方法 str.format() 的基本用法如下:
print('We are the {} who say "{}!"'.format('Knights', 'Ni'))
>>> We are the Knights who say "Ni!"

# 中カッコ {}　是这个符号
* print('{0}and{1}'.format('spam','eggs')) # 注意{0}and{1} 没加空格
>>> spamandeggs # 输出结果

* print('{0} and {1}'.format('spam', 'eggs'))
>>> spam and eggs # {0} and {1} 加了空格

# 位置互换
* print('{1} and {0}'.format('spam', 'eggs'))
>>> eggs and spam


# キーワード引数

print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'
))
>>> This spam is absolutely horrible.

# 位置引数とキーワード引数は自由に混雑できる：
print('The story of {0},{1},and {other}.'.format('Bill', 'Manfred', other='Georg'))
>>> The story of Bill,Manfred,and Georg.

import math
print('The value of PI is approximately {}.'.format(math.pi))
>>> The value of PI is approximately 3.141592653589793.
print(type('The value of PI is approximately {}.'.format(math.pi)))
>>> <class 'str'>

# 因为数组是二维的，所以用{0[0]}{0[1]}{0[2]}查询的
pl = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33]) 
print(tpl)
>>> i am 1, age 2, really 3


# 字段后的‘ ：’  后面加一个整数会限定该字段的最小宽度
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10}==>{1:10d}'.format(name, phone)) # 10代表一共占多少位置 用空格补充 d代表十进制
    print('{0:10}==>{1:10x}'.format(name, phone)) # 10代表一共占多少位置 用空格补充 x代表16进制

>>> Sjoerd    ==>      4127
>>> Sjoerd    ==>      101f
>>> Jack      ==>      4098
>>> Jack      ==>      1002
>>> Dcab      ==>      7678
>>> Dcab      ==>      1dfe

* print('{0:10}<=={1:<10d}'.format(name, phone)) 注意要是想往左对齐需要 在10那里加<  右对齐> 
Sjoerd    <==4127      
Jack      <==4098      
Dcab      <==7678 

# 如果你可以用命名来引用被格式化的变量而不是位置就好了。
# 有个简单的方法，可以传入一个字典，用中括号( '[]' )访问它的键:
# （用这种方式也可以全部输出） 

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack:{0[Jack]:d}: Sjoerd:{0[Sjoerd]:d} ; Dcab:{0[Dcab]:d}'.format(table))

>>> Jack:4098: Sjoerd:4127 ; Dcab:8637678

# 上面的代码在简略一下
# 也可以用 ‘**’ 标志将这个字典以关键字参数的方式传入:
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack:{Jack:d}; Sjoerd:{Sjoerd:d} Dcab:{Dcab:d}'.format(**table))
>>> Jack:4098; Sjoerd:4127 Dcab:8637678

# (旧式的字符串格式化)従来形式の文字列フォーマッティング
# 操作符 % 也可以用于字符串格化。

import math
print('πの値はおよそ%5.3fである。' % math.pi) # 注意的是 字符串有' % ' 后接 % math.pi
>>> πの値はおよそ3.142である。 # %5.3f中的5表示这个数至少要占到5个字符，当然要包括小数点在内，其中的3表示小数点后面有3位小数。 

import math
print('πの値はおよそ%10.3fである。' % math.pi)
>>> πの値はおよそ     3.142である。  # 改成10的话就变成这样带空格 占10位  保留3位

# 3.10 改变后
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

import math
print(f'The value of pi is approximately {math.pi:.3f}.')  # 3f保留三位小数点
>>> The value of pi is approximately 3.142.

import math
print(f'The value of pi is approximately {math.pi:10.3f}.')  # 3f保留三位小数点
>>> The value of pi is approximately      3.142. # 占位10 保留3

# ファイルの読み書き (文件的操作)
# 函数 open() 返回 文件对象，通常的用法需要两个参数：open(filename, mode)。
f = open('workfile', 'w')

* 第一个参数是一个含有文件名的字符串。
  第二个参数也是一个字符串，含有描述如何使用该文件的几个字符。
  mode 为 'r' 时表示只是读取文件；'w' 表示只是写入文件（已经存在的同名文件将被删掉）；
  'a' 表示打开文件进行追加，写入到文件中的任何数据将自动添加到末尾。 
  'r+' 表示打开文件进行读取和写入。mode 参数是可选的，默认为 'r'。

f = open('f.txt', 'w')  # 这里的f多半代表file

with open('f.txt') as f:
    read_data = f.read()
print(f.closed)

>>> True







* 错误示范

f = open('f.txt', 'w')

with open('f.txt') as f:
    read_data = f.read()
f.closed # 这里的closed 写的不对 应该是f.close() 有打开有关闭才被程序认可 
f.read()

>>> f.read()
>>> ValueError: I/O operation on closed file.

** 具体的一些操作

f = open('f.txt', 'r+')  # r+ 读写  ，w 有创建覆盖的意思
for line in f:
    print(line, end=' ')

with open('f.txt', 'r+') as f:  # read_data3 这块用的是 write 需要支持读写所以要加权限
    # 不写'r+'会报错io.UnsupportedOperation: not writable(不支持写入的权限)
    read_data = f.readline()  # readline查询第一行，因为第一行有\n所以换行回车了·
    read_data2 = f.read(5)  # 读取第一行前5个字符
    read_data3 = f.write('This is a test\n')  # 实际在文件里也会被输入进去
    print(read_data)
    print(read_data2)
    print(read_data3)
    print(f.closed)  # 如果下面还有将要处理的文件会提示False

    value = ('the answer', 42)  # 这里是元祖类型，所以需要转换成str才能被f.write 执行
    print(value)
    # *** 问题点怎么输出元祖的个数 这样就能方便对比了str是把（）算进个数所以下面的结果是18
    print(type(value))
    s = str(value)
    print(type(s))
    print(f.write(s))  # 会把('the answer', 42) 内容输入进去

print(f.closed)  # 下面不在有执行所以返回True

>>> 'This is the entire file.\n'
>>> 'Second line of the file\n'
>>> aaaaaaaaaa
>>> bbbb
>>> bbbb
>>> bv
>>> vvvcc
>>> 'This is the entire file.\n'
>>>
>>> 'Seco
>>> 15
>>> False
>>> ('the answer', 42)
>>> <class 'tuple'>
>>> <class 'str'>
>>> 18
>>> True

# f.tell() 返回整数，给出文件对象在文件中的当前位置，
  表示为二进制模式下时从文件开始的字节数，
  以及文本模式下的意义不明的数字。

# f.seek(offset, whence)的用法及说明
# 可以改变文件对象的位置。通过向参考点添加 offset 计算位置；

f = open('workfile', 'rb+')
print(f.write(b'0123456789abcdef'))
>>> 16
print(f.seek(13))  # 标志着13但会移动到文件的第14个字节也就是 d 
>>> 13
print(f.read(1))
>>> b'd'
print(f.seek(-3, 2))  # 移动到文件倒数第3个字节 2 代表倒数 0 代表文件起始处 1代表当前
>>> 13
print(f.read(1))
>>> b'd'
print(f.seek(33, 2))  # 若超出范围内容会变成  b'' 第19位 即便超出数据范围也可以无限偏移
>>> 49
print(f.read(1))
>>> b''

* 在文本文件（模式字符串未使用 b 时打开的文件）中，只允许相对于文件开头搜索
*（使用 seek(0, 2) 搜索到文件末尾是个例外），
* 唯一有效的 offset 值是能从 f.tell() 中返回的，或 0。其他 offset 值都会产生未定义的行为。

# 使用 json 保存结构化数据
# 注解 JSON 格式通常用于现代应用程序的数据交换。
# 程序员早已对它耳熟能详，可谓是交互操作的不二之选。

import json
x = [1, 'simple', 'list'] #  数据也可以这么写[{1, 'simple', 'list'}]
print(json.dumps(x))
>>> [1, "simple", "list"]

y = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
data = json.loads(y)
print(data)
>>> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.

'''

'''
# エラーと例外(错误和异常)
# 構文エラー (syntax error) と　例外 (exception) 
# たとえ文や式が構文的に正しくても、実行しようとしたときにエラーが発生するかもしれません。
# 実行中に検出されたエラーは 例外 (exception) と呼ばれ、常に致命的とは限りません。

10 * (1/0)
>>> ZeroDivisionError: division by zero

4 + spam * 3
>>> NameError: name 'spam' is not defined

'2' + 2
>>> TypeError: can only concatenate str (not "int") to str

* 错误信息的最后一行说明程序遇到了什么类型的错误。
  异常有不同的类型，而类型名称会作为错误信息的一部分中打印出来：
  上述示例中的异常类型依次是：ZeroDivisionError， NameError 和 TypeError。


* 可以编写程序处理选定的异常。下例会要求用户一直输入内容，直到输入有效的整数，
  但允许用户中断程序（使用 Control-C 或操作系统支持的其他操作）；
  注意，用户中断程序会触发 KeyboardInterrupt 异常。(Ctrl + C)
  
while True:
    try:
        x = int(input("Please enter a number：")) # 输入数字不在执行，但是输入字符转会报错下面的内容
        break
    except ValueError:
        print("Oops! That was no valid number.Try again...")


* try 语句的工作原理如下：
  首先，执行 try 子句 （try 和 except 关键字之间的（多行）语句）。
  如果没有触发异常，则跳过 except 子句，try 语句执行完毕。
  如果在执行 try 子句时发生了异常，则跳过该子句中剩下的部分。 
  如果异常的类型与 except 关键字后指定的异常相匹配，则会执行 except 子句，
  然后跳到 try/except 代码块之后继续执行。
  如果发生的异常与 except 子句 中指定的异常不匹配，则它会被传递到外部的 try 语句中；
  如果没有找到处理程序，则它是一个 未处理异常 且执行将终止并输出如上所示的消息。


*** try 语句可以有多个 except 子句 来为不同的异常指定处理程序。 
    但最多只有一个处理程序会被执行。 处理程序只处理对应的 try 子句 中发生的异常，
    而不处理同一 try 语句内其他处理程序中的异常。
    except 子句 可以用带圆括号的元组来指定多个异常，例如:
    except (RuntimeError, TypeError, NameError):
        pass

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B, C, D]:
    try:
        raise cls() # 触发异常
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
>>> B
>>> C
>>> D

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:  # 这里的err直接返回[Errno 2] No such file or directory: 'myfile.txt'
    print("OS error: {0}".format(err))  # 这里直接输出OS error: [Errno 2] No such file or directory: 'myfile.txt'
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
    
>>> OS error: [Errno 2] No such file or directory: 'myfile.txt'

import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readline()), 'lines')
        f.close()

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst)) # 例外インスタンスの型
    print(inst.args)  # .argsに格納された引数
    print(inst)　　　 # __str__により引数は直接表示可能であるが、
    　　　　　　　　　# これは例外のサブクラスでオーバーライトされ得る 
    x, y = inst.args　# 引数のアンパック
    print('x =', x)
    print('y =', y)
>>> <class 'Exception'>
>>> ('spam', 'eggs')
>>> ('spam', 'eggs')
>>> x = spam
>>> y = eggs


def this_fails():
    x = 1 / 0
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

>>> Handling run-time error: division by zero

# 例外の送出
# プログラマはraise文により指定の例外を強制的に発生させられるようになっている。
# raise 语句允许程序员强制抛出一个指定的异常。例如:

raise NameError('HiThere')

>>> Traceback (most recent call last):
>>>   File "<stdin>", line 1, in ?
>>> raise NameError('HiThere')
>>> NameError: HiThere

# raise 唯一的参数就是要触发的异常。
# 这个参数必须是异常实例或异常类（派生自 Exception 类）。
# 如果传递的是异常类，将通过调用没有参数的构造函数来隐式实例化：
* raise ValueError  # shorthand for 'raise ValueError()'

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise   # 输出print语句后，在跳回上面的raise语句的异常

>>> An exception flew by!
>>>   File " 文件执行路径 ", line 1957, in <module>
>>>     raise NameError('HiThere')
>>> NameError: HiThere

# ユーザー定義例外 (异常链)
# raise 语句支持可选的 from 子句，该子句用于启用链式异常。 例如：
# raise RuntimeError from OSError #これは変形させるのに便利である。例を示す:　（3.10例）

def func():
    raise IOError

try:
    func()
except IOError as exc:
    raise RuntimeError('データベースのオープンに失敗しました') from exc

>>> Traceback (most recent call last):
>>> File" ", line 1974, in <module>
>>>    func()
>>> File " ", line 1971, in func
>>>    raise IOError
>>> OSError
>>> The above exception was the direct cause of the following exception:  
　　# (上の例外は以下の例外の直接の原因です)
>>> Traceback (most recent call last):
>>>  File " ", line 1976, in <module>
>>>   raise RuntimeError('データベースのオープンに失敗しました') from exc
>>> RuntimeError: データベースのオープンに失敗しました

# 定义清理行为  (クリーンアップ動作の定義)

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye,world!') # 先输出'Goodbye,world!' 在输出异常
    
>>> Goodbye,world!
>>> Traceback (most recent call last):
>>>   File " ", line 1993, in <module>
>>>     raise KeyboardInterrupt
>>> KeyboardInterrupt

# 不管有没有发生异常，finally子句 在程序离开 try 后都一定会被执行。
# try 语句经由 break ，continue 或 return 语句退 出也一样会执行 finally 子句。

def divide(x, y):
     try:
         result = x / y
     except ZeroDivisionError:
         print("division by zero!")
     else:
         print("result is", result)
     finally:
         print("executing finally clause")

print(divide(2, 1))
>>> result is 2
>>> executing finally clause

print(divide(2, 0))
>>> division by zero!
>>> executing finally clause

print(divide("2", "1"))
>>> executing finally clause
>>> Traceback (most recent call last):
>>>  File "<stdin>", line 1, in ?
>>>  File "<stdin>", line 3, in divide
>>> TypeError: unsupported operand type(s) for /: 'str' and 'str'

# オブジェクトに定義してあるクリーンアップ動作(预定义清理行为)


for line in open("myfile.txt"):
    print(line)
** 这段代码的问题在于在代码执行完后没有立即关闭打开的文件。
   这在简单的脚本里没什么，但是大型应用程序就会出问题。
   with 语句使得文件之类的对象可以 确保总能及时准确地进行清理。
   
with open("myfile.txt") as f:
    for line in f:
        print(line)       

** 语句执行后，文件 f 总会被关闭，即使是在处理文件中的数据时出错也一样。
   其它对象是否提供了预定义的清理行为要查看它们的文档。       

*-*-*- 课外
# 吸收多余元素 - 序列解包
*x,y = [1,2,3]
print(x,y)
>>> [1, 2] 3

x,y *rest = (1,2,3,4,5)
print(x,y,rest)
>>> 1 2 [3,4,5]

first,*middle,last = "Leonardo di ser Piero Da Vinci".split() # .split() 按空格拆分分出来就是个列表
print(first,middle,last)
>>> Leonardo ['di','ser','piero','Da'] Vinci

*-*-*- 课外
# 非空既真
print(bool(None))
>>> False

print(bool([]),bool(()),bool({})) # 列表 list 元祖() 集合{} 空的就算假
>>> False False False

print(bool([1,2,])),bool((2,)),bool({"name":"jude","age":17})
>>> True True True

print(3 *(4))
>>> 12

print((4,)*3)
>>> (4,4,4)

*-*-*- 课外
# 断言
scores = [78, 99, 22, 12, 15, 67]

def computeAverageScores(scores):
    # scores list 里的数要小于等于100否则 max(scores)会报错  min(scores) 是最小也要 >=0 
    assert len(scores) > 0 and max(scores) <= 100 and min(scores) >= 0   
    return sum(scores) / len(scores)

print(computeAverageScores(scores))
>>> 48.833333333333336
print('%.3f' % computeAverageScores(scores))
>>> 48.833

*-*-*- 课外

# for loop
# 驴打滚的债/滚雪球的复利 / 利滚利  # 因为安装matplotlib模块所以运行不了

fBalance = 10000
fRate = 0.0005
balances = []
for i in range(365 * 30):
    fBalance = fBalance + fBalance * fRate  # 贷款余额 = 本金 + 本金*利率
    balances.append(fBalance)               # 把贷款余额存入列表绘图用
print("30年后连本带利欠款总额:%.2f" % fBalance)

from matplotlib import pyplot as plt        # 贷款余额 vs 天数增长曲线

plt.plot(list(range(365 * 30)), balances)
plt.title("Loan Balance grow by days")
plt.show

*-*-*- 课外
# while 循环 - 跟C语言一致
sum = i = 0
while i <= 100;
    sum += i
    i+=1
print("sum of (1,2,.....,100)=",sum)

>>> sum of (1,2,.....,100)= 5050

*-*-*- 课外
# 也有break,用法跟C语言相同
# 微时间 - 九层之台，起于累土  # 一张纸对折几次能超过珠穆拉玛峰

iCounter = 0                # 对折次数
fThickness = 0.0001         # 纸厚
while True:
    if fThickness > 8844.43:    # 超过珠峰高度就停止循环
        break
    else:
        fThickness *= 2         # 对折一次厚度翻倍
        iCounter += 1           # 对折次数加1
print("纸对折 %d 次后的厚度为 %.2f 米,超过了珠穆拉玛峰。" % (iCounter, fThickness))

>>> 纸对折 27 次后的厚度为 13421.77 米,超过了珠穆拉玛峰。

*-*-*- 课外
# 可以将包含键值对的列表转换为字典
abc = [('name', 'Dorothy'), ('id', '100003'), ('age', 26)]
dorothy = dict(abc)

print(dorothy)
>>> {'name': 'Dorothy', 'id': '100003', 'age': 26}

print(type(dorothy))
>>> <class 'dict'>

*-*-*- 课外
# 也可以通过dict()函数中的关键字参数提供键值对

dorothy = dict(name='Dorothy', id='10003', age=26)
# 在C语言里，函数的参数是按顺序分配的，Python里，可以照名字分配...
# 字典的基本操作
print(dict)
>>> <class 'dict'>
print(len(dorothy))
>>> 3
for i, k in dorothy.items():
    print(i, k)
    
>>> name Dorothy
>>> id 10003
>>> age 26

print(dorothy["id"])
>>> 10003

dorothy['gender'] = 'female'
>>> 'gender': 'female'
del dorothy['id']
>>> {'name': 'Dorothy', 'age': 26, 'gender': 'female'}
print("dict after del:", dorothy)
>>> dict after del: {'name': 'Dorothy', 'age': 26, 'gender': 'female'}

if "age" in dorothy:
    print("Key age exists in dict dorothy.")
>>> Key age exists in dict dorothy.

*-*-*- 课外
# 字典的嵌套
d = {"dora": {}, "jack": {}}
d["tom"] = {"name": "tom", "age": 27}
print(d["tom"]["age"])

>>> 27
print(d)
>>> {'dora': {}, 'jack': {}, 'tom': {'name': 'tom', 'age': 27}}


# 除了使用占位符，Python里格式化字符串还有更好的办法
sText = "Mary have {} lambs , thy are {n1},{n2} and " \
        "{}.".format(3, 'cot', n1='happy', n2='nauty')
print(sText)
>>> Mary have 3 lambs , thy are happy,nauty and cot.
# {}称为替代字段，支持设置宽度，补0，对齐等复杂语法

# 有了字典，字符串的格式化可以更容易
dora = {"name": "Dora", "age": 27, "salary": 12000}
sText = "Name:\t{name}\nAge:\t{age}\nSalary:\t{salary}"
print(sText.format_map(dora))
>>> Name:	{name}
>>> Age:	{age}
>>> Salary:	{salary}

print(sText)
>>> Name:	Dora
>>> Age:	27
>>> Salary:	12000

# get成员函数为不存在的键，提供默认值
dora = {'id': '10003', 'name': 'Dora Chen', 'gender': 'female', \
        'age': 32, 'title': 'Sales'}
print("Title:", dora.get("title"))
>>> Title: Sales

print("Salary:", dora.get("salary", 2000))
>>> Salary: 2000


*-*-*- 课外
# 字典遍历
dora = {'id': '10003', 'name': 'Dora Chen', 'gender': 'female', \
        'age': 32, 'title': 'Sales'}
for x in dora:  # 遍历键
    print(x)
>>> id
>>> name
>>> gender
>>> age
>>> title

for k in dora.keys():  # 遍历键
    print(k)
>>> id
>>> name
>>> gender
>>> age
>>> title

for v in dora.values():  # 遍历值
    print(v)
>>> 10003
>>> Dora Chen
>>> female
>>> 32
>>> Sales

for k, v in dora.items():  # 遍历键值对
    print(k, v)
>>> id 10003
>>> name Dora Chen
>>> gender female
>>> age 32
>>> title Sales

*-*-*- 课外
# 万物皆对象，函数也是对象
def add(x, y):
    return x + y

tmp = 1
# callable 函数 检测参数是否可以调用,只有函数是可以调用的
print(callable(add), callable(tmp)) # 所以callable(add)是True  callable(tmp) False
>>> True False

tmp = add  # 名字绑定关系，tmp也被绑定到add对象上 所以有同功能
print(tmp(3, 2))
>>> 5

*-*-*- 课外
# 函数文档
help(print)

# 自己写的函数文档 (内容上可以加转义符)
def add(x, y):
    "Calculate thr sum of two numbers. \
    \nThe Numbers could be integer or float."
    return x + y

# doc  前后要有两个__ __
print(add.__doc__)

*-*-*- 课外
# 函数的传参就是名字绑定，对于只读数据类型，可以等同于C语言中的传值
def swap(x, y):
    x, y = y, x
    s = x + y
    return s

# a = 3 b = 5 传到函数里 x y 在  a，b 的绑定之上所以只是x y 做了交换 a b 没做交换
a, b = eval(input("input a and b(a,b):"))
>>> input a and b(a,b):3,5 # 假设3,5 

c = swap(a, b)
print("a=%d,b=%d,c=%d" % (a, b, c))
>>> a=3,b=5,c=8


*-*-*- 课外
# 函数的传参就是名字绑定，对于可修改类型，相当于C++中的传引用
def initPerson(person, id, name, age, gender, title):
    assert type(person) == dict
    person["id"] = id
    person["name"] = name
    person["gender"] = gender
    person["title"] = title
    person["saslary"] = []


dora = {}
initPerson(dora, "10001", "Dora Chen", 26, 'female', 'Sales') # dora 绑定在person上所以可以进行修改 
print("dict dora after function call:\n", dora)
>>> dict dora after function call:
>>>  {'id': '10001', 'name': 'Dora Chen', 'gender': 'female', 'title': 'Sales', 'saslary': []}

# 把一个对象传给第三方函数，担心在函数内被修改？ copy，或者切片大法

*-*-*- 课外
# 函数的作用域
def func():
    # global x
    x = 77
    # globals()["x"] = 99
    print("x inside func:", x)  # 内部标有数字77的话是调用的是内部，如果没有吊用外部的x = 1
    print("y inside func:", y)
x = 1
y = 2
func()
print("x outside func:", x)
>>> x inside func: 77
>>> y inside func: 2
print("y outside func:", y)
>>> x outside func: 1
>>> y outside func: 2

'''

'''
# 类

class MyClass:
    """A simple example class"""
    i = 1234
    def f(self):
        return 'hello world'

x = MyClass.i  # 返回一个整数
v = MyClass.f  # 一个方法对象
xv = MyClass()
xvk = xv.f
print(xvk())
>>> hello world

print(x)
>>> 1234

MyClass.i = 5
print(x)
>>> 1234

print(v)
>>> <function MyClass.f at 0x0000024C2F3AB9D0>

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r)
>>> 3.0
print(x.i)
>>> -4.5


# 类和实例变量
# 一般来说，实例变量用于对每一个实例都是唯一的数据，类变量用于类的所有实例共享的属性和方法:

class Dog:
    kind = 'canine' # どのインスタンスも持つ事になるクラス変数

    def __init__(self, name):　
        self.name = name　# インスタンスごとに固有のインスタンス変数


d = Dog('Fido')
print(d)
>>> <__main__.Dog object at 0x0000023DDB1865E0>
e = Dog('Buddy')
print(e)
>>> <__main__.Dog object at 0x0000023DDB19D460>
print(d.kind)　　#　すべての犬に共通
>>> canine
print(e.kind)　　#　すべての犬に共通
>>> canine
print(d.name)　　#　dに固有
>>> Fido　
print(e.name)　　#　eに固有
>>> Buddy

#　 不正确设计
class Dog:
    tricks = []  # クラスの使い方間違っている

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
print(d.name)
>>> Fido
e = Dog('Buddy')
print(e.name)
>>> Buddy
d.add_trick('roll over')
print(d.tricks)
>>> ['roll over']
e.add_trick('play dead')
print(e.tricks)
>>> ['roll over', 'play dead']  # 这个结果就是全体共享了 

# 这个类的正确设计应该使用一个实例变量:（正解はインスタンス変数を使う事だ）

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
print(d.name)
>>> Fido
e = Dog('Buddy')
print(e.name)
>>> Buddy
d.add_trick('roll over')
print(d.tricks)
>>> ['roll over']
e.add_trick('play dead')
print(e.tricks)
>>> ['play dead'] # 不在共享分离了

'''

'''
# 操作系统接口 (標準のライブラリめぐり)

import os

print(os.getcwd())  # 今いるディレクトリを返す
>>> C:\\Users\Joker\Desktop\python练习\pyhon チュートリアル
# os.chdir('/server/accesslogs')  # カレントディレクトリ変更

os.system('mkdir today')  # システム側のシェルでmkdirコマンドを実行
print(os.system)

'''

import os

# print(os.getcwd())  # 今いるディレクトリを返す
# >>> C:\\Users\Joker\Desktop\python练习\pyhon チュートリアル
# # os.chdir('/server/accesslogs')  # カレントディレクトリ変更print(os.getcwd())  # 今いるディレクトリを返す
# >>> C:\\Users\Joker\Desktop\python练习\pyhon チュートリアル
# # os.chdir('/server/accesslogs')  # カレントディレクトリ変更

os.system('mkdir today')  # システム側のシェルでmkdirコマンドを実行
print(os.system(utf-8))