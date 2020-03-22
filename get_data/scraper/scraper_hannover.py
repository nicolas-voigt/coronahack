import requests
import urllib.request
import time

from datetime import datetime

from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector

import mysql.connector as mariadb

import locale

pagenum = 1
url = 'https://presse.hannover-stadt.de/index.cfm?page=' + str(pagenum)

def PushNewDataToDB(tuple):
    # TODO push whole list to database instead of single elements
    # this could improve performance

    # Return-Status 0 success
    # Return-status 1 fail
    # Return-status 2 data already in db
    try:
        date = tuple[0]
        url = tuple[1]
        title = tuple[2]

        cityName = "München"

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
            ID_Src = data[0]

        if(ID_news < 0):
            cursor.execute("INSERT INTO news (date, url, title, city_id, source_id) VALUES (%s, %s, %s, %s, %s)", (date, url, title, ID_City, ID_Src))
        
        return 0
    except Exception as e:
        print(e)
        print("Query Failed!")
        return 1
    


# main
# locale.setlocale(locale.LC_ALL, 'de_DE')



listDate = []
listUrl = []
listTitle = []

srcName = "Stadt Hannover"
srcType = "Stadtregierung"
base_url = "https://presse.hannover-stadt.de/"
first_date = datetime(2020, 2, 20)

datefeedsleft = True

while datefeedsleft:
    datefeedsleft = False
    resp = requests.get(url)

    http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type',
                                                                   '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(resp.content, 'lxml', from_encoding=encoding)

    # find all rows:
    newss = soup.find("div", {"id": "sectionOhneAjax"}).find("ul", {"id": "pressemeldungenUL"})
    newss = newss.find_all("li", recursive=False)
    print("Found ", len(newss), "news")
    for news in newss:
        ul = news.find("ul", recursive=False)
        date = ul.find("li").text
        link = news.find("h2").find("a")
        title = link.text
        url = link["href"]
        url = base_url + url
        print(url, title, date)

        listUrl.append(url)
        listTitle.append(title)
        datetime_object = datetime.strptime(date, "%d.%m.%Y")
        listDate.append(datetime_object)
    if first_date >= datetime_object:
        break

    # search for next page
    next_page = soup.findAll("li", {"id": "seitenVorLI"})
    if len(next_page) == 1:
        next_url = next_page[0].find("a")["href"]
        url = base_url + next_url
        datefeedsleft = True



tuplelist = []
for i in range(0, len(listDate)):
    tuplelist.append((listDate[i], listUrl[i], listTitle[i], srcName, srcType))


print(tuplelist)

mariadb_connection = mariadb.connect(host="ketograph.de", user='coronahack',
                                     password='xapooyo6HeeS', database='coronahack')
cursor = mariadb_connection.cursor()


for t in tuplelist:
    result = PushNewDataToDB(t)
    print("[" + str(result) + "] - " + t[1])

mariadb_connection.commit()

