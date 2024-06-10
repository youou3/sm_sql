from flask import Flask

# 定义一个视图函数（请求处理函数）
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,World!'

@app.route('/hello')
def hello():
    return '<h1>Hello</h1>'
