import time
import os
import sqlite3 as sqlite3

created = os.path.exists('test.db')
con = sqlite3.connect('test.db')
if not created:
    sql = '''
          CREATE TABLE memory
          (
          memory INT ,
          time INT 
          );
          '''
    con.execute(sql)
db = con

def getMem():
    with open('/proc/meminfo') as f:
        total = int(f.readline().split()[1])
        free = int(f.readline().split()[1])
        ava = int(f.readline().split()[1])
        buffers = int(f.readline().split()[1])
        cache = int(f.readline().split()[1])
    mem_use = total - free - buffers - cache
    t = int(time.time())
    print(mem_use/1024)
    sql = r'''
            INSERT INTO memory (memory, time)
            VALUES (%s,%s);
        '''% (mem_use/1024,t)
    db.execute(sql)
    db.commit()
while True:
    time.sleep(1)
    getMem()