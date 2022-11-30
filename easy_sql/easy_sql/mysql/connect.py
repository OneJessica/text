
import pymysql
import pathlib
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read(pathlib.Path.home().joinpath('.my.cnf'))

def connect(
    host,
    port,
    database = None,

):
    """
    连接mysql数据库

    Args:
        host (int): 地址
        port (int): 端口
        database (str, optional): 数据库. Defaults to None.

    Returns:
        conn: 连接
    """    '''
    
    '''
    assert type(host)==int,("host 必须是整数,如：88")
    assert type(port)==int,("port 必须是整数,如：3306")
        
    conn = pymysql.connect(
        host = '192.168.1.'+str(host),
        port = port,
        user = CONFIG['client']['user'],
        passwd = CONFIG['client']['password'],
        database = database,
        

    )
    return conn