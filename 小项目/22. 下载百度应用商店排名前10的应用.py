# coding: utf-8
import requests
import json
import re
from bs4 import BeautifulSoup
header={'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }
def fetchData():
    response=requests.get('http://rj.baidu.com/soft/ranking/1',headers=header)
    content=response.text
    # print content
    str_content=content.encode('utf-8')
    # print str_content
    start_index=str_content.find('var configs =  ')+len('var configs =  ')
    end_index=str_content.find(('var loginUrl'))
    content=str_content[start_index:end_index].strip()
    content=content[:-1]
    content=json.loads(content)
    info=content.get('data').get('softList').get('list')
    software_urls=[]
    for i in info:
        url=i.get('url')
        software_urls.append(url)
    print software_urls
    return software_urls
def download(urls):
    for url in urls[:-2]:
        software_name=url.split('/')[-1]
        print '正在下载',software_name
        response=requests.get(url,headers=header)
        software=response.content
        with open(software_name,'wb')as f:
            f.write(software)
            print '文件',software

def main():
    print '开始下载'
    urls=fetchData()
    download(urls)
    print '完成'
if __name__ == '__main__':
    main()