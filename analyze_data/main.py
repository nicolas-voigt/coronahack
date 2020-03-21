import pandas as pd 
import numpy as np 
import sqlalchemy
from progress.bar import Bar
import numpy as np 
import datetime

# server ='server,com'
# database = 'name'
# username = 'mctoel'
# password =  '***'

# engine = sqlalchemy.create_engine('postgresql://'+ username +':' + password + '@' + server + '/' + database + '?sslmode=require')

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
    how_old = datetime.timedelta(datetime.datetime.now() - data['timestamp']).days
    source_score = get_source_score(data['url'])


dummy_data = pd.DataFrame({'url':'', 'timestamp':'', })

unchecked_data = pd.read_sql(sql='SELECT * FROM dbname WHERE fact_checked == False'  , con=engine)

for i in range(len(unchecked_data)):
    unchecked_data.at[i, :] = bewerte(unchecked_data.at[i, :])
    source = bewerte(source)

upload(source)

def upload():
    unchecked_data.to_sql(con=engine, if_exist='append')
    #engine.delete(source) nicht löschen
    engine.upload(source)
    engine2.upload(source)
