from alayatodo import app
from alayatodo.models import User, Todo
from alayatodo.database import db_session
from alayatodo.helpers import login_required, render_template_or_json
from flask import (
    redirect,
    render_template,
    request,
    session,
    flash,
    )


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
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username,
                                password=password).first()
    if user:
        session['user'] = {'id': user.id,
                           'username': username}
        session['logged_in'] = True
        return redirect('/todo')
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
    todo = Todo.query.get(id)
    return render_template_or_json('todo.html',  request.url_rule, todo=todo)


@app.route('/todo', strict_slashes=False, methods=['GET'])
@login_required
def todos():
    todos = Todo.query.all()
    return render_template('todos.html', todos=todos)


@app.route('/todo/<id>', methods=['PUT'])
@login_required
def todos_update(id):
    todo = Todo.query.get(id)
    done = request.form['done']
    todo.done = not todo.done if done else todo.done
    db_session.add(todo)
    db_session.commit()
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
        db_session.add(todo)
        db_session.commit()
        flash('TODO created!', 'success')
    return redirect('/todo')


@app.route('/todo/<id>', methods=['POST'])
@login_required
def todo_delete(id):
    todo = Todo.query.get(id)
    db_session.delete(todo)
    db_session.commit()
    flash('TODO deleted!', 'success')
    return redirect('/todo')
