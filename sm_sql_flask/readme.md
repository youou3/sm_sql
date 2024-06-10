# 当根目录下存在app.py文件时，可以直接运行flask命令启动服务：
flask run

# 或者，可以指定运行的端口：
flask run --port=5000

# 或者，可以指定运行的主机和端口：
flask run --host=0.0.0.0 --port=5000

# 或者，可以指定运行的模式：
flask run --debug

# 或者，可以指定运行的环境：
flask run --env=production

# 或者，可以指定运行的配置文件：
flask run --config=config.py

# 或者，可以指定运行的日志文件：
flask run --log-file=error.log

# 或者，可以指定运行的访问日志文件：
flask run --access-log-file=access.log

# 或者，可以指定运行的应用上下文：
flask run --app=my_app

# 或者，可以指定运行的服务器：
flask run --server=gevent

# 或者，可以指定运行的进程数：
flask run --processes=4

# 或者，可以指定运行的线程数：
flask run --threads=2

# 或者，可以指定运行的秘钥：
flask run --key=my_secret_key

# 或者，可以指定运行的SSL证书：
flask run --cert=my_ssl.crt --key=my_ssl.key

# 设置系统环境变量 FLASK_APP=app.py 后，可以直接运行 flask 命令启动服务：
export FLASK_APP=app1.py
flask run

# 当 python-dotenv 安装后，Flask 会从项目根目录的 .flaskenv 和 .env 文件读取环境变量并设置。我们分别使用文本编辑器创建这两个文件，或是使用更方便的 touch 命令创建（注意不要漏掉文件名开头的点）：
touch .env .flaskenv

# .flaskenv 用来存储 Flask 命令行系统相关的公开环境变量；而 .env 则用来存储敏感数据，不应该提交进 Git 仓库，我们把文件名 .env 添加到 .gitignore 文件的结尾（新建一行）来让 Git 忽略它。你可以使用编辑器打开这个文件，然后添加下面这一行内容：
.env
# 在新创建的 .flaskenv 文件里，我们写入一行 FLASK_DEBUG=1，将环境变量 FLASK_DEBUG 的值设为 1，以便开启调试模式：
# .flaskenv 文件
FLASK_DEBUG=1
# 顺便说一句，如果你安装的 Flask 版本是 2.3 或更高版本，则可以直接使用 --debug 命令行选项来开启调试模式，即：
flask run --debug
<!-- https://tutorial.helloflask.com/database/ -->
