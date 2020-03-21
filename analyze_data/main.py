import pandas as pd 
import numpy as np 

import json

import sqlalchemy
from progress.bar import Bar
import datetime

#We are using bottle for the api
from bottle import request, response
from bottle import post, get, put, delete

server ='ketograph.de'
database = 'coronahack'
username = 'coronahack'
password =  'xapooyo6HeeS'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + username + ':'+ password + '@' + server+ '/' + database

# Test if it works
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
print(engine.table_names())


def get_source_score(source_url):
    super_trust_sources = []
    trust_sources = []
    newspaper_sources = []

    if source_url in super_trust_sources:
        return 1
    elif source_url in trust_sources:
        return 0.75
    elif source_url in newspaper_sources:
        return 0.25
    else:
        return 0

def bewerte(data):
    source_score = get_source_score(data['url'])
    score = 1 # some smart formula
    return score

def upload(data, table):
    data.to_sql('table', con=engine, if_exists='append', method='multi')

dummy_data = pd.DataFrame({'url':'', 'timestamp':'', })

unchecked_data = pd.read_sql(sql='SELECT * FROM dbname WHERE fact_checked == False'  , con=engine)

for i in range(len(unchecked_data)):
    unchecked_data.at[i, :] = bewerte(unchecked_data.at[i, :])

upload(unchecked_data, 'checked_data')

@post('/rate')
def rate_data():
    try:
        # parse input data
        try:
            data = request.json()
        except:
            raise ValueError

        if data is None or data.id is None or data.rating is None:
            raise ValueError
        
        try:
            data = pd.read_sql(sql='SELECT * FROM tablename WHERE fact_checked = true;'  , con=engine)
        except:
            raise ValueError
        

    except ValueError:
        # if bad request data, return 400 Bad Request
        response.status = 400
        return


    data

    response.headers['Content-Type'] = 'application/json'
    return data.to_json(orient='records')


@post('/get_data')
def creation_handler():
    try:
        # parse input data
        try:
            data = request.json()
        except:
            raise ValueError

        if data is None:
            raise ValueError

        try:
            data = pd.read_sql(sql='SELECT * FROM dbname WHERE fact_checked == True'  , con=engine)
        except:
            raise ValueError
        

    except ValueError:
        # if bad request data, return 400 Bad Request
        response.status = 400
        return

    response.headers['Content-Type'] = 'application/json'
    return data.to_json(orient='records')
if __name__ == '__main__':
    bottle.run(s, host = '127.0.0.1', port = 8000)