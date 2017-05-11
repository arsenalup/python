# coding: utf-8
import requests
import json
import re
from bs4 import BeautifulSoup
header={'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }
content=requests.get('http://rj.baidu.com/soft/ranking/1',headers=header).content.decode('utf-8')
soup=BeautifulSoup(content,'html.parser')
# print soup
conts=soup.find_all("script",type="text/javascript")
# print conts
# list = re.findall(r'(?<="url":")http\S+(?=")', conts)
# print list
a=''
for cont in conts:
     a=cont.get_text()

     # print a
     list = re.findall(r'(?<="url":")http\S+exe(?=")', a)
     print list
     for l in list:
         if l:
             l=l.replace('\\','')
             print l
             software_name = l.split('/')[-1]
             print '正在下载', software_name
             response = requests.get(l, headers=header)
             software = response.content
             with open(software_name, 'wb') as f:
                 f.write(software)
                 print '文件', software, '已下载'