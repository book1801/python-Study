# -*- coding:utf-8 -*-

from spiderSearch import SpiderSearch

class MakeTestDoc(object):
    keywords=[]

    #初始化
    def __init__(self):
        self.readKeywords()

    #读取关键字
    def readKeywords(self):
        for word in open("keyword.txt",mode="r",encoding="utf-8"):
            self.keywords.append(word+" app 赚钱")

    #开始进行关键词搜索
    def getSearchAboutKeyword(self):
        aboutKeywordList=[]
        for word in self.keywords:
            keywordlist=[]
            aboutKeyword=set()
            s=SpiderSearch(word)
            baidusearch=s.spiderBaidu()
            haososearch=s.spiderHaoso()
            sogousearch=s.spiderSogou()
            for x in baidusearch: aboutKeyword.add(x)
            for x in haososearch: aboutKeyword.add(x)
            for x in sogousearch: aboutKeyword.add(x)
            for w in aboutKeyword:
                keywordlist.append(w)
            aboutKeywordList.append(keywordlist)
        
        #将相关关键词写入文件
        f=open("aboutKeywordList.txt",mode="w",encoding="utf-8")
        for l in aboutKeywordList:
            tmpstr=','.join(l)+"\n"
            f.writelines(tmpstr)
        f.close()   

    #生成问答
    def makeDoc(self):
        i=0
        for keyline in open("aboutKeywordList.txt",mode="r",encoding="utf-8"):
            if i < 5:
                docfilename="doc"+str(i+1)+".txt"
                testfilename="test"+str(i+1)+".txt"
                f=open(docfilename,mode="r",encoding="utf-8")
                content=f.read()
                content=content + keyline
                
                ft=open(testfilename,mode="w",encoding="utf-8")
                ft.write(content)
                ft.close()
                f.close()
                i=i + 1

    #流程
    def run(self):
        aboutKeywordList=self.getSearchAboutKeyword()
        self.makeDoc()
        print("程序全部完成！")

mt=MakeTestDoc()
mt.run()