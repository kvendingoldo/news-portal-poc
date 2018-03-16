# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth import get_user_model
from website.news.models import Post


class PostAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['queryset'] = get_user_model().objects.filter(username=request.user.username)
        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ('author',)
        return self.readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data['author'] = request.user
        request.GET = data
        return super(PostAdmin, self).add_view(request, form_url="", extra_context=extra_context)


admin.site.register(Post, PostAdmin)
