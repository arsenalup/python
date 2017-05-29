#-*- coding:utf-8 -*-
import pymongo
import json
import  requests
import sys
client=pymongo.MongoClient()
db=client.wangyimisic
db_songlist=db.songlist
db_lyrics=db.lyrics

headers = {
    'Cookie': 'appver=1.5.0.75771',
    'Referer':'http://music.163.com/'
}

def song_list(keywords):
    url = 'http://music.163.com/api/search/pc'
    data = {'s':keywords,'offset':1,'limit':10,'type':1000}
    req = requests.post(url,data=data,headers=headers)
    content = req.json()
    content=content
    song_id=[]
    for cont in content['result']['playlists']:
        song_id.append(cont['id'])

    return song_id

def save_song(song_id):
    url='http://music.163.com/api/playlist/detail?id={}&updateTime=-1'
    for i in song_id:
        print 'save list',i
        url=url.format(i)
        req = requests.post(url,  headers=headers)
        content = req.json()
        db_songlist.insert_one(content['result'])

def save_lyric():
    url='http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'
    for song in db_songlist.find():
        for track in song['tracks']:
            song_id=track['id']
            url=url.format(song_id)
            print 'savd lyric',song_id
            req = requests.post(url, headers=headers)
            content = req.json()
            db_lyrics.update_one({'id':song_id},{'$set':content},upsert=True)


def main():
    keywords=raw_input('input keywords:')
    song_id=song_list(keywords)
    save_song(song_id)
    save_lyric()


if __name__ == '__main__':
    main()




