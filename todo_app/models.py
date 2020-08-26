from todo_app import db

class Task(db.Model):
   __tablename__ = "task"

   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   content = db.Column(db.String(50), nullable=False)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))

def init():
    db.create_all()
