from flask import Flask
from flask_iniconfig import INIConfig
from ConfigParser import SafeConfigParser, NoSectionError


app = Flask(__name__)

parser = SafeConfigParser()
parser.read('../gateConfigs.ini')
"""
INIConfig(app)

with app.app_context():
    app.config.from_inifile('../gateConfigs.ini')
    print "[+]RUNNING FLASk CONFIG"

    app.config['SERVER_NAME'] = (app.config.get('Flask').get('SERVER_NAME'))
app.config['Testing'] = (app.config.get('Flask').get('testing'))
app.config['Debug'] = (app.config.get('Flask').get('debug'))

app.config['WTF_CSRF_ENABLED'] = (app.config.get('Flask').get('WTF_CSRF_ENABLED'))
app.config['SECRET_KEY'] = (app.config.get('Flask').get('SECRET_KEY'))
print app.config.get('Flask').get('SECRET_KEY')


"""
app.config['Testing'] = True
app.config['DEBUG'] = True
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = "blackShirts!"
#app.config['SERVER_NAME'] = parser.get('Flask', 'SERVER_NAME')
#print parser.get('Flask', 'SERVER_NAME')
app.config['SQLALCHEMY_DATABASE_URI'] = parser.get('PostgresConfigs', 'URL')

#SERVER_NAME = "127.0.0.1:3000"

