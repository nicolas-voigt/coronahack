import mysql.connector


def connect() -> mysql.connector.MySQLConnection:
    cnx = mysql.connector.connect(user='coronahack', password='xapooyo6HeeS',
                                  host='ketograph.de', database='coronahack')
    return cnx