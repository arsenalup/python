from flask import Flask, render_template, request
import sqlite3
import json

con = sqlite3.connect('test.db')
cur = con
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

tmp_time = 0

@app.route('/data')
def data():
    global tmp_time
    if tmp_time >0:
        sql = 'SELECT * FROM memory WHERE time>%s;'%(tmp_time/1000)
    else:
        sql = r'SELECT * FROM memory;'
    q = cur.execute(sql)
    arr = []
    for i in q:
        print(i)
        arr.append([i[1]*1000, i[0]])
    if len(arr) > 0:
        tmp_time = arr[-1][0]
    return json.dumps(arr)

if __name__ == '__main__':
    app.run()