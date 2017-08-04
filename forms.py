#forms.py

from wtforms import *
from wtforms.validators import DataRequired

class SignUp(Form): 
	'''Inherits from Form. Responsibe for handling
	new users signing up for the first time.'''
	name = TextField("Name", validators=[DataRequired()])
	email = TextField("Email", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Submit")
