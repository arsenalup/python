# coding=utf-8
import sys, os
import time
import requests
import json
header={'User-Agent':
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
          'apikey':'2fd858445546756a2cea84b14c7'
        }
def getInfo(stockname):
    response=''
    try:
        response=requests.get('http://apis.baidu.com/apistore/stockservice/stock?stockid='+stockname,headers=header)
    except:
        print u'请求失败'
    content=response.text
    content=json.loads(content)
    info=content.get('reDate')
    currentprice=''
    if info:
        currentprice=info.get('stockinfo').get('surrentprice')
    else:
        print u'查询失败'
        exit()
    return currentprice
def main():
    print u'输入要查询的股票代码：'
    stock=raw_input('...')
    i=0
    while i<5:
        currrentp=getInfo(stock)
        sys.stdout.write('\r'+str(currrentp))
        sys.stdout.flush()
        time.sleep(10)
        i+=1
    print ('\n程序结束')
if __name__=="__main__":
    main()

