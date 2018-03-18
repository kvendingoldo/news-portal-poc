# -*- coding: utf-8 -*-

from django.urls import re_path
from django.views.generic import RedirectView
from website.news.views import PostsListView, PostDetailView


urlpatterns = [
    re_path(r'^$', PostsListView.as_view(), name='list'),
    re_path(r'^(?P<pk>\d+)/$', PostDetailView.as_view())
]

