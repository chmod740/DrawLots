from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    user_type = models.IntegerField()
    user_group = models.IntegerField()

class Draw(models.Model):
    title = models.CharField(max_length=100)
    data = models.CharField(max_length=200)
    user_group = models.IntegerField()
    add_time = models.DateTimeField(auto_now=True)

class DrawResult(models.Model):
    draw = models.ForeignKey(Draw)
    user = models.ForeignKey(User)
    result = models.IntegerField()
    add_time = models.DateTimeField(auto_now=True)



