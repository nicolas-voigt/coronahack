import mysql.connector as mariadb
from datetime import datetime
import json

__HOST__ = "ketograph.de"
__USER__ = "coronahack"
__PWD__  = "xapooyo6HeeS"
__DB__   = "coronahack"

mariadb_connection = mariadb.connect(host=__HOST__,user=__USER__, password=__PWD__, database=__DB__)
cursor = mariadb_connection.cursor()

resultSet = []
resultDict = []

sourceDict = {
    "Stadt Essen" : (7.21897,51.54258),
    "Stadt Herne" : (7.013055555,51.450833333),
    "Stadt Recklinghausen" : (7.2,51.616666666),
    "Stadt Muenster" : (7.625555555,51.9625),
    "Stadt Berlin" : (13.4050,52.5200),
    "Stadt Köln" : (6.957777777,50.942222222),
    "Stadt Hamburg" : (9.993682,53.551085),
    "Stadt München" : (11.5755,48.137194444),
    "Stadt Leipzig" : (12.3730747,51.3396955),
    "Stadt Dortmund" : (7.4652981,51.5135872),
    "Stadt Bremen" : (8.8016937,53.0792962),
    "Stadt Hannover" : (9.7320104,52.3758916),
}

#sourcename,sourcetype,title,url,LG,BG

cursor.execute("Select s.name,s.type,n.title,n.url,c.latitude,c.longitude from news n left join city c on n.city_id = c.id left join source s on n.source_id = s.id where s.name = %s LIMIT 20", ("Stadt Herne",))
for x in cursor:
    resultSet.append(x)

cursor.execute("Select s.name,s.type,n.title,n.url,c.latitude,c.longitude from news n left join city c on n.city_id = c.id left join source s on n.source_id = s.id where s.name = %s LIMIT 20", ("Stadt Essen",))
for x in cursor:
    resultSet.append(x)

cursor.execute("Select s.name,s.type,n.title,n.url,c.latitude,c.longitude from news n left join city c on n.city_id = c.id left join source s on n.source_id = s.id where s.name = %s LIMIT 20", ("Stadt Muenster",))
for x in cursor:
    resultSet.append(x)

cursor.execute("Select s.name,s.type,n.title,n.url,c.latitude,c.longitude from news n left join city c on n.city_id = c.id left join source s on n.source_id = s.id where s.name = %s LIMIT 20", ("Stadt Berlin",))
for x in cursor:
    resultSet.append(x)

cursor.execute("Select s.name,s.type,n.title,n.url,c.latitude,c.longitude from news n left join city c on n.city_id = c.id left join source s on n.source_id = s.id where s.name = %s LIMIT 20", ("Stadt Köln",))
for x in cursor:
    resultSet.append(x)

cursor.execute("Select s.name,s.type,n.title,n.url,c.latitude,c.longitude from news n left join city c on n.city_id = c.id left join source s on n.source_id = s.id where s.name = %s LIMIT 20", ("Stadt Hamburg",))
for x in cursor:
    resultSet.append(x)

cursor.execute("Select s.name,s.type,n.title,n.url,c.latitude,c.longitude from news n left join city c on n.city_id = c.id left join source s on n.source_id = s.id where s.name = %s LIMIT 20", ("Stadt München",))
for x in cursor:
    resultSet.append(x)

cursor.execute("Select s.name,s.type,n.title,n.url,c.latitude,c.longitude from news n left join city c on n.city_id = c.id left join source s on n.source_id = s.id where s.name = %s LIMIT 20", ("Stadt Leipzig",))
for x in cursor:
    resultSet.append(x)

cursor.execute("Select s.name,s.type,n.title,n.url,c.latitude,c.longitude from news n left join city c on n.city_id = c.id left join source s on n.source_id = s.id where s.name = %s LIMIT 20", ("Stadt Dortmund",))
for x in cursor:
    resultSet.append(x)

cursor.execute("Select s.name,s.type,n.title,n.url,c.latitude,c.longitude from news n left join city c on n.city_id = c.id left join source s on n.source_id = s.id where s.name = %s LIMIT 20", ("Stadt Bremen",))
for x in cursor:
    resultSet.append(x)

cursor.execute("Select s.name,s.type,n.title,n.url,c.latitude,c.longitude from news n left join city c on n.city_id = c.id left join source s on n.source_id = s.id where s.name = %s LIMIT 20", ("Stadt Hannover",))
for x in cursor:
    resultSet.append(x)

for rset in resultSet:
    tempDict = {}
    tempDict["SourceName"] = rset[0]
    tempDict["SourceType"] = rset[1]
    tempDict["Title"] = rset[2]
    tempDict["Url"] = rset[3]
    tempDict["Latitude"] = sourceDict[rset[0]][0]
    tempDict["Longitude"] = sourceDict[rset[0]][1]
    resultDict.append(tempDict)

with open('db_dump.json', 'w') as outfile:
    json.dump(resultDict, outfile)