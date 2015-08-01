#coding:utf-8
__author__ = 'zhangdewei'

import os
import sys

from settings import *

import sys
reload(sys)
sys.setdefaultencoding('utf8')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'annuts',
	'USER': 'root',
	'PASSWORD': '',
	'HOST': 'localhost',
	'PORT': '3306'
    }
}

# mongodb
MONGDO_HOST = '192.168.33.10'
MONGDO_PORT = 27017