from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
    )
from flask import jsonify
from sqlalchemy.orm import relationship
from alayatodo.database import Base


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(255), unique=True)
    todos = relationship('Todo')

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)

    @property
    def jsonified(self):
        return jsonify(id=self.id, username=self.username)


class Todo(Base):

    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String(255), unique=True)
    done = Column(Boolean, default=False)

    def __init__(self, user_id=None, description=None):
        self.user_id = user_id
        self.description = description
        self.done = False

    def __repr__(self):
        return '<Todo(user: {}) {}>'.format(self.user_id, self.description)

    @property
    def jsonified(self):
        return jsonify(id=self.id,
                       done=self.done,
                       description=self.description)
