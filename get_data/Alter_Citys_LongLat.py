import requests
import urllib.request
import time

from datetime import datetime

from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector

import mysql.connector as mariadb

import locale

print()
print("Connecting to db..")
mariadb_connection = mariadb.connect(host="ketograph.de",user='coronahack', password='xapooyo6HeeS', database='coronahack')
cursor = mariadb_connection.cursor()
print("connected!")

import json

def load_city_list(filename: str):
    with open(filename) as cityfile:
        data = json.load(cityfile)
    return data

def insert_cities(cities, connection):
    # keys: item, itemLabel, website, coordinates, BundeslandLabel
    c = connection.cursor(buffered=True)  # to avoid mysql.connector.errors.InternalError: Unread result found
    for city in cities:
        c.execute("SELECT id FROM city WHERE name = %s", (city["itemLabel"], ))
        result = c.fetchone()
        if result:
            print(f"Skipped id {result}")
            continue
        bundesland = city["BundeslandLabel"]
        c.execute("SELECT id FROM state WHERE name = %s", (bundesland, ))
        state_id = c.fetchone()[0]

        query = f"INSERT INTO city (name, state_id, coordinates) VALUES ('{city['itemLabel']}', {state_id}, ST_PointFromText('{city['coordinates']}'))"
        c.execute(query)
        connection.commit()


cities = load_city_list("city_list.json")   

for city in cities:
    # print(city)
    splitPoint = city['coordinates'].replace("Point(","").replace(")","").split(" ")

    cityname = city['itemLabel']
    pointX = splitPoint[0]
    pointY = splitPoint[1]
    
    ID_City = -1
    print(cityname)
    cursor.execute("SELECT * FROM city WHERE name = %s", (cityname,))    
    for data in cursor:
        ID_City = data[0]
        print(data)


    
    cursor.execute("UPDATE city SET longitude = %s, latitude = %s", (pointX, pointY,))
    




cursor.execute("select * from city limit 2")


index = 0
for blob in cursor:
    print(blob)
# print(index)


# tables = []
# cursor.execute("SHOW TABLES")
# for (table_name,) in cursor:
#     tables.append(table_name)

# for i in range(0, tables.__len__()):
#     table = tables[i]
#     print(table)
#     cursor.execute("SHOW COLUMNS FROM " + table + " FROM coronahack;")
#     for x in cursor:
#         print(x)

mariadb_connection.commit()