import pymongo
import pandas as pd
class mongo():
    @classmethod
    def connect(cls,
        host,
        port,
        database = None
    ):
        assert type(host)==int,("host 必须是整数，例如：88")
        assert type(port)==int,("port 必须是整数，例如：27017")
        assert host in [33,55,77,88,99,],("host 必须在33,55,77,88,99之中")
        
        host = '192.168.1.'+ str(host)
        connect_str = f'mongodb://{host}:{port}'
        myclient = pymongo.MongoClient(connect_str)
        if database:
            return myclient[database]
        else:
            print('目前含有数据库:', myclient.list_database_names())
            return myclient
    @classmethod
    def select(cls,
        table,
        query = '*',
        to_frame = True,
    ):
        '''
        默认查全部数据*，
        args:
        query:dict
        table:Collection(Database(MongoClient...
        to_frame:bool[default:DataFrame()]
        returns:
        
        '''
        res = []
        if query == '*':
            res = list(table.find())
        else:
            for i in table.find(query):
                res.append(i)
                
        if to_frame:
            return pd.DataFrame(res)
        return res
    
