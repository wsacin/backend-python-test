from alayatodo import app
from alayatodo.models import Todo
from alayatodo.helpers import login_required, render_template_or_json
from flask_paginate import Pagination, get_page_parameter
from alayatodo.forms import LoginForm
from alayatodo import db
from flask import (
    redirect,
    render_template,
    request,
    session,
    flash,
    )


PER_PAGE = 5


@app.route('/')
def home():
    with app.open_resource('../README.md', mode='r') as f:
        readme = "".join(l.decode('utf-8') for l in f)
        return render_template('index.html', readme=readme)


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_POST():
    form = LoginForm(request.form)
    if form.validate() and form.user:
        session['user'] = form.user.get_security_payload()
        session['logged_in'] = True
        flash('Login successfully', 'success')
        return redirect('/todo')
    flash('Incorrect username or password.', 'error')
    return redirect('/login')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user', None)
    return redirect('/')


@app.route('/todo/<id>/json', methods=['GET'])
@app.route('/todo/<id>', methods=['GET'])
@login_required
def todo(id):
    todo = Todo.query.filter_by(id=id, user_id=session['user']['id']).first()
    return render_template_or_json('todo.html',
                                   request.url_rule,
                                   todo=todo)


@app.route('/todo', strict_slashes=False, methods=['GET'])
@login_required
def todos():
    page = request.args.get(get_page_parameter(), type=int, default=1) - 1
    todos = Todo.query.filter_by(user_id=session['user']['id'])
    pagination = Pagination(page=page,
                            total=todos.count(),
                            search=False,
                            per_page=5,
                            record_name='todos')
    begin = PER_PAGE * page
    end = PER_PAGE * page + PER_PAGE

    return render_template(
            'todos.html',
            todos=todos[begin:end],
            pagination=pagination,
            current_page=page+1,
            page_items=[begin, end])


@app.route('/todo/<id>', methods=['PUT'])
@login_required
def todos_update(id):
    todo = Todo.query.filter_by(id=id, user_id=session['user']['id']).first()
    done = request.form['done']
    todo.done = not todo.done if done else todo.done
    db.session.add(todo)
    db.session.commit()
    return render_template('todo.html', todo=todo)


@app.route('/todo', strict_slashes=False, methods=['POST'])
@login_required
def todos_POST():
    description = request.form['description']

    if not description:
        flash('TODOs must have a description!', 'error')
    else:
        todo = Todo(user_id=session['user']['id'],
                    description=description)
        db.session.add(todo)
        db.session.commit()
        flash('TODO created!', 'success')
    return redirect('/todo')


@app.route('/todo/<id>', methods=['POST'])
@login_required
def todo_delete(id):
    todo = Todo.query.filter_by(id=id, user_id=session['user']['id']).first()
    db.session.delete(todo)
    db.session.commit()
    flash('TODO deleted!', 'success')
    return redirect('/todo')
