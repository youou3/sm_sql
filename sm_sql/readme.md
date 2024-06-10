# 导入数据库中的表到django里，执行下边的命令，该命令的意思是将对应数据库的表自动生成到models.py文件中。
python manage.py inspectdb > models.py

# 将django与数据库进行同步，可以进行增删改查操作。
python manage.py migrate

# 后续通知Django的【app name】的模型有变更
python manage.py makemigrtions [app name] # e.g.: app1
python manage.py migrate [app name] # e.g.: app1
