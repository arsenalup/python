# -*- coding: utf-8 -*-
import re
import requests
import time
from bs4 import BeautifulSoup
import threading
import time
import os


class Spider(object):
    def __init__(self):
        self.siteURL = 'http://jandan.net/ooxx/page-'
        if not os.path.exists('E:\jiandan'):
            os.makedirs('E:\jiandan')


    def getSource(self,url):
        user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
        headers = {'User_agent': user_agent}
        r = requests.get(url, headers=headers)
        result = r.content
        return result

    def saveDetailPage(self,detailURL,number):
        source = self.getSource(detailURL)
        soup = BeautifulSoup(source, 'html.parser')
        res = soup.find_all('img')
        num = 1
        for i in res:
            b = i['src']
            b = 'http:' + b
            print b
            req = requests.get(b)
            time.sleep(0.1)
            num += 1
            fileName=r'E:\jiandan/%s-%s.jpg'%(number,num)
            f=open(fileName,'wb')
            f.write(req.content)
            print 'save',fileName
            f.close()

spider = Spider()
start_time = time.time()
start=raw_input('input start:')
end=raw_input('input end page:')
number = int(start)
for page in range(int(start), int(end) + 1):
    print '\ndownloading', page, 'page...'
    detailURL = 'http://jandan.net/ooxx/page-'+str(page)
    try:
        threading.Thread(target=spider.saveDetailPage, args=(detailURL, page)).start()
    except TypeError:
        print('数据异常,爬取失败')
    end_time = time.time()
    print('总共耗时%.2fs' % (end_time-start_time))
    print 'sucessful'