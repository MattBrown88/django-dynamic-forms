# -*- coding: utf-8 -*-

from django.urls import path, re_path

from .views import data_set_detail

urlpatterns = [
    re_path(r'show/(?P<display_key>[a-zA-Z0-9]{24})/$', data_set_detail,
        name='data-set-detail'),
]
