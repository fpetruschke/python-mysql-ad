import mysql.connector
import config.mysqlConfig


# takes a queryString in Format """query"""
def executeSqlShow(querystring):
    # setting up the db connection via the mysqlConfig.py
    db = mysql.connector.connect(host=config.mysqlConfig.hostName, database=config.mysqlConfig.dbName, user=config.mysqlConfig.dbUser, password=config.mysqlConfig.dbPassword)
    # defining the cursor for reading data
    cursor = db.cursor()
    # query the database
    cursor.execute(querystring, )
    rows = cursor.fetchall()
    db.close()
    return rows
