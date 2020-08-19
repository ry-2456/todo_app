from flask import render_template, request, redirect, url_for
from todo_app import app, mysql

@app.route("/")
def top():
    return render_template("top.html")

@app.route("/list")
def show_list():
    """タスク一覧"""
    with mysql.connection.cursor() as cur:
        sql = "SELECT * FROM task"
        cur.execute(sql)
        # mysql.connection.commit() # delete, update, insertの場合のみ
        task_list = cur.fetchall()
        task_list = map(lambda row:
            {"id":row[0], "content":row[1]}, task_list)

    # cur = mysql.connection.cursor()
    # sql = "SELECT * FROM task"
    # cur.execute(sql)
    # # mysql.connection.commit()
    # todo_list = cur.fetchall()
    # todo_list = [row[1] for row in todo_list]
    # cur.close()

    return render_template("list.html", task_list=task_list)

@app.route("/edit")
def edit_task():
    pass

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    with mysql.connection.cursor() as cur:
        sql = "DELETE FROM task WHERE id={}".format(task_id)
        cur.execute(sql)
        mysql.connection.commit() 

    return redirect(url_for("show_list"))

@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "GET":
        return render_template("add_task.html")

    if request.method == "POST":
        task_todo = request.form["task_todo"] 

        with mysql.connection.cursor() as cur:
            sql = "INSERT INTO task (todo) VALUES ('{}')".format(task_todo)
            cur.execute(sql)
            mysql.connection.commit()

        return redirect(url_for("show_list"))
