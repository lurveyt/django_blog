from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    # categories = models.ManyToManyField(Category, blank=True, related_name="posts")

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        """You may also have noticed that the admin links to the list of
        categories with the word "Categorys".
        Categorys? That looks funny.
        In blogging/models.py, add the following method to the Category class:"""
        verbose_name_plural = 'Categories'