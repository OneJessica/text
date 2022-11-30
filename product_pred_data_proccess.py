import json
import pandas as pd
import numpy as np
import os
from glob import glob
from tqdm import tqdm



filepath = r'/home/zhangjin/products_cat/一级分类'
 
input_rule = 'three'

input_dirfile = [filepath+"/"+i for i in os.listdir(filepath) if i.startswith(input_rule)]

input_file_name = [i.split('/')[-1] for i in glob(f'{input_dirfile[0]}/*')]



def get_categories(bs:str,name:str):
    '''
    fuction:
    读取文件夹下的文件并将之转化为dataFrame对象，再将预测结果处理成可读模式
    arg:
        bs:file_path
        name:file_name
        
    return:
        categories:pd.dataframe
    '''
    with open(f'{bs}/{name}') as f:
            data = json.load(f) 

    # 读取的json字典转化为pandas的dataframe对象
    k = pd.DataFrame.from_dict(data).T

    # 将dataframe中预测结果为1的列添加其文件夹名的最后一个词
    k.loc[k[k['predicted'] == 1].index,'pred_categories'] = bs.split('_')[-1]

    # 将np.nan转换为None
    k = k.where((pd.notnull(k)), None)
 
    
    return k[['id','pred_categories']]


def get_unique(text):
    if text:
        if isinstance(text,str):
            return text.split(',')
        elif isinstance(text,list):
            return text
    else:
        return []

def combine_categories(k:str,v:str):
    '''
    fuction：
    将读取的多个文件夹下的相同预测文件合并
    arg:
    k:文件1
    v:文件2  
    '''
    combine = k[['id','pred_categories']].join(v[['id','pred_categories']],lsuffix='_x', rsuffix='_y', sort=False)
    if (combine['id_x'] == combine['id_y']).all:
        

        combine['pred'] = [get_unique(a)+get_unique(b) if a!=b \
                            else a for a,b in zip(combine['pred_categories_x'].to_list(),combine['pred_categories_y'].to_list()) ]
        combine = combine.rename({'id_x':'id','pred':'pred_categories'},axis =1)
        # print(combine.head())
    return combine[['id','pred_categories']]


def remove_duplicated(text:list):
    if text:
        return list(set(text))
    return []

fist_con['pred'] = fist_con.pred_categories.map(remove_duplicated)

result_dict = fist_con[['id','pred']].T.to_dict()
result_list = []
for k,v in result_dict.items():
    result_list.append(v)

with open(outfile,'w') as f:
    json.dump(result_list,f,indent = 4, ensure_ascii=False)
    