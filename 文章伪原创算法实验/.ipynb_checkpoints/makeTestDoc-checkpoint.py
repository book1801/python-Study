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
            return aboutKeywordList

    #生成问答
    def makeDoc(self,aboutKeywordList):
        i=0
        for wl in aboutKeywordList:
            keywordcontent=""
            for word in wl[0]:
                keywordcontent=keywordcontent+","+word 
            docfilename="doc"+str(i)+".txt"
            testfilename="test"+str(i)+".txt"
            f=open(docfilename,mode="r",encoding="utf-8")
            content=f.read()
            f.close()

            ft=open(testfilename,mode="w",encoding="utf-8")
            content=content + keywordcontent
            ft.write(content)
            ft.close()

            i=i + 1

    #流程
    def run(self):
        aboutKeywordList=self.getSearchAboutKeyword()
        self.makeDoc(aboutKeywordList)
        print("程序全部完成！")