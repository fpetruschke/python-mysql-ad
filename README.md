# python-mysql-ad
Python script to manage Active Directory

# Requirements

* Running MySql-Server
* Python 3.x
* mysql.connector 2.0.4

# Deployment

## Mysql-Configuration

To setup the database connection to the mysql database you can use the config.py
The config.py **must** contain following entries:

* hostName = '<localhost | IP>'
* dbName = '<name of your mysql db>'
* dbUser = '<user who has access to the db>'
* dbPassword = '<password of the above user>'

