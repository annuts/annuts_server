#coding:utf-8
__author__ = 'zhangdewei'

from django.conf.urls import patterns, include, url
from django.conf import  settings

from annuts_app import views as annuts_view

urlpatterns = [
    url(r'^test/$', annuts_view.Test.as_view())
]