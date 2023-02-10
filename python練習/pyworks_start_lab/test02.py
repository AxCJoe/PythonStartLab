class Stu1:
    def __school__(self,name='',lang='',math='',eng=''):
        self.name = name
        self.lang = lang
        self.math = math
        self.eng = eng
    a = Stu1(name='Jack')
    b = Stu1(lang="80")
    c = Stu1(math="78")
    d = Stu1(eng="88")

    print(a.name)
    print(b.lang)
    print(c.math)
    
    #     def show_attributes(self):
    #         print("中学生の名前:",self.name)
    #         print("国語の点数:",self.lang)
    #         print("数学点数:",self.marh)
    #         print("英語点数:",self.eng)
    #          data = Stu1("Jack","80","85","66")
    #         # data.show_attributes()
    # print(Stu1)