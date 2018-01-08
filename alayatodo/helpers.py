from functools import wraps
from flask import session, redirect, render_template


def render_template_or_json(template, url_path, **kwargs):
    """
    Method for responding with JSONified object
    for rules that end with /json
    """
    for key, value in kwargs.items():
        if value is None:
            return render_template('404.html'), 404
        elif url_path.rule.split('/')[-1] == 'json':
            return value.jsonified
    return render_template(template, **kwargs)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function
