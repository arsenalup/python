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
    #print list_n
level=1
for x in list_n:
    x.insert(0,level)#插入排名
    level+=1
    for e in x[2:-2]:
        if int(e)<60:
            x[x.index(e)]='不及格'#替换不及格
data1=open('data1.txt','w')
print list_n
first_line=['名次' ,'名字','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分\n']
data1.write('  '.join(first_line)+'\n')#写入标题
for i in list_n:
    # data1.write('   '.join(str(i))+'\n')
    for j in i:
        data1.write(str(j).center(6,' '))#写入数据
    data1.write('\n')
data1.close()#关闭







