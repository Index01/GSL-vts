from flask import Flask
from flask.ext.iniconfig import INIConfig
import config

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')


