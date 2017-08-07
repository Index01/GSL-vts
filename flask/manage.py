#~*~ Coding: utf-8 ~*~
#!/usr/bin/env python



from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
#from config import app, db
import config

migrate = Migrate(config.app, config.db)
manager = Manager(config.app)


manager.add_command('db', MigrateCommand)


if __name__=='__main__':
     manager.run()


