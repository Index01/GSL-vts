from flask import Flask
from flask_iniconfig import INIConfig
from flask_sqlalchemy import SQLAlchemy

from ConfigParser import SafeConfigParser, NoSectionError

app = Flask(__name__)


parser = SafeConfigParser()
parser.read('../gateConfigs.ini')


app.config['Testing'] = True
app.config['DEBUG'] = True
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = "super-generic-string"
#app.config['SERVER_NAME'] = parser.get('Flask', 'SERVER_NAME')
#print parser.get('Flask', 'SERVER_NAME')
app.config['SQLALCHEMY_DATABASE_URI'] = parser.get('PostgresConfigs', 'URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']=parser.get('PostgresConfigs', 'URL')
#SERVER_NAME = "127.0.0.1:3000"

print parser.get('PostgresConfigs', 'URL')

db = SQLAlchemy(app)
