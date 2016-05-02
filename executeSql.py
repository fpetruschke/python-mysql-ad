import mysql.connector
import config


# takes a queryString in Format """query"""
def executeSqlShow(querystring):
    # setting up the db connection via the config.py
    db = mysql.connector.connect(host=config.hostName, database=config.dbName, user=config.dbUser, password=config.dbPassword)
    # defining the cursor for reading data
    cursor = db.cursor()
    # query the database
    cursor.execute(querystring, )
    rows = cursor.fetchall()
    db.close()
    return rows
