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
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    pw_hash = db.Column(db.String(255), unique=True)
    todos = relationship('Todo')

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_security_payload(self):
        return {
          'id': self.id,
          'username': self.username
        }

    @property
    def jsonified(self):
        return jsonify(id=self.id, username=self.username)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(
            password, method=app.config['PASSWORD_HASH_METHOD']
        )

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)


class Todo(db.Model):

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
