from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import os
import urllib
import threading
all_rooms=[]
url='http://zu.sh.fang.com/house1/'
driver=webdriver.PhantomJS(service_args=['--load-images=no'])
driver.set_window_size(1920,2000)
driver.get(url)
time.sleep(1)
# driver.find_element_by_partial_link_text('地铁').click()
time.sleep(1)
# driver.get_screenshot_as_file('room2.jpg')
for i in range(2):
    soup=BeautifulSoup(driver.page_source,'lxml')
    items=soup.find_all(class_='info rel')
    for item in items:
        all_rooms.append(('http://zu.sh.fang.com/'+item.find('a').get('href')))
    driver.find_element_by_partial_link_text('下一页').click()
    time.sleep(1)

for j in all_rooms:
    a=1
    print(j)
    driver.get(j)
    items=driver.page_source
    soup = BeautifulSoup(items, 'lxml')
    # print(items)
    projname=re.findall("projname: '([\s|\S]*?)',",items)[0]
    address=re.findall("address: '([\s|\S]*?)',",items)[0]
    price = re.findall("price: '([\s|\S]*?)',", items)[0]
    pic_list=soup.find_all(width="100")
    dir_name='pic/'+address+projname
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    for i in pic_list:
        file_name=(dir_name+'/'+price+'-%s.jpg')%a
        i=i.get('src')
        urllib.request.urlretrieve(i,file_name)
        a+=1

driver.close()









