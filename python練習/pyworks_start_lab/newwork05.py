"""
成績管理表のクラス を作る
1.中学生の名前と３教科（国語、数学、英語）
の成績を属性にもつクラス（型）を作成し、5人分のインスタンスを作成してください。
2.random モジュールを使って、任意の名前と成績を 100 
人分生成してファイルに保存してください。
"""
class Stu1:
    def __school__(self,name = '',lang = '',math = '',eng = ''):
        self.name = name
        self.lang = lang
        self.math = math
        self.eng = eng
    
        def show_attributes(self):
            print("中学生の名前:",self.name)
            print("国語の点数:",self.lang)
            print("数学点数:",self.marh)
            print("英語点数:",self.eng)
            data = Stu1("Jack","80","85","66")
            data.show_attributes()
            print(Stu1)