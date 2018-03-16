# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

CATEGORIES = (
    ('World', 'World'),
    ('Russia', 'Russia'),
    ('Economics', 'Economics'),
    ('Sport', 'Sport')
)

AUTHORS = (
    ('kvendingoldo', 'kvendingoldo'),
    ('admin', 'admin')
)


class Post(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    announcement = models.CharField(max_length=250)
    body = models.TextField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/news/%i/" % self.id


class Comment(models.Model):
    news = models.ForeignKey(Post, on_delete=models.PROTECT)
    username = models.CharField(max_length=70)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
