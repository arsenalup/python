# -*- coding: utf-8 -*-
import re
import requests
import os
from bs4 import BeautifulSoup
import time

class Spider():
    def __init__(self):
        self.keyword=raw_input(u'请输入图片：')
        self.siteURL=r'https://pixabay.com/zh/photos/?q='+ str(self.keyword)+ r'&image_type=&cat=&min_width=&min_height='
    def getSource(self,url):
        result=requests.get(url).content.decode('utf-8')
        return result
    def getPageNum(self):
        result=self.getSource(self.siteURL)
        soup = BeautifulSoup(result, 'html.parser')
        content1 = soup.find_all("input", attrs={"name": "pagi"})
        for a in content1:
            b = a.get_text()
            b = re.sub(r'.+/ ', '', b)
            b = b.strip(' ')
            if b:
                print u'这个主题有',b, u'页'
            else:
                print u'没有内容'
            return b
    def getItem1(self,url):
        result=self.getSource(url)
        soup = BeautifulSoup(result, 'html.parser')
        items = soup.find_all("img", alt=re.compile(r'.+'))
        return items
    # def getItem2(self,url):
    #     result=self.getSource(url)
    #     soup = BeautifulSoup(respond, 'html.parser')
    #     items = soup.find_all("img", alt=re.compile(r'.+'))
    def saveImage(self,detailURL,name):
        try:
            picture=requests.get(detailURL)
            fileName=name+'.jpg'
            string='F:\pixabay\%s\%s'%(self.path,fileName)
            E=os.path.exists(string)
            if not E:
                f=open(string,'wb')
                f.write(picture.content)
                f.close()
            else:
                print u'图片已经存在，跳过！'
                return  False
        except (urllib2.HTTPError,urllib2.URLError), e:
            print e.reason
            return None

    def makeDir(self, path):
        self.path = path.strip()
        E = os.path.exists(os.path.join('F:\pixabay', self.path))
        if not E:
            # 创建新目录,若想将内容保存至别的路径（非系统默认），需要更环境变量
            # 更改环境变量用os.chdir()
            os.makedirs(os.path.join('F:\pixabay', self.path))
            os.chdir(os.path.join('F:\pixabay', self.path))
            print u'成功创建名为', self.path, u'的文件夹'
            return self.path
        else:
            print u'名为', self.path, u'的文件夹已经存在...'
            return False
    def saveOnePage(self,url):
        i=1
        items=self.getItem1(url)
        if i<=16:
            for item in items:
                detailURL = re.findall(r'(http.*)__340.jpg', item['src'])
                detailURL = "".join(detailURL) + '_960_720.jpg'
                print  u'\n', u'正在下载并保存图片', i, detailURL
                self.saveImage(detailURL, name='Num'+str(i))
                time.sleep(0.5)
                i += 1
        if i>16:
            for item in items:
                detailURL = re.findall(r'(http.*)__340.jpg', item['data-lazy'])
                detailURL = "".join(detailURL) + '_960_720.jpg'
                print  u'\n', u'正在下载并保存图片', i, detailURL
                self.saveImage(detailURL, name='Num'+str(i))
                time.sleep(0.5)
                i += 1
    def saveMorePage(self):
        numbers=self.getPageNum()
        Num = int(raw_input(u'一页共100张图，\n请输入要下载的页数(默认页数大于等于1）：'))
        Start = int(raw_input(u'请输入下载起始页数：'))
        if numbers >= 1:
            for page in range(Start, Start + Num):
                if page == 1:
                    print u'\n', u'正在获取第1页的内容......'
                    self.url1 = self.siteURL
                    self.makeDir(path=self.keyword + 'page' + str(page))
                    self.saveOnePage(url=self.url1)
                else:
                    print u'\n', u'正在获取第', page, u'页的内容'
                    # self.url2 = 'https://pixabay.com/zh/photos/?orientation=&image_type=&cat=&colors=&q=' + str(self.keyword) + '&order=popular&pagi=' + str(page)
                    self.url2 ='https://pixabay.com/zh/photos/?q='+ str(self.keyword) +'&image_type=&min_width=&min_height=&cat=&pagi=' + str(page)
                    self.makeDir(path=self.keyword + 'page' + str(page))
                    self.saveOnePage(url=self.url2)

        else:
            return False

        print  u'\n',u'圆满成功!!!'

spider=Spider()
spider.saveMorePage()







