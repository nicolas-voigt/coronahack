import pandas as pd 
import numpy as np 

import json

import sqlalchemy
from progress.bar import Bar
import datetime

#We are using bottle for the api
from bottle import request, response
from bottle import post, get, put, delete
import config

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + config.username + ':'+ config.password + '@' + config.server+ '/' + config.database

# # Test if it works
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
# print(engine.table_names())

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

    # https://en.wikipedia.org/wiki/Rule_of_succession
    user_rating = (data['user_rating'] + 1 ) / (data['total_ratings'] + 2)
    score = 1 # some smart formula
    return score

def upload(data, table):
    data.to_sql('table', con=engine, if_exists='append', method='multi')

@post('/rate') #https://stackoverflow.com/questions/34661318/replace-rows-in-mysql-database-table-with-pandas-dataframe
def rate_data():
    try:
        # parse input data
        try:
            data = request.json()
            data = {
                'news_id': 1234,
                'rating': 1
            }
        except:
            raise ValueError
        try:
            news_data = pd.read_sql(sql='SELECT * FROM news WHERE id = {0}'.format(data['news_id']), con=engine).at[0, :]
        except:
            raise ValueError
    except ValueError:
        response.status = 400
        return

    news_data['total_ratings'] += 1
    news_data['user_rating'] += data['rating']
    # replace row in database (delete and the reinsert)
    delete_str = 'DELETE FROM db_name WHERE id == {0}'.format(data['news_id'])
    cursor = engine.cursor()
    cursor.execute(delete_str)
    engine.commit()
    news_data.to_sql('news', if_exists='append', con=engine)


@post('/get_data')
def creation_handler():
    try:
        # parse input data
        try:
            data = request.json()
            data = {
                'country':'germany',
                'state':'Bayern',
                'city':'köln'
            }
        except:
            raise ValueError
        # try:
        if data['country']:
            country_data = pd.read_sql(sql='SELECT * FROM news WHERE state_id IS NULL AND city_id IS NULL', con=engine)
        # except:
        #     raise ValueError
        
        # try:
        if data['state']:
            pd.read_sql(sql='SELECT * FROM state WHERE name="{0}"'.format(data['state']), con=engine).at[0,'id']
            state_data = pd.read_sql(sql='SELECT * FROM news WHERE state_id="{0}"'.format(state_id)  , con=engine)
        # except:
        #     raise ValueError

        # try:
        if data['city']:
            city_id = pd.read_sql(sql='SELECT * FROM city WHERE name="{0}"'.format(data['city']), con=engine).at[0, 'id']
            city_data = pd.read_sql(sql='SELECT * FROM news WHERE state_id="{0}"'.format(city_id), con=engine)
        # except:
        #     raise ValueError
        
    except ValueError:
        # if bad request data, return 400 Bad Request
        response.status = 400
        return
    
    # TODO: Add trust score

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({"country":country_data.to_json(), "state":state_data.to_json(), "city":city_data.to_json()})


if __name__ == '__main__':
    bottle.run(s, host = '127.0.0.1', port = 8000)