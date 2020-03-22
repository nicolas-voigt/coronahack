import pandas as pd 
import numpy as np 

import json

import sqlalchemy
import datetime

#We are using bottle for the api
from bottle import request, response, run
from bottle import post, get, put, delete
import config

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + config.username + ':'+ config.password + '@' + config.server+ '/' + config.database

# # Test if it works
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)
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
    data = {}
    try:
        # parse input data
        try:
            data = request.json
            # data = {
            #     'country':'germany',
            #     'state':'Bayern',
            #     'city':'Herne'
            # }
        except:
            raise ValueError
        # try:
        if data['country']:
            country_data = pd.read_sql(sql='SELECT * FROM news WHERE state_id IS NULL AND city_id IS NULL', con=engine)
        else:
            country_data = pd.DataFrame()
        # except:
        #     raise ValueError
        
        # try:
        if data['state']:
            state_id = pd.read_sql(sql='SELECT * FROM state WHERE name="{0}"'.format(data['state']), con=engine).at[0,'id']
            state_data = pd.read_sql(sql='SELECT * FROM news WHERE state_id="{0}"'.format(state_id)  , con=engine)
        else:
            state_data = pd.DataFrame()
        # except:
        #     raise ValueError

        # try:
        if data['city']:
            city_id = pd.read_sql(sql='SELECT * FROM city WHERE name="{0}"'.format(data['city']), con=engine).at[0, 'id']
            city_data = pd.read_sql(sql='SELECT * FROM news WHERE city_id="{0}"'.format(city_id), con=engine)
        else:
            city_data = pd.DataFrame()
        # except:
        #     raise ValueError
        
    except ValueError:
        # if bad request data, return 400 Bad Request
        response.status = 400
        return
    
    # TODO: Add trust score
    country_json = ''
    if not country_data.empty:
        country_data['trust_rank'] = 0.5
        country_data['flesch_reading_ease'] = 0.6
        country_data = country_data.to_dict('records')
        country_data['date'] = country_data['date'].dt.strftime('%Y-%m-%d')
    else:
        country_data = ''
    state_json = ''
    if not state_data.empty:
        state_data['trust_rank'] = 0.5
        state_data['flesch_reading_ease'] = 0.6
        state_data = state_data.to_dict('records')
        state_data['date'] = state_data['date'].dt.strftime('%Y-%m-%d')
    else:
        state_data = ''
    city_json = ''
    if not city_data.empty:
        city_data['trust_rank'] = 0.5
        city_data['flesch_reading_ease'] = 0.6
        city_data['date'] = city_data['date'].dt.strftime('%Y-%m-%d')
        city_data = city_data.to_dict('records')
    else:
        city_data = ''

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({"country":country_data, "state":state_data, "city":city_data}, ensure_ascii=False)


if __name__ == '__main__':
    run(host = '127.0.0.1', port = 8000)

