# -*- coding:utf-8 -*-
#给定一个包含若干 py 文件的目录，统计该目录中所有文件的总代码行数，并分别列出注释行、空行与有效代码的行数。
import os
import re
dir_1=r'd:\temporary\programs'#目标文件夹
blank_1=0
valid_1=0
mark_1=0
total_1=0
for root,dirs,files in os.walk(dir_1):#遍历文件得数据
    for files_1 in files:
        file_root=os.path.join(root,files_1)#文件地址
        open_file=open(files_root,'r')
        file_content=open_file.readlines()
        open_file.close()
        print u'正在统计： ',file_root
        for i in file_content:
            judge=re.search(r'(?<=\s)*\S',i)#匹配空字符0次或无限次，在匹配第一个非空
            if not judge:
                blank_1+=1
            elif judge.group()=='#':
                mark_1+=1
            else:
                valid_1+=1
            total_1+=1
print '空白行：',blank_1
print '注释行：',mark_1
print  'daima:',valid_1
print  'zong:',total_1

