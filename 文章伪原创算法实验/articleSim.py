#-*- conding:utf-8 -*-
#文章伪原创算法
from jieba import posseg
from gensim import corpora,models,similarities

class ArticleSim():
    '''
    param:
    doclist:list  file name list
    testfilelist:list test file name list
    '''
    def __init__(self,doclist,testfilelist):
        self.doclist=doclist
        self.testfilelist=testfilelist
        
    #读取列表文件
    def readListFile(self,encoding="utf-8"):
        doc_list=[]
        for file in self.doclist:
            f=open(file,mode="r",encoding=encoding)
            content=f.read()
            doc_list.append(content)
            f.close()
            
    #对文档进行分词，并删除停止词 
    def cutWordUseStopWrod(self,docs_content_list,myStopWordList,myStopWordFlagList):
        stopWordList=[]
        #生成停止词列表
        stopFileList=["百度停用词列表.txt","哈工大停用词表.txt","四川大学机器智能实验室停用词库.txt","中文停用词库.txt","自己的停止词词库.txt"]
        for file in stopFileList:
            for line in open(file,mode="r",encoding="utf-8"):
                stopWordList.add(line.replace(" "))
            
        for w in myStopWordList:
            stopWordList.add(w)
        
        all_docs_words=[]
        for content in docs_content_list:
            pwords=posseg.cut(content)
            pwords=[word for word in pwords if word.word not in stopWordList]
            pwords=[word.word for word in pwords if word.flag not in myStopWordFlagList]
            all_docs_words.add(pwords)
        
        return all_docs_words
    
    #计算文档的相似度
    def sim(self,all_docs_words,test_doc_words):
        # 首先用dictionary方法获取词袋（bag-of-words)
        dictionary=corpora.Dictionary(all_docs_words)
        
        #词袋中用数字对所有词进行了编号
        dictionary.keys()
        
        #编号与词之间的对应关系
        dictionary.token2id
        
        #使用doc2bow制作语料库
        corpus = [dictionary.doc2bow(doc_words) for doc_words in all_docs_words]
        
        #对测试文档分词转换为二元向量
        doc_test_vec = dictionary.doc2bow(test_doc_words)
        
        #使用TF-IDF模型对语料库建模
        tfidf = models.TfidfModel(corpus)
        
        #获取测试文档中，每个词的TF-IDF值
        print(tfidf[doc_test_vec])
        
        #对每个目标文档，分析测试文档的相似度
        index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
        sim = index[tfidf[doc_test_vec]]
        
        #根据相似度排序
        result=sorted(enumerate(sim), key=lambda item: -item[1])
        
        return result