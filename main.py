"""AlayaNotes

Usage:
  main.py runserver
  main.py db initdb
  main.py db migrate
  main.py db upgrade
"""
from alayatodo import manager, db
from alayatodo.models import User, Todo




if __name__ == '__main__':
    manager.run()
