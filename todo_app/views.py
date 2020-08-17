from flask import render_template
from todo_app import app

@app.route("/")
def top():
    return render_template("top.html")

@app.route("/list")
def show_list():
    todo_list = ["歯を磨く", "結婚する", "大根を買う", "ピザと頼む"]
    return render_template("list.html", todo_list=todo_list)

@app.route("/edit")
def edit():
    pass

@app.route("/delete")
def delete():
    pass

@app.route("/add")
def add():
    pass
