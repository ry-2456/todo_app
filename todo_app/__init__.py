import os
from flask import Flask
# from flaskext.mysql import MySQL
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL接続設定
mysql = MySQL()
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = os.environ["MYSQL_ROOT_PASSWD"]
app.config["MYSQL_DB"] = "flask_todo_app"
mysql.init_app(app)


from todo_app import views
