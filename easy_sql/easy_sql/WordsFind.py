import pandas as pd
import re
import json
class WordsFind:
    '''
    从列表、字典查找想要的词，或者从先有的数据中提取含有某些关键词的部分数据
    
    '''
    def __init__(self,sign = ' '):
        self.sign = sign
        self.not_std_name = set()
        
    def from_list(self,text,source,sign = ','):
        '''
        function:从json或csv文件中获得原始文件，判断拆分后的text内容是否在源数据中

        ---
        args:
            text:str
            source:list or 
        '''
        if not text:
            return None
        text_list =text.lower().split(sign)

        if isinstance(source,str):
            if source.endswith('json'):
                source_list = pd.read_json(source)
                source_list = source_list[source_list.columns[0]].to_list()
            if source.endswith('csv'):
                source_list = pd.read_csv(source)
                source_list = source_list[source_list.columns[0]].to_list()
        elif isinstance(source,list):
            source_list = source
        else:
            assert type(source) == list, 'source应该为列表或者含列表的文件'
            
        for source in source_list:
            if source.lower() in text_list:
                return source
    def to_dict(self,filename):
        source_dict = {}

        if filename.endswith('json'):
            with open(filename) as f:
                for k,v in  json.loads(f.read()).items():
                    for term in v:
                        source_dict[term.lower()] = k
        elif filename.endswith('csv'):
            source_dict = pd.read_csv('../../标准表/species.csv',index_col = 0)
            source_dict.term = source_dict.term.str.lower()
            source_dict = source_dict.set_index('term')['species'].to_dict()

        else:
            assert type(source) == str,('仅接受json或csv文件名')
        return source_dict


    def from_dict(self,text):
        if isinstance(source,str):
            source_dict = self.get_dict(source)
        elif isinstance(source,dict):
            source_dict = source
        else:
            assert '仅接受字典'
        if not text:
            return
        # 默认"N/A"为空值
        if text == "N/A":
            return

        result = []
        texts = re.split(r',|, ',text)

        for text in texts:
            text = text.strip(r'[,.;，。；：: ]') 

            result.append(source_dict.get(text.lower(),text))

        return json.dumps(result)
    
    def check_text(self,feature):
        if not isinstance(feature,str):
            return
        return feature
    
    def check_words(self):
        self.check_dict = {}
        for word in self.keywords:
            self.check_dict[word]=len(word.split(' '))
        return self.check_dict
    
    def lemma(self,text):
        if not text:
            return None
        if text.endswith('ies'):
            return text[:-3]+'y'
        elif text.endswith('xes') or text.endswith('ses'):
            return text[:-2]
        elif text.endswith('s'):
            return text[:-1]
        elif text.endswith('ing'):
            return text[:-3]
        elif text.endswith('ed'):
            return text[:-2]
        return text
    def criticize_text(self,text):
        fragments = re.findall(r'(.*?)(\(.*\))(.*?)',text)
        
    
    def split_text(self,text):
        if not text:
            return None
        
        features = text.split(self.sign)
        features = [f.lower().strip(r'[,.;，；：:?？\(\)]') for f in features]
        return features
    
    def get_neighbor(self, lists:list, num:int):
        '''
        functions:获得相邻元素，用空格分隔
        ---
        args:
            lists:list
            num:int
        returns:
            neighbor:list
        ---
        
        
        '''
        if not lists:
            return None
        neighbor = []
        for idx, _ in enumerate(lists):
            if idx < len(lists) - num + 1:
                neighbor.append(' '.join(lists[idx:idx+num]))
        return neighbor
    
    def get_element(self,text:str):
        '''
        functions:获得关键长度敏感性检查文本
        ---
        args:
            text:str
        returns:
            resutls:dict
        
        
        '''
        if not text:
            return None
        self.results = dict()

        text_list = self.split_text(text)
        for keyword,num in self.check_words().items():
            self.results[keyword]= self.get_neighbor(text_list, num)
        return self.results
    

    def find_words(self,feature:str,keywords:list,join = True, is_tight = True):
        '''
        function:从json数组从获得含有某些关键词的集合
        ---
        args：features：str
              keywords:list 关键词列表，只要含有关键词列表中一个就返回该字段，大小写不敏感，含有单词边界
              sign：str default = ','
        returns：text:str(用sign合并关键词列表)

        '''
        if not feature:
            return
        try:
            feature = json.loads(feature)
        except:
            feature = self.check_text(feature)
        finally:
            self.keywords = keywords
            # self.feature = feature
            if not feature:
                return 

            result = set()
            features = feature
            

            if is_tight:
                if not isinstance(feature,list):
                    if isinstance(feature,int) or isinstance(feature,float):
                        self.not_std_name.add(feature)
                        return None
                    else:
                        features = self.split_text(feature)
                if not features:
                    return None
                

                for feature in features:
                    self.results = self.get_element(feature)
                    if not self.results:
                        
                        return None
                    
                    for word in keywords:
                        if not word:
                            return None
                        if word.lower() in self.results[word]:
                            result.add(feature)

            else:
                for word in keywords:
                    if word.lower() in feature.lower():
                        result.add(feature)

            if not result:
                return
            keytext = list(result)[::1]
            if join:
                return self.sign.join(keytext)

            else:
                return keytext
            
    def __notstd__(self):
        return self.not_std_name
            
        
    def find_affix(self,feature:str,affix:list,method = 'pre'):
        
        '''
        functions:返回含有某种词缀文本
        ---
        args:
            feature:str 文本
            affix:list 词缀列表
            method:str ['pre','suf','both'],默认前缀
        returns:
            
        
        '''
        if not feature:
            return None
        features = self.split_text(feature)

        for fea in features:
            if not fea:
                return None
            if method == 'pre':
                for af in affix:
                    if fea.lower().startswith(af.lower()):
                        return feature
                        
            elif method == 'suf':
                for af in affix:
                    if fea.lower().endswith(af.lower()):
                        return feature
            elif method == 'both':
                for af in affix:
                    if fea.lower().endswith(af.lower()) or fea.lower().startswith(af.lower()):
                        return feature
            
            else:
                raise ValueError('method is wrong, accepted pre and suf.')
