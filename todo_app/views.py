from flask import render_template
from todo_app import app

@app.route("/")
def top():
    return render_template("top.html")
