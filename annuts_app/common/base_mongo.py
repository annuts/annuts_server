#coding:utf-8
__author__ = 'zhangdewei'

from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.MONGDO_HOST, settings.MONGO_PORT)

mongodb_test = client['test']