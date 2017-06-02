from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import os
import urllib
import threading


def get_urls(url):
    all_rooms=[]
    driver=webdriver.PhantomJS(service_args=['--load-images=no'])
    driver.set_window_size(1920,2000)
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_partial_link_text('闵行').click()
    time.sleep(1)
    for i in range(1):
        soup=BeautifulSoup(driver.page_source,'lxml')
        items=soup.find_all(class_='info rel')
        for item in items:
            all_rooms.append(('http://zu.sh.fang.com/'+item.find('a').get('href')))
        driver.find_element_by_partial_link_text('下一页').click()
        time.sleep(1)
    return all_rooms


def detail_pics(j):
        driver = webdriver.PhantomJS(service_args=['--load-images=no'])
        driver.set_window_size(1920, 2000)
        print(j)
        driver.get(j)
        items=driver.page_source
        soup = BeautifulSoup(items, 'lxml')
        projname=re.findall("projname: '([\s|\S]*?)',",items)[0]
        address=re.findall("address: '([\s|\S]*?)',",items)[0]
        price = re.findall("price: '([\s|\S]*?)',", items)[0]
        pic_list=soup.find_all(width="100") or soup.find_all(width="509")
        dir_name='pic/闵行-'+address+projname
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        a = 1
        for i in pic_list:
            file_name=(dir_name+'/'+'price'+price+'-%s.jpg')%a
            i=i.get('src')
            urllib.request.urlretrieve(i,file_name)
            a+=1

def main():
    url = 'http://zu.sh.fang.com/'
    all_rooms=get_urls(url)
    for j in all_rooms:
        threading.Thread(target=detail_pics, args=(j,)).start()
        while threading.active_count() > 3:
            time.sleep(3)
            print(threading.active_count())

if __name__ == '__main__':
    main()














