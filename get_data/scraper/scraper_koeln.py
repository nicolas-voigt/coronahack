import requests
import urllib.request
import time

from datetime import datetime

from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector

import mysql.connector as mariadb

import locale

url = 'https://www.stadt-koeln.de/artikel/69095/index.html'


def PushNewDataToDB(tuple):
    
    # Return-Status 0 success
    # Return-status 1 fail
    # Return-status 2 data already in db
    try:
        date = tuple[0]
        url = tuple[1]
        title = tuple[2]

        cityName = "Köln"

        srcName = tuple[3]
        srcType = tuple[4]
        
        debug = False

        cursor.execute("SELECT * FROM news WHERE date = %s AND url = %s AND title = %s", (date, url, title))   
        if(debug):
            print("1 Filte for old data")
        i = 0
        for data in cursor:
            i = i + 1
        if(i > 0):
            print("URL already in DB")
            return 2


        # get ID of City 
        cursor.execute("SELECT id FROM city WHERE name = %s", (cityName,))   
        if(debug):
            print("2 Search for city id")
        ID_City = -1
        for data in cursor:
            ID_City = data[0]


        # Check for Source 
        cursor.execute("SELECT id FROM source WHERE name = %s AND type = %s", (srcName, srcType))   
        if(debug):
            print("3 Search for Source-ID")
        ID_Src = -1
        for data in cursor:
            ID_Src = data[0]
            
        # Push new Source-record, if none was found
        if(ID_Src == -1):
            cursor.execute("INSERT INTO source (name, type) VALUES (%s, %s)",(srcName, srcType)) 
            if(debug):
                print("4 Insert new Source-Record")

        cursor.execute("SELECT id FROM source WHERE name = %s AND type = %s", (srcName, srcType))  
        if(debug):
            print("5 Select newly inserted Source-ID")
        ID_Src = -1 
        for data in cursor:
            ID_Src = data[0]

        # Check for old news-record
        cursor.execute("SELECT id FROM news WHERE date = %s AND url = %s AND title = %s AND city_id = %s AND source_id = %s", (date,url,title,ID_City, ID_Src))   
        if(debug):
            print("6 Search for old news in DB")
        ID_news = -1 
        for data in cursor:
            ID_news = data[0]

        if(ID_news < 0):
            print("7 news-record was not in DB. Inserting new record")
            
            # query_insertNewNews = "INSERT INTO news (date, url, title, city_id, source_id) VALUES ({0}, {1}, {2}, {3}, {4})".format(date, url, title, ID_City, ID_Src)
            # print(query_insertNewNews)
            # cursor.execute(query_insertNewNews)

            cursor.execute("INSERT INTO news (date, url, title, city_id, source_id) VALUES (%s, %s, %s, %s, %s)", (date, url, title, ID_City, ID_Src))
            print("finished")
            if(debug):
                print("8 finished inserting")
        
        return 0
    except:
        print("Query Failed!")
        return 1
    


# main
locale.setlocale(locale.LC_ALL, 'de_DE')

listDate = []
listUrl = []
listTitle = []

srcName = "Stadt Köln"
srcType = "Stadtregierung"

bDatafeedsLeft = True

print("crawling..")
while bDatafeedsLeft:

    resp = requests.get(url)
    

    http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(resp.content, 'lxml', from_encoding=encoding)

    bDatafeedsLeft = False
    
    for a in soup.findAll("ul",{"class":"textteaserliste",  "id":"ziel_0_2"}):
        # date
        for i in a.findAll("time"):
            attrDate = i.attrs['datetime']# 2020-03-21T17:32:00+00:00
            splitSting = attrDate.split('+')
            attrDate = splitSting[0] # 2020-03-21T17:32:00
            datetime_object = datetime.strptime(attrDate, '%Y-%m-%dT%H:%M:%S')
            # print(datetime_object)
            listDate.append(datetime_object)

        # url
        for i in a.findAll("a"):
            tmpUrl = "https://www.stadt-koeln.de" + i.attrs['href']
            # print(tmpUrl)
            listUrl.append(tmpUrl)
                
        # title
        for i in a.findAll("h2"):
            tmpTitle = i.text
            # print(tmpUrl)
            listTitle.append(tmpTitle)

        # search for next page
        for i in soup.findAll("a", {"rel":"next"}):
            url = "https://www.stadt-koeln.de" + i.attrs['href']
            bDatafeedsLeft = True
            print(f"crawling to next page - {url}")


print("crawling finished")
# print(len(listDate))
# print(len(listUrl))
# print(len(listTitle))

tuplelist = []
for i in range(0,listDate.__len__()):
    tuplelist.append((listDate[i], listUrl[i], listTitle[i], srcName,srcType))

print()
print("Connecting to db..")
mariadb_connection = mariadb.connect(host="ketograph.de",user='coronahack', password='xapooyo6HeeS', database='coronahack')
cursor = mariadb_connection.cursor()
print("connected!")



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

# cursor.execute("SHOW COLUMNS FROM news FROM coronahack;")
# for x in cursor:
#     print(x)

# cursor.execute("SELECT * FROM source")
# for data in cursor:
#     print(data)



# Push newsdata to DB
for i in range(2,tuplelist.__len__()):
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
