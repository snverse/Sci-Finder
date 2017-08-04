from __future__ import print_function
import mysql.connector

#creating MySQLConnection object using connect() constructor to the MySQL server. 
mariaCon = mysql.connector.connect(user='flask', host ='localhost', password = 'flaskpass' , database ='scifinder')

#creating new cursor which is a MySQLCursor object. Using connection's cursor() method
cursor = mariaCon.cursor()

#insert new user
name = "1Bryce Vokus"
pwd = "secret"
email = "1Bryce@python.com"

add_user = ("INSERT INTO User " 
            " (name, password, email) " 
            "VALUES  (%s, %s, %s)")

# formatted for cursor.execute()
user_data = (name, pwd , email)

#works in sql INSERT INTO User  (name, password, email) VALUES  ("NAME" , "PASSWORD", "EMAIL")

#DOES USER EXIST ALREADY
query = "SELECT email FROM User WHERE email = %s " 

cursor.execute(query,(email,) )

i = 0
for each in cursor:
    i += 1
print("length of cur", i)

#IF USER DOES NOT EXIST, ADD USER TO DATABSSE
if i == 0:
    cursor.execute(add_user, user_data)

    #commit to database
    mariaCon.commit()
    print("User: ", name, "added to database")
else:
    print("User: ", name, " already exists, not added!")



#MakeNewUser(name, password, email)
