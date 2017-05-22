# -*- coding: utf-8 -*-
import sqlite3
import os
import string
import random


def make_number():
    b = []
    while len(set(b)) < 200:
        for i in range(0, 200):
            a = list(string.ascii_letters)
            random.shuffle(a)
            a = ''.join(a)
            b.append(a[:8])
    return b

def save(b):
    a=0
    for i in range(0, len(b)) :
        a+=1
        sql = r'''
            INSERT INTO CODES (code)
            VALUES ('%s');
        '''% (b[i])
        conn.execute(sql)
        conn.commit()
        # conn.close()
        print '保存成功%d'%(a)


DATABASE = 'youhui.db'
created = os.path.exists(DATABASE)
conn = sqlite3.connect(DATABASE)
if not created:
    sql =r'''
          CREATE TABLE CODES
          (
          code CHAR(8) primary key
          );
          '''
    conn.execute(sql)

save(make_number())
# queryset = conn.execute('SELECT * FROM CODES;')
# for q in queryset:
        # print q[0]

