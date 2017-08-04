#forms.py

from wtforms import *
from wtforms.validators import DataRequired

class SignUp(Form): 
    name = TextField("Name", validators=[DataRequired()])
    email = TextField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class SignIn(Form):
    email = TextField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class Edit(Form):
    about = TextField("About:", validators=[DataRequired()])
    research = TextField("Research:", validators=[DataRequired()])
    submit = SubmitField("Submit")

class Search(Form):
    query = TextField("Search", validators=[DataRequired()])
    submit = SubmitField("Submit")
