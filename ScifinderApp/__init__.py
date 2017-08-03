#__init__.py

from flask import Flask

s_app = Flask(__name__)  # Create a Flask application object called t_app 
#s_app.config.from_object('config') # was giving error 

#from ScifinderApp import views # Import the views module from the ScifinderApp package
import views

if __name__ == "__main__":
    s_app.run(debug=True)
    print("*******THIS IS RUNNING __INIT___ FILE :" , __name__)
