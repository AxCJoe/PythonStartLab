# -*- coding: utf-8 -*-
score = eval(input('请输入您的成绩：'))

# 判断
if score < 0 or score > 101:
    print('成绩有误')
elif score < 60:
    print('你的成绩不及格是\'D\'')
elif score > 60 and score < 70:
    print('你的成绩及格是\'C\'')
elif score > 70 and score < 80:
    print(r"你的成绩及格式'B'")
elif score > 80 and score < 90:
    print('你的成绩及格式'"'A'")
elif score > 90 and score <= 100:
    print('你的成绩及格式'"'S'")
else:
    print('输入有误，重新输入')
