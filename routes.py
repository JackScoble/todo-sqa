from flask import render_template, request, redirect, url_for
from datetime import datetime
from extensions import db
from models import Task


def index():
    total = Task.query.count()
    completed = Task.query.filter_by(completed=True).count()
    pending = total - completed
    return render_template('index.html', active='home', total=total, completed=completed, pending=pending, year=datetime.utcnow().year)


def all_tasks():
    items = Task.query.order_by(Task.id).all()
    return render_template('tasks.html', active='tasks', tasks=items, year=datetime.utcnow().year)


def task_detail(task_id):
    t = Task.query.get(task_id)
    if not t:
        return render_template('task_detail.html', active='tasks', task=None, year=datetime.utcnow().year), 404
    return render_template('task_detail.html', active='tasks', task=t, year=datetime.utcnow().year)


def edit_task(task_id):
    t = Task.query.get(task_id)
    if not t:
        return redirect(url_for('all_tasks')), 404

    if request.method == 'POST':
        title = request.form.get('title')
        deadline = request.form.get('deadline')
        importance = request.form.get('importance', '3')
        if title:
            t.title = title
            t.deadline = datetime.strptime(deadline, '%Y-%m-%d').date() if deadline else None
            t.importance = int(importance)
            db.session.commit()
            return redirect(url_for('task_detail', task_id=task_id))
        else:
            return render_template('edit_task.html', active='tasks', task=t, error='Title required', year=datetime.utcnow().year), 400

    return render_template('edit_task.html', active='tasks', task=t, year=datetime.utcnow().year)


def toggle_complete(task_id):
    t = Task.query.get(task_id)
    if t:
        t.completed = not t.completed
        db.session.commit()
    return redirect(request.referrer or url_for('all_tasks'))


def create_task():
    if request.method == 'POST':
        title = request.form.get('title')
        deadline = request.form.get('deadline')
        importance = request.form.get('importance', '3')
        if title:
            task = Task(
                title=title,
                completed=False,
                deadline=datetime.strptime(deadline, '%Y-%m-%d').date() if deadline else None,
                importance=int(importance),
            )
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('all_tasks'))
        else:
            return render_template('new_task.html', active='create', error='Title required', year=datetime.utcnow().year), 400
    return render_template('new_task.html', active='create', year=datetime.utcnow().year)


def about():
    return render_template('about.html', active='about', year=datetime.utcnow().year)


def register_routes(app):
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/tasks', 'all_tasks', all_tasks)
    app.add_url_rule('/task/<int:task_id>', 'task_detail', task_detail)
    app.add_url_rule('/task/<int:task_id>/edit', 'edit_task', edit_task, methods=['GET', 'POST'])
    app.add_url_rule('/task/<int:task_id>/toggle-complete', 'toggle_complete', toggle_complete)
    app.add_url_rule('/new-task', 'create_task', create_task, methods=['GET', 'POST'])
    app.add_url_rule('/about', 'about', about)
