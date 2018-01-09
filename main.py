"""AlayaNotes

Usage:
  main.py runserver
  main.py db initdb
  main.py db migrate
  main.py db upgrade
"""
from alayatodo import manager, db
from alayatodo.models import User, Todo
from alayatodo.fixtures import fixtures


@manager.command
def load_fixtures():
    models = {'User': User, 'Todo': Todo}
    for key, values in fixtures.items():
        for value in values:
            db.session.add(models[key](*value))
            db.session.commit()


if __name__ == '__main__':
    manager.run()
