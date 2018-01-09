from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CSRFProtect
from flask_script import Manager
from settings import *


app = Flask(__name__)
app.config.from_object(__name__)

csrf = CSRFProtect(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

import alayatodo.views
