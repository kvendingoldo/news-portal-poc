# -*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView
from website.news.models import Post


class PostsListView(ListView):
    model = Post
    queryset = Post.objects.order_by('-date')
    paginate_by = 10

    def get_queryset(self):
        """Filter by tag if it is provided in GET parameters"""
        queryset = super(PostsListView, self).get_queryset()
        if 'tag' in self.request.GET:
            queryset = queryset.filter(category=self.request.GET['tag'])
        return queryset


class PostDetailView(DetailView):
    model = Post
