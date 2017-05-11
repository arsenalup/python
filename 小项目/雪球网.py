# -*- coding: utf-8 -*-
import re
import urllib2
import json
# import chardet
url='https://xueqiu.com/P/ZH438953'
headers={
        "Accept":'*/*',
        "Connection":"keep-alive",
        "Cookie":"aliyungf_tc=AQAAAIPnaXLDuQ4AG1bjdG4EnjZ1pnJ9; xq_a_token=afe4be3cb5bef00f249343e7c6ad8ac7dc0e17fb; xq_a_token.sig=6QeqeLxu5hi1S21JgtozJ1EZcsQ; xq_r_token=a1e0ac0c42513dcf339ddf01778b49054e341172; xq_r_token.sig=VPMAft0BfpDHm5UE0QJ5oDLYunw; u=801494498651742; s=em11y801ae; __utmt=1; __utma=1.657091123.1494500481.1494500481.1494500481.1; __utmb=1.3.10.1494500481; __utmc=1; __utmz=1.1494500481.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1494498652; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1494501119",
        "Host":"xueqiu.com",
        "Referer":"https://xueqiu.com/k?type=cube&q=ZH438953",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}
reqe=urllib2.Request(url,headers=headers)
req=urllib2.urlopen(reqe).read()
# print req
post_start=req.find('SNB.cubeInfo = ')+len('SNB.cubeInfo = ')
post_end=req.find(r'SNB.cubePieData')
# print post_end,post_start
data=req[post_start:post_end-2]
# print data
data_jason=json.loads(data)
print data_jason["name"]