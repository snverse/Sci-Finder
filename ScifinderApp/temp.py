from __future__ import print_function
import mysql.connector

#creating MySQLConnection object using connect() constructor to the MySQL server. 
mariaCon = mysql.connector.connect(user='flask', host ='localhost', password = 'flaskpass' , database ='scifinder')

#creating new cursor which is a MySQLCursor object. Using connection's cursor() method
cursor = mariaCon.cursor()

#insert new user

name = "Bryce Vokus"
pwd = "secret"
email = "Bryce@python.com"

add_user ="INSERT INTO User (name, password, email) VALUES  (%s, %s, %s)"
user_data = (name, pwd, email)

cursor.execute(add_user, user_data)

print("attempting to add to databsse: ", name, pwd, email)

#MakeNewUser(name, password, email)
