#coding:utf-8
__author__ = 'zhangdewei'

from django.conf.urls import patterns, include, url
from django.conf import  settings

from dashboard import views as dashboard_views

urlpatterns = [
    url(r'^base/$', dashboard_views.Base.as_view())
]
