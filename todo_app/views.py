from flask import render_template
from todo_app import app, mysql

@app.route("/")
def top():
    return render_template("top.html")

@app.route("/list")
def show_list():
    cur = mysql.connection.cursor()
    sql = "SELECT * FROM task"
    cur.execute(sql)
    # mysql.connection.commit()
    todo_list = cur.fetchall()
    todo_list = [row[1] for row in todo_list]
    cur.close()

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
