import os

# MySQLの設定
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = os.environ["MYSQL_ROOT_PASSWD"]
MYSQL_DB = "flask_todo_app"

SQLALCHEMY_DATABASE_URI = "mysql://{username}:{password}@{host}/{db_name}".\
            format(username=MYSQL_USER, 
                   password=MYSQL_PASSWORD, 
                   host=MYSQL_HOST, 
                   db_name=MYSQL_DB)
