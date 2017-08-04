
#views.py

from __init__ import * # s_app, AddNewUser
from flask import render_template, request
from UserHandler import UserHandle
import forms

@s_app.route('/')
@s_app.route('/index')
def main():
    return render_template('index.html')

@s_app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        #do the signup.
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']

	u = UserHandle(name, password, email)
	result = u.AddNewUser()

        if result == "success":
            return "Success! YAY!"
            #TODO: go to new user page
        else:
            return render_template('error.html', error=result)
    else:
        form = forms.SignUp()
        return render_template('signup.html', form=form)

@s_app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
	return "foobar"
        #TODO: go to existing user page
    else:
        form = forms.SignIn()
        return render_template('signin.html', form=form)


@s_app.route('/error', methods=['POST', 'GET'])
def error(error):
    return render_template('error.html', form=form)


print(s_app.instance_path)
import sys
print(sys.version_info)
