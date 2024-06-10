# sm_sql
# 创建一个django项目
django-admin startproject myproject
# 创建一个app
python manage.py startapp myapp
# 创建数据库
python manage.py migrate
# 创建超级用户
python manage.py createsuperuser
# 运行服务器
python manage.py runserver
# 打开浏览器，输入http://localhost:8000/admin/，登录系统
# 创建模型
python manage.py makemigrations
python manage.py migrate
# 定义模型
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)     
