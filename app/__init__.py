from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

app = Flask(__name__)
csrf = CSRFProtect(app)

# bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:password@localhost/project2db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

UPLOAD_FOLDER ='./app/static/uploads'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views, models