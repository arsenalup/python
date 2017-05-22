# -*- coding: utf-8 -*-
import re
# import chardet
result={}
with open('data.txt') as scores:
    lines=scores.readlines()
for line in lines:
    name=re.findall(r'[^\d]+',line)[0].strip()
    score =eval(re.findall(r'\d+', line)[0])
    if name in result:
        result[name][0]+=int(score)
        result[name][1]+=1
    else:
        result[name]=[score,1]
sort_result=sorted(result.items(),key=lambda x:x[1][0],reverse=True)
print sort_result
data=[]
for i in sort_result:
    avg=float(i[1][0]/i[1][1])
    print i[0][0]
    s='%s   %d   %d   %.1f\n'%(i[0][0],i[1][0],i[1][1],avg)
    data.append(s)
with open('result.txt','w') as f:
    f.writelines(data)


