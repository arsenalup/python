#-*- coding:utf-8 -*-
import requests
import pymongo

client=pymongo.MongoClient()
db=client.douban
collection=db.movies
for start in range(0,100,20):
    print start
    url='http://api.douban.com/v2/movie/top250?start='+str(start)
    req=requests.get(url)
    data=req.json()
    print 'inserting',start
    collection.insert_many(data['subjects'])
    print ('finish',start)
