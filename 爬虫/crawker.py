#-*- coding:utf-8 -*-
import requests
import pymongo
import time

client=pymongo.MongoClient()
db=client.douban
collection=db.movies
col_casts=db.casts


def get_cast(id):
    if not id:
        return
    print 'fetching',id
    try:
        url='https://api.douban.com/v2/movie/celebrity/'+str(id)
        req=requests.get(url)
        data=req.json()
        print ('updatinf',id)
        col_casts.update_one({'id':data['id']},{'$set':data},upsert=True)
        print ('done',id)
    except Exception as e:
        print (e,id)

for movie in collection.find():
    casts=movie['casts']
    for cast in casts:
        print (cast['name'],cast['id'])
        get_cast(cast['id'])
        time.sleep(1.5)