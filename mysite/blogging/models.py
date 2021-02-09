from django.db import models
from django.db.models import CharField, TextField, DateTimeField, ForeignKey
from django.contrib.auth.models import User


class Post(models.Model):

    title = CharField(max_length=150)
    text = TextField(blank=True)
    author = ForeignKey(User, on_delete=models.CASCADE)
    created_date = DateTimeField(auto_now_add=True)
    modified_date = DateTimeField(auto_now=True)
    published_date = DateTimeField(blank=True, null=True)
