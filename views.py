#views.py

import time
from __init__ import * # s_app, AddNewUser
from flask import *
from UserHandler import *
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
            info = u.GetUserInfo()
            info.PopulatePage("Stuff here", "Fill me in!")
            return edit(email, password)

        else:
            return render_template('error.html', error=result)
    else:
        form = forms.SignUp()
        return render_template('signup.html', form=form)

@s_app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
	email = request.form['email']
	password = request.form['password']

	if CheckLogin(email, password):
            return edit(email, password)

        time.sleep(3)
        return render_template('error.html', error="Username or password incorrect. Try again.")

    form = forms.SignIn()
    return render_template('signin.html', form=form)

@s_app.route('/userpage', methods=['POST', 'GET'])
def getuserpage():
    if request.method == 'POST':
        email = request.form['email']
        uid = RetrieveUserInfo(email).GetUid()
        return redirect('/userpage/%d' % (uid))
    else:
        form = forms.Search()
        return render_template('search.html', form=form)

@s_app.route('/userpage/<id>')
def userpage(id):
    u = RetrieveUserInfo(uid=id)
    data = u.GetPage()

    if data is None:
        return redirect('/userpage')

    research, about = data
    return render_template('userpage.html', research=research, about=about)

@s_app.route('/edit', methods=['POST', 'GET'])
def edit(email=None, password=None):
    if email is not None:
        form = forms.Edit()
        return render_template('edit.html', form=form, email=email, password=password)

    email = request.form['email']
    password = request.form['password']

    #double-check credentials, just to be sure
    if not CheckLogin(email, password):
        time.sleep(3)
        return render_template('error.html', error="You're not logged in!")

    research = request.form['research']
    about = request.form['about']
    info = RetrieveUserInfo(email)
    info.PopulatePage(research, about)
    uid = info.GetUid()

    return redirect("/userpage/%d" % (uid))

@s_app.route('/error', methods=['POST', 'GET'])
def error():
    return render_template('error.html')

def CheckLogin(email, password):
    return RetrieveUserInfo(email).CheckLogin(password)
