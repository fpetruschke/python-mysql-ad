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