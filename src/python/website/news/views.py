# -*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView
from website.news.models import Post


class PostsListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
