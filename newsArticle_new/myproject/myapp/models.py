from email.mime import image
from email.policy import default
from enum import auto
from time import timezone
from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    is_author = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

class NewsArticles(models.Model):
    news_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    headline = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    mainbody = models.CharField(max_length=200)
    # image = models.ImageField()
    author = models.CharField(max_length=50)
    locality = models.CharField(max_length=30)
    like = models.CharField(max_length=20)
    comment = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)

class Like(models.Model):
    news_id = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)


class Locality(models.Model):
    locality_name = models.CharField(max_length=200)
    user_role_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class userRole(models.Model):
    user_role_id = models.AutoField(primary_key=True)
    user_role = models.CharField(max_length=200)
    
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=250)
    