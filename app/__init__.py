from flask import Flask

# Creates an object called app of Flask class
app = Flask(__name__)
# Imports app package from views, not the same as object 'app'
from app import views
