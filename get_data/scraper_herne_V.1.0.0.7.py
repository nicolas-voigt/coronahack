import requests
import urllib.request
import time

from datetime import datetime

from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector

import mysql.connector as mariadb

import locale


url = 'https://www.herne.de/Rathaus/Politik/'


def PushNewDataToDB(tuple):
    
    # Return-Status 0 success
    # Return-status 1 fail
    # Return-status 2 data already in db
    
    try:
        date = tuple[0]
        url = tuple[1]
        title = tuple[2]

        cityName = "Herne"

        srcName = tuple[3]
        srcType = tuple[4]
        
        
        print((date, url, title))

        cursor.execute("SELECT * FROM news WHERE date = %s AND url = %s AND title = %s", (date, url, title))   
        i = 0
        for data in cursor:
            i = i + 1
        if(i > 0):
            print("URL already in DB")
            return 2

        # get ID of City 
        cursor.execute("SELECT id FROM city WHERE name = %s", (cityName,))        
        ID_City = -1
        for data in cursor:
            ID_City = data[0]


        # Check for Source
        cursor.execute("SELECT id FROM source WHERE name = %s AND type = %s", (srcName, srcType))   
        ID_Src = -1
        for data in cursor:
            ID_Src = data[0]
            
        # Push new Source-record, if none was found
        if(ID_Src == -1):
            cursor.execute("INSERT INTO source (name, type) VALUES (%s, %s)",(srcName, srcType)) 

        cursor.execute("SELECT id FROM source WHERE name = %s AND type = %s", (srcName, srcType))  
        ID_Src = -1 
        for data in cursor:
            ID_Src = data[0]

        # Check for old news-record
        cursor.execute("SELECT id FROM news WHERE date = %s AND url = %s AND title = %s AND city_id = %s AND source_id = %s", (date,url,title,ID_City, ID_Src))   
        ID_news = -1 
        for data in cursor:
            ID_news = data[0]

        if(ID_news < 0):
            cursor.execute("INSERT INTO news (date, url, title, city_id, source_id) VALUES (%s, %s, %s, %s, %s)", (date, url, title, ID_City, ID_Src))
        
        return 0
    except:
        print("Query Failed!")
        return 1
    


# main
locale.setlocale(locale.LC_ALL, 'de_DE')


resp = requests.get(url)

http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
encoding = html_encoding or http_encoding
soup = BeautifulSoup(resp.content, 'lxml', from_encoding=encoding)

date = []
url = []
title = []

srcName = ""
srcType = "Stadtregierung"

# print(soup.findAll("title"))
for i in soup.findAll("meta", {"name":"author"}):
    srcName = i.attrs['content']

for i in soup.findAll("div",{"class":"meldung_datum"}):
    datetime_str = i.text.replace("Meldung vom ","")    
    datetime_object = datetime.strptime(datetime_str, ' %d. %B %Y ')
    date.append(datetime_object)

for a in soup.findAll("div",{"class":"meldung_inhalt"}):
    for b in a.find_all('a', href=True):
        url.append("www.herne.de" + b['href'])
        title.append(b.text)


tuplelist = []
for i in range(0,date.__len__()):
    tuplelist.append((date[i], url[i], title[i], srcName,srcType))


mariadb_connection = mariadb.connect(host="ketograph.de",user='coronahack', password='xapooyo6HeeS', database='coronahack')
mariadb_connection.rollback()
cursor = mariadb_connection.cursor()


# tables = []
# cursor.execute("SHOW TABLES")
# for (table_name,) in cursor:
#     tables.append(table_name)
#     print(table_name)

# for i in range(0, tables.__len__()):
#     table = tables[i]
#     print(table)
#     cursor.execute("SHOW COLUMNS FROM " + table + " FROM coronahack;")
#     for x in cursor:
#         print(x)

# cursor.execute("SELECT * FROM source")
# for data in cursor:
#     print(data)




for i in range(0,tuplelist.__len__()):
    result = PushNewDataToDB(tuplelist[i])
    print("[" + str(result) + "] - " + tuplelist[i][1])

mariadb_connection.commit()



# try:
#     cursor.execute("SELECT * FROM source")
#     for data in cursor:
#         print(data)
# except:
#     print("error")

    
# cursor.execute("SELECT * FROM news")
# for data in cursor:
#     print(data)
