import uuid
import MYSQLdb


def create_code(num, length):
    result = []
    while True:
        uuid_id = uuid.uuid1()
        temp = str(uuid_id).replace('-', '')[:length]
        if temp not in result:
            return result.append(temp)
        if len(result) == num:
            break
    return result


def save_to_mysql(num_list):
    conn = MYSQLdb.connect(host='', user='', passwd='', port='')
    cur = conn.cursor()

    sql_create_database = 'create database if not EXISTS  activecode_db'
    cur.execute(sql_create_database)

    conn.select_db('activecode_db')
    sql_create_table = 'create table if not exists active_codes(active_code CHAR(32) )'
    cur.execute(sql_create_table)

    cur.executemany('insert into actice_code VALUE(%s) ', num_list)

    conn.commit()
    cur.close()
    conn.close()

