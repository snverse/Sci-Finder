#forms.py

from flask.ext.wtf import forms
from wtforms import StringField
from wtforms.validators import DataRequired

class SignUp(Form): 
	'''Inherits from Form. Responsibe for handling
	new users signing up for the first time.'''
	new_user = StringField('First_name', validators=[DataRequired()])
