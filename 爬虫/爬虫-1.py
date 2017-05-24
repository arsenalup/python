#-*- coding:utf-8 -*-
import requests
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

conts=''
url='https://www.qiushibaike.com/'
number=raw_input('get number：')
for i in range(1,int(number)+1):
    req = requests.get(url)
    html = req.content.decode('utf-8')
    tree = etree.HTML(html)
    content = tree.xpath('//div[@class="article block untagged mb15"]')
    for a in content:
        i+=1
        author=a.xpath('.//h2/text()')[0]
        conts +=('author:%s'%author+':\n')
        cont=a.xpath('.//div[@class="content"]/span/text()')[0]
        conts+=('content：%s\n'%cont)
        funny_count = a.xpath('.//span[@class="stats-vote"]/i/text()')[0]
        conts+=('laught：%s\n'%funny_count)
        repost_count = a.xpath('.//span[@class="stats-comments"]/a/i/text()')
        if repost_count=='':
            repost_count=0
        else:
            repost_count=repost_count[0]
        conts+=('bang：%s'% repost_count)
        conts+='\n=======\n\n'
    url='https://www.qiushibaike.com/8hr/page/%d/?s=4985449'%(i)

with open('qiushi.txt','w') as f:
    f.write(conts)


