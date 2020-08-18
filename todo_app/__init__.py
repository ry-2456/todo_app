from flask import Flask
# from flaskext.mysql import MySQL
from flask_mysqldb import MySQL

app = Flask(__name__)

# 設定の読み込み
app.config.from_object("todo_app.config")

# MySQLオブジェクト生成
mysql = MySQL()
mysql.init_app(app)

from todo_app import views
