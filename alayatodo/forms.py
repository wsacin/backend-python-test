# -*- coding: utf-8 -*-
from wtforms import (
    TextField,
    PasswordField,
    validators,
    ValidationError,
    Form
    )
from alayatodo.models import User


class LoginForm(Form):

    user = None

    username = TextField(label=u'Username',
                         validators=[validators.required()])

    password = PasswordField(label=u'Password',
                             validators=[validators.required()])

    def validate_username(form, field):
        username = field.data
        try:
            form.user = User.query.filter_by(username=username).first()
        except:
            raise ValidationError(u'Username not found.')

    def validate_password(form, field):
        password = field.data
        if form.user:
            if not form.user.check_password(password):
                raise ValidationError(u'Incorrect password.')
