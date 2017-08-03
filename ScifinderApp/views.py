#views.py

from __init__ import s_app
from flask import render_template, requests



@s_app.route('/')
@s_app.route('/index')
def main():
    return render_template('index.html')

@s_app.route('/signup.html')
def showSignUp():
    return render_template('signup.html')

@s_app.route('/addUser', methods=['post'])
def addUser():
    
