import mysql.connector as mariadb
from datetime import datetime

__HOST__ = "ketograph.de"
__USER__ = "coronahack"
__PWD__  = "xapooyo6HeeS"
__DB__   = "coronahack"

mariadb_connection = mariadb.connect(host=__HOST__,user=__USER__, password=__PWD__, database=__DB__)
cursor = mariadb_connection.cursor()

def GetStateIds():
    cursor.execute("SELECT * FROM state")
    stateDict = {}
    for id,name in cursor:
        stateDict[name] = id
    return stateDict
def GetCityIds():
    cursor.execute("SELECT id, name FROM city")
    cityDict = {}
    for id,name in cursor:
        cityDict[name] = id
    return cityDict
def GetSourceIds():
    cursor.execute("SELECT id, name FROM source")
    sourceDict = {}
    for id,name in cursor:
        sourceDict[name] = id
    return sourceDict
    
stateDict = GetStateIds()
cityDict = GetCityIds()
sourceDict = GetSourceIds()

def InsertSource(source,sourceType):
    #Source Types,Bundesregierung,Landesregierung,Stadtregierung,Presse,Institut
    cursor.execute("INSERT INTO source (name,type) VALUES(%s,%s);",(source,sourceType))
    cursor.execute("SELECT LAST_INSERT_ID();")
    for id in cursor:
        return id[0]
    mariadb_connection.commit()

def InsertNews(city,source,sourceType, date,title,url,fromFedGovt = False):
    global sourceDict
    if(source not in sourceDict):
        InsertSource(source,sourceType)
        sourceDict = GetSourceIds()
    if(fromFedGovt):
        execQuery = cursor.execute("INSERT INTO news (city_id,state_id,source_id,date,title,url) VALUES (%s, %s, %s, %s, %s, %s)", \
                                    (None,None,sourceDict[source],date,title,url))
    else:
        execQuery = cursor.execute("INSERT INTO news (city_id,source_id,date,title,url) VALUES (%s, %s, %s, %s, %s)", \
                                    (cityDict[city], sourceDict[source],date,title,url))
    result = cursor.execute(execQuery)    
    mariadb_connection.commit()
    return result

# InsertSource("Stadt Recklinghausen", "Stadtregierung")
# InsertNews("Recklinghausen", "Stadt Recklinghausen", "Stadtregierung", datetime.now(), "Title_test_123", "URL_TEST_123")
