# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import include, re_path


admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^news/', include('website.news.urls'))
]
