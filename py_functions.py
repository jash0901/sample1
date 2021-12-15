import pandas as pd

def fetch_data(cnxn):
    query='SELECT * FROM EMPLOYEE'
    print(query)
    df=pd.read_sql(query,cnxn)
    return df