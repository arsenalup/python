# coding: utf-8
import os
def getDirInfo(path):
    result=[]
    items=0
    for root,dirs,files in os.walk(path):
        # print root
        # print dirs
        # print files
        for file in files:
            size=os.path.getsize(root+os.sep+file)
            result.append([root+os.sep+file,size])
            items+=1
    result=sorted(result,key=lambda i:i[1],reverse=True)
    for i in result:
        print '文件',i[0].decode('gbk'),'占用',i[1],'字节'
    print 'wenjainjia',path.decode('gbk'),'gonfyou',items
def main():
    print '输入文件路径'
    path=raw_input()
    if os.path.exists(path):
        getDirInfo(path)
    else:
        print u'路径有无'
if __name__ == '__main__':
    main()