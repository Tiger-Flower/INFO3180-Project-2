from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,PasswordField,TextAreaField
from wtforms.validators import DataRequired, Email, InputRequired

DEBUG = True
SECRET_KEY = 'secret'

# keys for localhost. Change as appropriate.

app = Flask(__name__)
app.config.from_object(__name__)

class Register(FlaskForm):
    username  = StringField('Username', validators=[DataRequired("Please enter a username")])
    password  = PasswordField('Password', validators=[DataRequired("Please enter your password")])
    firstname = StringField('First Name', validators=[DataRequired("Please enter your firstname")])
    lastname  = StringField('Last Name', validators=[DataRequired("Please enter your lastname")])
    email     = StringField('Email', validators=[DataRequired("Please enter your e-mail address"), Email()])
    location  = StringField('Location', validators=[DataRequired("Please enter your location")])
    biography = TextAreaField("Biography", validators=[DataRequired("Please enter a biography of yourself")])
    photo     = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Please enter a username")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password")])

class postForm(FlaskForm):
    image = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg','png'],'Image only!')])
    caption = TextAreaField('Caption', validators=[InputRequired()])  

if __name__ == "__main__":
    app.run()