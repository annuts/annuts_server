#coding:utf-8
__author__ = 'zhangdewei'

from django.conf.urls import patterns, include, url
from django.conf import  settings

from annuts_app.dashboard import views

urlpatterns = [
    url(r'^base/$', views.Base.as_view())
]