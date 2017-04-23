# -*- coding: utf-8 -*-
with open("data.txt") as f:
    list_n = []
    for l in f.readlines():
        sum = 0
        data=l.split()
        for i in data[1:]:
            sum +=int(i)
        avg="%.2f"%(sum/9.0)
        data.append(sum)
        data.append(avg)#将计算值加入每一行中
        list_n.append(data)#得到一个汇总
    list_n.sort(key=lambda x: x[11], reverse=True)#排序
level=1
for x in list_n:
    x.insert(0,level)#插入排名
    level+=1
list2=['  0','平均']
for i in range(2,13):
    sum1=0
    for j in list_n:
        sum1+=float(j[i])
        avg2='%.1f'%(sum1/30)
        if float(j[i])<60:
            j[i]='不及格'
    list2.append(avg2)
data1=open('data1.txt','w')
first_line=['名次' ,'名字','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分\n']
data1.write('  '.join(first_line)+'\n')#写入标题
data1.write('  '.join(list2)+'\n')
for i in list_n:
    for j in i:
        data1.write(str(j).center(6,' '))#写入数据
    data1.write('\n')
data1.close()#关闭







