from models import db

class Todo(db.Model):
    __tablename__ = 'todo-list'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Todo {self.id}: {self.title}"

    def to_dict(self):   # converting todo to dictionary to return json
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }