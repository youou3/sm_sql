from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
# 大部分扩展都需要执行一个“初始化”操作。你需要导入扩展类，实例化并传入 Flask 程序实例
# 初始化扩展，传入程序实例 app
db = SQLAlchemy(app)


