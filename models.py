from datetime import date
from extensions import db


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    deadline = db.Column(db.Date, nullable=True)
    importance = db.Column(db.Integer, nullable=False, default=3)
    created_date = db.Column(db.Date, nullable=False, default=date.today)

    def __repr__(self):
        return f"<Task {self.id} {self.title!r}>"
