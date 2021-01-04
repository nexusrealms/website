'''URL Patterns for Django

This module contains URL patterns for static pages.
'''

from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]
