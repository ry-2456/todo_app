from flask import render_template, request, redirect, url_for
from todo_app import app, db
from todo_app.models import Task

@app.route("/")
def top():
    return render_template("top.html")

@app.route("/list")
def show_list():
    """タスク一覧"""
    tasks = Task.query.all()
    return render_template("list.html", tasks=tasks)

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):

    if request.method == "GET":
        task = Task.query.filter_by(id=task_id).first()
        return render_template("edit_task.html", task_edited=task)

    elif request.method == "POST":
        content_edited = request.form["content_edited"] 
        task = Task.query.filter_by(id=task_id).first()
        task.content = content_edited
        db.session.commit()
        
        return redirect(url_for("show_list"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    task_to_delete = Task.query.filter_by(id=task_id).first()
    db.session.delete(task_to_delete)
    db.session.commit()

    return redirect(url_for("show_list"))

@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "GET":
        return render_template("add_task.html")

    if request.method == "POST":
        task = Task(content=request.form["task_todo"])
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("show_list"))
