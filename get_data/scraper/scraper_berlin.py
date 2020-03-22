import requests
import urllib.request
import time

from datetime import datetime

from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector

import mysql.connector as mariadb

import locale

pagenum = 1
url = 'https://www.berlin.de/presse/pressemitteilungen/index/index/page/' + str(pagenum)


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

        cityName = "Berlin"

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
    except:
        print("Query Failed!")
        return 1
    


# main
# locale.setlocale(locale.LC_ALL, 'de_DE')



listDate = []
listUrl = []
listTitle = []

srcName = "Stadt Berlin"
srcType = "Stadtregierung"
base_url = "https://www.berlin.de"
first_date = datetime(2020, 2, 20)

bDatafeedsLeft = True

while bDatafeedsLeft:
    resp = requests.get(url)

    http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(resp.content, 'lxml', from_encoding=encoding)


    bDatafeedsLeft = False  

    # find all rows:
    rows = soup.findAll("tr", {"class": "odd"}) + soup.findAll("tr", {"class": "even"})
    for row in rows:
        elems = row.findAll("td")
        date = elems[0].text.replace("\n", "")
        link = elems[1].find("a", href=True)
        url = link["href"]
        title = link.text
        print(date, url, title)

        listUrl.append(base_url + url)
        listTitle.append(title)
        datetime_object = datetime.strptime(date, '%d.%m.%Y')
        listDate.append(datetime_object)
    if first_date >= datetime_object:
        # stop scraping before february 2020
        break
    # search for next page
    next_links = soup.findAll("li", {"class": "pager-next"})
    if len(next_links) >= 1:
        next_link = next_links[0].find("a")
        url = base_url + next_link.attrs['href']
        bDatafeedsLeft = True


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

