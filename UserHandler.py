
from __future__ import print_function
import mysql.connector

class UserHandle():

    def __init__(self, name, pwd, email):
        self.name = name
        self.pwd = pwd
        self.email = email
        self.mariaCon = None
        self.cursor = None
        self.uid = None
        self.uniqueUser=None

        self.ConnectToDB()


    def ConnectToDB(self):
        #creating MySQLConnection object using connect() constructor to the MySQL server. 
        self.mariaCon = mysql.connector.connect(user='flask', host ='localhost', password = 'flaskpass' , database ='scifinder')
        self.cursor = self.mariaCon.cursor()

    def DisconnectDB(self):
        self.mariaCon.close()

    def DoesUserExist(self):
        '''Determines is user exists. Returns true if user exists,
        returns false and number of users with same email in a tuple (email, num_of_dupliates)'''
        query = "SELECT email FROM User WHERE email = %s "

        self.cursor.execute(query,(self.email,) )

        i = 0
        for each in self.cursor:
            i += 1
        print("length of cur", i)

        #IF USER DOES NOT EXIST, ADD USER TO DATABSSE
        if i == 0:
            return False

        elif i > 0:
            return (True, i)  #if 1 then just returns 1 which is also true? Works vecause only use negate

    def AddNewUser(self):
        '''If user sucessifully added, will return "success". If user already exists, 
        then returns "error" and user is not added'''
        if not self.name or not self.pwd or not self.email:
            return "Error: User already exists. Please try a different email address."

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

            #need to get userid and store
            query_uid = "SELECT uid FROM User WHERE email = %s"
            self.cursor.execute(query_uid, (self.email,))

            self.uid = self.cursor.fetchone()[0]

            print("User: ", self.name, "added to database")
            return "sucess"

        #USER ALREADY EXISTS, DONT ADD
        else:
            print("User: ", self.name, " already exists, not added!")
            return "Error: User already exists. Please try a different email address."

    def PopulatePage(self, about, research):

        #Add about and research to Page

        add_info = ("INSERT INTO Page (user, about, research) "
                    "VALUES  (%s, %s, %s)")

        self.cursor.execute(add_info, (self.uid, about, research))
        self.mariaCon.commit()

        #once user page is populted, connection is closed
        #self.DisconnectDB

class RetrieveUserInfo():
    def __init__(self, email):
        self.email = email
        self.uid = None

        self.ConnectToDB()

    def ConnectToDB(self):
        #creating MySQLConnection object using connect() constructor to the MySQL server. 
        self.mariaCon = mysql.connector.connect(user='flask', host ='localhost', password = 'flaskpass' , database ='scifinder')
        self.cursor = self.mariaCon.cursor()

    def GetUid(self):
        query_uid = "SELECT uid FROM User WHERE email = %s"
        self.cursor.execute(query_uid, (self.email,))

        self.uid = self.cursor.fetchone()[0]
        return self.uid


    def CheckLogin(self,password):
        query = "SELECT email FROM User WHERE email = %s AND password = %s "

        self.cursor.execute(query,(self.email,password) )

        if self.cursor.fetchone() is None:
            return False
        else:
            return True


    def DisconnectDB(self):
        self.mariaCon.close()

    def GetPage(self):
        query_uid = "SELECT Page.research, Page.about FROM User join Page on User.uid=Page.user WHERE User.email = %s "
        self.cursor.execute(query_uid, (self.email,))
        return self.cursor.fetchone()



if __name__ == "__main__":
    #new = UserHandle("5Ronjo", "5new here", "5WORKING@gmail.com")

    #new.AddNewUser()
    #new.PopulatePage("THIS WHOULD LKJLKJ", "BITEME!!!")

    retr = RetrieveUserInfo("5WORKING@gmail.com")
    print("UID: ",retr.GetUid())
    print("Research and About ", retr.GetPage())
    if retr.CheckLogin("5new here" ):
        print("login worked")
    else:
        print("login failed")






