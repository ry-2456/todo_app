from todo_app import db

class Task(db.Model):
   __tablename__ = "task"

   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   content = db.Column(db.String(50), nullable=False)

def init():
    db.create_all()
