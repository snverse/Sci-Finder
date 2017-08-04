#__init__.py
from __future__ import print_function
from flask import Flask
import mysql.connector   #communicates with MySQL database (MariaDB)

s_app = Flask(__name__)  # Create a Flask application object called t_app 
#s_app.config.from_object('config') # was giving error 

#from ScifinderApp import views # Import the views module from the ScifinderApp package
import views

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
        return "success"
    else:
        print("User: ", name, " already exists, not added!")
        return "error"

if __name__ == "__main__":
    s_app.run(debug=True)
    print("*******THIS IS RUNNING __INIT___ FILE :" , __name__)
