#-*- coding:utf-8 -*-
import requests
import json
import csv
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

headers={
'Cookie':'uuid="w:8d4bef04531c40a88504bbb08597bbaa"; UM_distinctid=15c45358ebf4fb-01e42ef7c50402-8373f6a-144000-15c45358ec2ea1; tt_webid=6424453945696192001; _ga=GA1.2.1452030574.1495809757; _gid=GA1.2.1731173785.1495811747; CNZZDATA1259612802=1114325011-1495807249-%7C1495807249; __tasessionId=o0aseb2eg1495809756630',
'Host':'www.toutiao.com',
'Referer':'https://www.toutiao.com/ch/news_sports/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
url='https://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time={}&max_behot_time_tmp={}&tadrequire=true&as=A105E99248C470C&cp=592834B720BC4E1'
next_time=['1495809447']
all_news = []
def crawl(url):
    global next_time
    req=requests.get(url=url,headers=headers)
    data=req.json()
    next_time.append(data['next']['max_behot_time'])
    for news in data['data']:
        try:
            all_news.append([ news['title'], news['abstract'],news['comments_count']])
        except Exception as e:
            print
            continue

    return all_news

def save(all_news):
    with open('toutiao.csv','w')as f:
        writer=csv.writer(f)
        writer.writerow(['标题','内容','评论'])
        for i in all_news:
            writer.writerow(i)

def main():
    global next_time
    for i in range(5):
        time_stamp=next_time.pop()
        next_url=url.format(time_stamp,time_stamp)
        print '正在获取：',next_url
        all_news=crawl(next_url)
        save(all_news)

if __name__ == '__main__':
    main()
