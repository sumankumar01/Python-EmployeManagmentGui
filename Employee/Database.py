from random import random

import mysql.connector
from mysql.connector import Error


class Db:

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def logindb(self):
        global status
        global record
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='employee',
                                                 user='root',
                                                 password='suman')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                print("select * from login where ID={} and password='{}';".format(self.username,self.password))
                cursor.execute("select * from login where ID={} and password='{}';".format(self.username,self.password))
                record = cursor.fetchone()
                status=cursor.rowcount
                print("You're connected to database: ", status)
                print("You're connected to database: ", record[1])

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

        return status,record

    def register(self,first_name,last_name,user_name,city,gender,age,password):
        global status
        global record
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='employee',
                                                 user='root',
                                                 password='suman')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()

                #cursor.execute("select * from login where ID={};".format(self.username))
                print("insert into emp(FirstName,LastName,EMPID,City,Gender,age) values('{}','{}',{},'{}','{}','{}');".format(first_name,last_name,int(user_name),city,'M',age))

                cursor.execute("insert into emp(FirstName,LastName,EMPID,City,Gender,age) values('{}','{}',{},'{}','{}','{}');".format(first_name,last_name,int(user_name),city,'M',age))

                print("insert into login values({},'{}')".format(int(user_name),password))

                status = cursor.rowcount



                print("You're connected to database: ", status)
                print("You're connected to database: ", record[1])

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        return status, record

    def validateUser(self):
        global status
        global record
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='employee',
                                                 user='root',
                                                 password='suman')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()

                cursor.execute("select * from login where ID={};".format(self.username))
                record = cursor.fetchone()
                status=cursor.rowcount



                print("statsu of querry ", status)


        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        return status