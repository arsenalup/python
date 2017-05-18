# -*- coding: utf-8 -*-
import re
import requests
import time
from bs4 import BeautifulSoup


class Spider(object):
    def __init__(self):
        self.siteURL = 'http://jandan.net/ooxx/page-'

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

    def getAllPage(self, start, end):
            number = int(start)
            for page in range(int(start), int(end) + 1):
                print '\ndownloading', number, 'page...'
                detailURL = self.siteURL +str(page)
                self.saveDetailPage(detailURL, number)
                time.sleep(2)
                number += 1
            if number == int(end) + 1:
                print 'sucessful'
                return False

spider = Spider()
spider.getAllPage(start=raw_input('input start:'), end=raw_input('input end page:'))
e=input('end')