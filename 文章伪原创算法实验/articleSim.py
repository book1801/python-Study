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
    doclist=[] #doc file name list
    testfilelist=[] #test file name list

    def setDoc(self,doclist):
        self.doclist=doclist

    def setTestDoc(self,testfilelist):
        self.testfilelist=testfilelist
        
    #读取列表文件
    def readListFile(self,mydoclist):
        my_docs_content_list=[]
        for file in mydoclist:
            f=open(file,mode="r",encoding="utf-8")
            content=f.read()
            my_docs_content_list.append(content)
            f.close()
        return my_docs_content_list

    #对文档进行分词，并删除停止词 
    def cutWordUseStopWrod(self,my_docs_content_list):
        stopWordList=set()
        #生成停止词列表
        stopFileList=["百度停用词列表.txt","哈工大停用词表.txt","四川大学机器智能实验室停用词库.txt","中文停用词库.txt","自己的停止词词库.txt"]
        for file in stopFileList:
            for line in open(file,mode="r",encoding="gbk"):
                stopWordList.add(line.replace(" ",""))
            
        myStopWordFlagList=[]
        for flag in open("词性过滤表.txt",mode="r",encoding="utf-8"):
            myStopWordFlagList.append(flag.replace(" ",""))
        
        all_docs_words=[]
        for content in my_docs_content_list:
            pwords=posseg.cut(content)
            pwords=[word for word in pwords if word.word not in stopWordList]
            pwords=[word.word for word in pwords if word.flag not in myStopWordFlagList]
            all_docs_words.append(pwords)
        
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
        #print(tfidf[doc_test_vec])
        
        #对每个目标文档，分析测试文档的相似度
        index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
        sim = index[tfidf[doc_test_vec]]
        
        #根据相似度排序
        result=sorted(enumerate(sim), key=lambda item: -item[1])
        
        return result
        

    #开始计算
    def run(self,doclist,testfilelist):
        self.setDoc(doclist)
        self.setTestDoc(testfilelist)    

        docs_content_list=self.readListFile(self.doclist)
        tests_content_list=self.readListFile(self.testfilelist)

        all_docs_words=self.cutWordUseStopWrod(docs_content_list)
      
        test_docs_words=self.cutWordUseStopWrod(tests_content_list)
        #import pdb
        #pdb.set_trace()
        r=self.sim(all_docs_words,test_docs_words[0])
        print("#" * 50)
        print("最后结果如下：")
        print(r)