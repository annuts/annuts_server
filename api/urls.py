#coding:utf-8
__author__ = 'zhangdewei'

from django.conf.urls import patterns, url, include
from api import views as API_VIEWS

from annuts_app.models import City

urlpatterns = [
    url(r'^citys/$', API_VIEWS.TestCity.as_view())
]
