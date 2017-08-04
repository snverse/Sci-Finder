
from __future__ import print_function
import mysql.connector

class UserHandle():

    def __init__(self, name, pwd, email):
        self.name = name
        self.pwd = pwd
        self.email = email
        self.mariaCon = None
        self.cursor = None

        self.ConnectToDB()

    def ConnectToDB(self):
        #creating MySQLConnection object using connect() constructor to the MySQL server. 
        self.mariaCon = mysql.connector.connect(user='flask', host ='localhost', password = 'flaskpass' , database ='scifinder')
        self.cursor = self.mariaCon.cursor()

    def DisconnectDB(self):
        self.mariaCon.close()

    def DoesUserExist(self):
        '''Determines is user exists. Returns true if user exists,
        returns false if user does not exist'''
        query = "SELECT email FROM User WHERE email = %s "

        self.cursor.execute(query,(self.email,) )

        i = 0
        for each in self.cursor:
            i += 1
        print("length of cur", i)

        #IF USER DOES NOT EXIST, ADD USER TO DATABSSE
        if i == 0:
            return False

        else:
            return True

    def AddNewUser(self):
        '''If user sucessifully added, will return "success". If user already exists, 
        then returns "error" and user is not added'''

        add_user = ("INSERT INTO User "
                    " (name, password, email) "
                    "VALUES  (%s, %s, %s)")

        user_data = (self.name, self.pwd , self.email)

        #NEW USER!
        #User does not exist
        if not self.DoesUserExist():
            self.cursor.execute(add_user, user_data)

            #commit to database
            self.mariaCon.commit()
            print("User: ", self.name, "added to database")
            return "success"

        #USER ALREADY EXISTS, DONT ADD
        else:
            return "Error: User already exists. Please try a different email address."

    def PopulateUserPage(self, about, research):
        #Add about PI to database
        add_about = ("INSERT INTO Page "
                    " (about) "
                    "VALUES  (%s)")

        self.cursor.execute(add_about, (about,) )

        #Add reserach to database
        add_research = ("INSERT INTO Page "
                    " (research) "
                    "VALUES  (%s, %s, %s)")

        self.cursor.execute(add_about, (about,) )





        #once user page is populted, connection is closed
        self.DisconnectDB




if __name__ == "__main__":
    new = UserHandle("99Bryce", "99whatever", "99hello@gmail.com")

    new.AddNewUser()
    new.PopulateUserPage("My name is Bryce hello", "I like to research Frisbees")
