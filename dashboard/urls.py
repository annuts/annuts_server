#coding:utf-8
__author__ = 'zhangdewei'

from django.conf.urls import patterns, include, url
from django.conf import  settings

from dashboard import views as dashboard_views

urlpatterns = [
    url(r'^$', dashboard_views.Base.as_view()),
    url(r'^login/$', dashboard_views.Login.as_view()),
    url(r'^logout/$', dashboard_views.Logout.as_view()),
]
