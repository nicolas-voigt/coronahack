#!/usr/bin/python
# -*- coding: utf8 -*-

import pandas as pd 
import numpy as np 

import json

import sqlalchemy
import datetime

#We are using bottle for the api
from bottle import request, response, run
from bottle import post, get, put, delete
import bottle
import config

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + config.username + ':'+ config.password + '@' + config.server+ '/' + config.database

# # Test if it works
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)
# print(engine.table_names())

def add_cors_headers():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = \
        'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = \
        'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@bottle.route('/<:re:.*>', method='OPTIONS')
def enable_cors_generic_route():
    """
    This route takes priority over all others. So any request with an OPTIONS
    method will be handled by this function.

    See: https://github.com/bottlepy/bottle/issues/402

    NOTE: This means we won't 404 any invalid path that is an OPTIONS request.
    """
    add_cors_headers()

@bottle.hook('after_request')
def enable_cors_after_request_hook():
    """
    This executes after every route. We use it to attach CORS headers when
    applicable.
    """
    add_cors_headers()

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

def calc_trust_score(data):
    # https://en.wikipedia.org/wiki/Rule_of_succession
    user_rating = (data['user_rating'] + 1 ) / (data['total_ratings'] + 2)

    time_delta = datetime.timedelta(datetime.datetime.today() - data['date']).days
    source_score = get_source_score(data['url'])
    score = source_score * (1 / (1 * np.e**(0.5*time_delta))) # source_score * sigmoid(t)
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
    request_data = {}
    data = {'country':pd.DataFrame(), 'state':pd.DataFrame(), 'city':pd.DataFrame()}
    try:
        try:
            request_data = request.json
        except:
            raise ValueError
        try:
            if request_data['country']:
                data['country'] = pd.read_sql(sql='SELECT * FROM news WHERE state_id IS NULL AND city_id IS NULL', con=engine)
            else:
                data['country'] = pd.DataFrame()
        except KeyError:
            raise KeyError
        
        try:
            if request_data['state']:
                state_id = pd.read_sql(sql='SELECT * FROM state WHERE name="{0}"'.format(request_data['state']), con=engine).at[0,'id']
                data['state'] = pd.read_sql(sql='SELECT * FROM news WHERE state_id="{0}"'.format(state_id)  , con=engine)
                data['state']['name'] = request_data['state']
                
            else:
                data['state'] = pd.DataFrame()
        except KeyError:
            raise KeyError

        try:
            if request_data['city']:
                city_id = pd.read_sql(sql='SELECT * FROM city WHERE name="{0}"'.format(request_data['city']), con=engine).at[0, 'id']
                data['city'] = pd.read_sql(sql='SELECT * FROM news WHERE city_id="{0}"'.format(city_id), con=engine)
                data['city']['name'] = request_data['city']
            else:
                data['city'] = pd.DataFrame()
        except KeyError:
            raise KeyError
        
    except ValueError:
        # if bad request data, return 400 Bad Request
        response.status = 400
        return
    except KeyError:
        # if bad request data, return 400 Bad Request
        response.status = 400
        return
    
    # TODO: Add trust score
    for key in data:
        if not data[key].empty:
            data[key]['trust_rank'] = 0.5
            data[key]['flesch_reading_ease'] = 0.6 # https://pypi.org/project/textstat/
            source_id = data[key].at[0,'source_id']
            sql_quer = 'SELECT * FROM source WHERE id="{0}"'.format(source_id)
            data[key]['source_name'] = pd.read_sql(sql=sql_quer.format(source_id), con=engine).at[0, 'name']

            data[key]['date'] = data[key]['date'].dt.strftime('%Y-%m-%d')
            data[key] = data[key].to_dict('records')
        else:
            data[key] = ''

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({"country":data['country'], "state":data['state'], "city":data['city']}, ensure_ascii=False)


if __name__ == '__main__':
    run(host = '127.0.0.1', port = 8000)

