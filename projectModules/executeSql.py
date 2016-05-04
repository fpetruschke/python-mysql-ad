import mysql.connector
import config.mysqlConfig


# Method for connecting to database
def connect():
    # setting up the db connection via the mysqlConfig.py
    db = mysql.connector.connect(host=config.mysqlConfig.hostName, database=config.mysqlConfig.dbName,
                                 user=config.mysqlConfig.dbUser, password=config.mysqlConfig.dbPassword)
    return db


# method for destroying database connection
def destroy(cursor, connection):
    cursor.close()
    connection.close()


# takes a queryString in Format """query"""
def executeMysqlShow(stringToSelect, tableName):
    db = connect()
    # defining the cursor for reading data
    cursor = db.cursor()
    # query the database
    cursor.execute("""SELECT""" + stringToSelect + """ FROM """ + tableName, )
    rows = cursor.fetchall()
    # destroying db connection
    destroy(cursor, db)
    return rows


def executeMysqlInsert(tablename, values):
    db = connect()
    cursor = db.cursor()

    add_user = ("INSERT INTO "+ tablename + "(name, firstname, password, class) VALUES (%(name)s, %(firstname)s, %(password)s, %(class)s)")

    cursor.execute(add_user, values)
    # Make sure data is committed to the database
    db.commit()
    destroy(cursor, db)


def executeMysqlDelete(tablename, column, value):
    db = connect()
    cursor = db.cursor()

    # delete statement
    del_user = "DELETE FROM `"+ tablename +"` WHERE `"+ tablename +"` . `"+ column +"`= " + str(value)

    # execution, commit and destruction of curser and connection
    cursor.execute(del_user)
    db.commit()
    destroy(cursor, db)