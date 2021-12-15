import uvicorn
from fastapi import FastAPI
import py_functions
import config
import pyodbc
import json

app=FastAPI()

def connect_db():
    driver=config.DRIVER
    server=config.SERVER
    database=config.DATABASE
    uid=config.UID
   
    trust=config.TRUST
    con_string=f'DRIVER={driver};SERVER={server};DATABASE={database};UID={uid}'
    cnxn=pyodbc.connect(con_string)
    cnxn.autocommit=True
    cursor=cnxn.cursor()
    print('Connection successful with database')
    return cnxn

@app.get('/')
def get_data():
    df=py_functions.fetch_data(cnxn)
    return df.to_dict('r')

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)