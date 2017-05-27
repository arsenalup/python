#-*- coding:utf-8 -*-
import requests
import csv
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

headers={
    'Cookie':'aliyungf_tc=AQAAACzRS1CtwQgAgQGdtIKpN9iMSx21; acw_tc=AQAAAFIa5ye58AkAgQGdtM1/YJ7yJlbq; q_c1=99bcb02b54b94d63999f9d6cefbf71a8|1495793752000|1495793752000; _xsrf=9127ca7c3fdab25863f3032e36aaf990; r_cap_id="ZDI4MGE2NmU5YTM4NDI5ZGE5MGU1YjZkMDM3MmJiM2I=|1495793752|ce7814386115748dac95722cf941fd771d66cb0a"; cap_id="ODg4Y2QwZDE4NzFkNDJjNmE1ZjQwNjJlZjEwOTM3MmI=|1495793752|b8eb846a44d59831915adb85928463824a62e370"; d_c0="AJDCcAIk0QuPTjJEvjuH4ASh9lblwAB6w6c=|1495793753"; _zap=7a4b5315-9102-4488-abf4-3a985129b0d6; l_n_c=1; __utma=51854390.1290202077.1495793762.1495793762.1495793762.1; __utmc=51854390; __utmz=51854390.1495793762.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100--|2=registration_date=20161115=1^3=entry_date=20161115=1; z_c0=Mi4wQUlBQWV3eGcyUW9Ba01Kd0FpVFJDeGNBQUFCaEFsVk5hbzFQV1FBQ1VEZHFrMVhqVjRUbFZaQ1doSGNLSmVDQ2Zn|1495793773|9b18457cdf81217d21c291a811b37069ca8130af',
    'Host':'www.zhihu.com',
    'Referer':'https://www.zhihu.com/people/pa-chong-21/following',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
url_1='https://www.zhihu.com/api/v4/members/'
url_2='/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset='

to_crawl=['pa-chong-21']
crawled=[]
all_user=[]
finished=threading.Event()

def crawl(url):
    global to_crawl,crawled,finished
    req=requests.get(url=url,headers=headers)
    data=req.json()
    for user in data['data']:
        if user['follower_count']>100000:
            token=user['url_token']
            if token not in to_crawl and token not in crawled:
                print user['name']
                to_crawl.append(token)
                all_user.append([token, user['name'], user['follower_count'],user['is_following']])
                print 'add token',token
                finished.set()
    return data['paging']

def get_following(user):
    print 'crawing',user
    global to_crawl,crawled
    url=url_1+user+url_2+'0&limit=20'
    paging=crawl(url)
    totals=paging['totals']
    count=20
    while count<totals and count<1000:
        url = url_1 + user + url_2 + str(count)+'&limit=20'
        t=threading.Thread(target=crawl,args=(url,))
        t.start()
        count+=20
    print 'to_crawl',to_crawl
    print  'crawed',crawled


while len(to_crawl)>0:
    user=to_crawl.pop()
    crawled.append(user)
    get_following(user)

    while len(to_crawl)==0 and threading.active_count()>1:
        print  'to_crawl',to_crawl
        print 'wait',threading.active_count()
        finished.clear()
        finished.wait(3)

with open('zhihudav','w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['token','name','follws','是否关注'])
    for data in all_user:
        writer.writerow(data)
