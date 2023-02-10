'''
Author: your name
Date: 2022-02-11 20:35:05
LastEditTime: 2022-02-12 13:55:46
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python练习\output.py
'''


fp = open('note.txt', 'w')  # 打开文件 w--write 路径个这个python文件在一起
print('终于学会python的文件输出了', file=fp)  # 输出到文件中
fp.close()  # 关闭文件

fp = open('note++.txt', 'w')
print('文件输出python', file=fp)
fp.close()

fp = open('wahaha.txt', 'w')
print('shuchuwenjian', file=fp)
fp.close()

fp = open('hahah.txt', 'w')
print('sss', file=fp)
fp.close()
