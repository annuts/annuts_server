from __future__ import absolute_import
#coding:utf-8
__author__ = 'zhangdewei'

import os

from celery import Celery

import platform

aws_hosts = [
    'iZ28hezih7iZ'
]
host = platform.uname()[1]

# set the default Django settings module for the 'celery' program.
if host in aws_hosts:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'annuts_server.settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'annuts_server.local_config')

from django.conf import settings

app = Celery('annuts_server')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))