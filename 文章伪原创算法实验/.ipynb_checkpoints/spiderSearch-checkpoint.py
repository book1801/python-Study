#-*-:coding:utf-8-*-
#抓取各搜索引擎的相关关键词

import requests
from urllib import parse
from lxml import etree

class SpiderSearch(object):
    
    def __init__(self,keywords):
        if type(keywords)=="list":
            self.keywords=keywords
        else:
            self.keywords=[keywords]
    
    #抓取百度相关关键词
    def spiderBaidu(self):
        about_keyword_list=[]
        header={}
        header["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        for k in self.keywords:
            wd=parse.quote(k)
            url="https://www.baidu.com/s?ie=utf-8&wd="+wd
            r=requests.get(url,headers=header)
            code=r.text
            if code.find("<!--STATUS OK-->") > 12:
                e=etree.HTML(code)
                a=e.xpath("//div[@id='rs']/table/tr/th/a/text()")
                for word in a:
                    about_keyword_list.append(word)
        return about_keyword_list
    
    #抓取好搜相关关键词
    def spiderHaoso(self):
        about_keyword_list=[]
        header={}
        header["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        for k in self.keywords:
            wd=parse.quote(k)
            url="https://www.so.com/s?ie=utf-8&fr=none&src=home-sug-store&q="+wd
            r=requests.get(url,headers=header)
            code=r.text
            e=etree.HTML(code)
            a=e.xpath("//div[@id='rs']/table/tr/th/a/text()")
            for word in a:
                about_keyword_list.append(word)
        return about_keyword_list
    
    #抓取sogou相关关键词
    def spiderSogou(self):
        about_keyword_list=[]
        header={}
        header["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        for k in self.keywords:
            wd=parse.quote(k)
            url="https://www.sogou.com/web?query="+wd
            r=requests.get(url,headers=header)
            code=r.text
            e=etree.HTML(code)
            a=e.xpath("//div[@class='hintBox']/table/tr/td/p/a/text()")
            for word in a:
                about_keyword_list.append(word)
        return about_keyword_list