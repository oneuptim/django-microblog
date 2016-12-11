from __future__ import unicode_literals
from django.db import models

# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField()
#     password = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now_add = True)
#
# class Message(models.Model):
#     message = models.TextField()
#     user_id = models.ForeignKey(User)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now_add = True)
#
# class Comment(models.Model):
#     comment = models.TextField()
#     user_id = models.ForeignKey(User)
#     message_id = models.ForeignKey(Message)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now_add = True)

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    blog = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    comment = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
