import os

# MySQLの設定
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = os.environ["MYSQL_ROOT_PASSWD"]
MYSQL_DB = "flask_todo_app"
