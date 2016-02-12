import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

# Creates an object called app of Flask class
app = Flask(__name__)
app.config.from_object('config')

# Imports app package from views, not the same as object 'app'
from app import views, models

# for database
db = SQLAlchemy(app)

# for login
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
