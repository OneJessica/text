import time
from .connect import connect
import pandas as pd

class Todb():
    '''
    自动在某个数据库下建表，并插入数据
    
    '''
    
    def __init__(self,table_name,df,conn = False):
        if not conn:
            self.conn = connect(77,3306,'ProductIncrement')
            self.cursor = self.conn.cursor()
        else:
            self.conn = conn
            self.cursor = self.conn.cursor() 
        
        self.table_name = table_name
        self.df =df
        self.columns = df.columns
        self.start_sql = '`aid` int(10) NOT NULL AUTO_INCREMENT,'
        self.end_sql ='''  
                      `create_on` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
                      `create_by` varchar(255) DEFAULT NULL,
                      `update_on` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                      `update_by` varchar(255) DEFAULT NULL,
                      `remark` varchar(1024) DEFAULT NULL,
                      PRIMARY KEY (`aid`) USING BTREE

                    ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
                  '''
        self.df_sql = f'''
        Create Table IF NOT EXISTS `{table_name}`
            ({self.start_sql}{','.join([
            '`'+ col +'`'+' text DEFAULT NULL' 
                    if col not in ['_id','id',] 
                    else '`'+ col +'`'+' bigint NOT NULL' 
                for col in self.columns
            ])},
        '''
        
    def create_table(self):
        sql = self.df_sql + self.end_sql
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e,sql,sep = '\n\n')
        finally:
            print('successfully created!')
            self.conn.commit()
    def row2db(self,row):
        column_str = ','.join(['`'+col+'`' for col in self.columns])
        values_str = ','.join(['%s'for i in range(len(self.columns))])
        values = list(row[self.columns])
        values = [i if pd.notna(i) else None for i in values ]
        sql = f"insert into `{self.table_name}`({column_str},create_by,update_by) values ({values_str},CURRENT_USER(),CURRENT_USER()) ",values
        try:
            self.cursor.execute(*sql)
        except Exception as e:
            print(e,sql,sep = '\n\n')
            assert 1==2
        finally:
            self.conn.commit()
            
    def to_mysql(self):
        start_time = time.time()
        for _,row in self.df.iterrows():
            self.row2db(row)
        print('time:',time.time() - start_time,'s')
    
    def easy_run(self):
        self.create_table()
        self.to_mysql()    