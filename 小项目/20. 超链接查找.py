# -*- coding:utf-8 -*-im
import requests
import json
from bs4 import BeautifulSoup
import re
content=requests.get('http://www.sjtu.edu.cn/').content.decode('utf-8')
# print content
soup=BeautifulSoup(content,'html.parser')
conts=soup.find_all('a',href=re.compile(r'http'))
print type(conts)
for cont in conts:
    print cont['href'],cont.get_text()
