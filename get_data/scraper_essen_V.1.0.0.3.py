import requests
import urllib.request
import time

from datetime import datetime

from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector

import mysql.connector as mariadb

import locale

pagenum = 1
url = 'https://www.essen.de/meldungen/meldungen_letzte_tage.de.jsp?pageNo=' + str(pagenum)


def PushNewDataToDB(tuple):
    
    # Return-Status 0 success
    # Return-status 1 fail
    # Return-status 2 data already in db
    try:
        date = tuple[0]
        url = tuple[1]
        title = tuple[2]

        cityName = "Essen"

        srcName = tuple[3]
        srcType = tuple[4]
        

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



listDate = []
listUrl = []
listTitle = []

srcName = "Stadt Essen"
srcType = "Stadtregierung"

bDatafeedsLeft = True

while bDatafeedsLeft:

    resp = requests.get(url)
    

    http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(resp.content, 'lxml', from_encoding=encoding)


    bDatafeedsLeft = False  

    # date
    for i in soup.findAll("td",{"headers":"date"}):    
        datetime_object = datetime.strptime(i.text, '%d.%m.%Y')
        listDate.append(datetime_object)

    # url & title
    for a in soup.findAll("td",{"headers":"title"}):
        for b in a.find_all('a', href=True):
            tmpUrl = "https://www.essen.de/meldungen/" + b['href']
            listUrl.append(tmpUrl)
            # print(tmpUrl)
            tmpTitle = b.text
            listTitle.append(tmpTitle)
            # print(tmpTitle)

    # search for next page
    for i in soup.findAll("a", {"title":"Eine Seite vorblättern."}):
        url = "https://www.essen.de" + i.attrs['href']
        bDatafeedsLeft = True


tuplelist = []
for i in range(0,listDate.__len__()):
    tuplelist.append((listDate[i], listUrl[i], listTitle[i], srcName,srcType))


print(tuplelist[0])

mariadb_connection = mariadb.connect(host="ketograph.de",user='coronahack', password='xapooyo6HeeS', database='coronahack')
cursor = mariadb_connection.cursor()




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
