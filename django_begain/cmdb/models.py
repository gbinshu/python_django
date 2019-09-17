# Terminal 中使用python manage.py makemigrations创建,接下来使用python manage.py migrate
from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)