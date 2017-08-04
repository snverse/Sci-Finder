#views.py

from __init__ import * # s_app, AddNewUser
from flask import render_template, request
import forms

@s_app.route('/')
@s_app.route('/index')
def main():
    return render_template('index.html')

@s_app.route('/signup')
def signup():
    form = forms.SignUp()
    return render_template('signup.html', form=form)

@s_app.route('/error.html')
def error(error):
    return error
