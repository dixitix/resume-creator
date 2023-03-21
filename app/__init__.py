import sqlite3
import os
from flask import Flask, render_template, request, g

# конфигурация
DATABASE = '/tmp/flaskr.db' 
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin' 
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path,'flaskr.db')))

from app import routes
