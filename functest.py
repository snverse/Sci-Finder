
from __future__ import print_function
import mysql.connector


def AddNewUser(name, pwd, email):
    #creating MySQLConnection object using connect() constructor to the MySQL server. 
    mariaCon = mysql.connector.connect(user='flask', host ='localhost', password = 'flaskpass' , database ='scifinder')

    #creating new cursor which is a MySQLCursor object. Using connection's cursor() method
    cursor = mariaCon.cursor()

    #Info for testing
    #name = "1Bryce Vokus"
    #pwd = "secret"
    #email = "1Bryce@python.com"
    
    #making string for insert
    add_user = ("INSERT INTO User "
            " (name, password, email) "
            "VALUES  (%s, %s, %s)")

    # formatted for cursor.execute()
    user_data = (name, pwd , email)

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
        return "Success, user added"
    else:
        print("User: ", name, " already exists, not added!")
        return "Error, user already exixts"

if AddNewUser("2Bryce", "whatever", "hello@gmail.com"):
    print("yep we added")

else:
    print("NOT ADDED, returned true")
