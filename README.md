# python-mysql-ad
Python script to manage Active Directory

# Requirements

* Running MySql-Server
* Python 3.x
* mysql.connector 2.0.4
* (for linux: install wmic)
* (for linux: install wmi_client_wrapper)
* WMI (Windows Manager Interface)


# Deployment

## Get everything running on school PCs

1. install python 3.4.4 windows **msi installer** !!! from python.org
1. get the master-branch from **[http://github.com/mysql/mysql-connector-python](http://github.com/mysql/mysql-connector-python)**
1. open mysql Workbench and insert the sql statements (make sure you have the **username - column** in the table!!!!!!!!! manually add it if not: username, VARCHAR(255))
1. change the **config for mysql connection** in the project folder under "config" (mysqlConfig) to:
	'hostname' = 'localhost'
	'dbName' = 'pythonTest'
	'dbUser' = 'root'
	'dbPassword' = ''
1. project should be running by now. Start it with cmd:
    **`C:\Python34\python.exe Path\to\Project\main.py`**

## Mysql-Configuration

To setup the database connection to the mysql database you can use the config/mysqlConfig.py
The mySqlConfig.py **must** contain following entries:

* hostName = '<localhost | IP>'
* dbName = '<name of your mysql db>'
* dbUser = '<user who has access to the db>'
* dbPassword = '<password of the above user>'

## ActiveDirectory-Configuration

To setup the ssh connection to your active directory you need to adjust the "config/adConfig.py".
The adConfig.py **must** contain following entries:

* server = '<IP>'
* username = '<login name>'
* password = '<password of the above user>'


## CSV-Import

First line of your csv should contain headers!
Values must be comma seperated!

ToDo: documentation of exact column names and accepted data types

## CSV-Export

You will get all data saved in the mysql database as .csv-file

ToDo: documentation of exact column names