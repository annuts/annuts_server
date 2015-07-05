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
	'PASSWORD': 'dewei',
	'HOST': 'localhost',
	'PORT': '3306'
    }
}

