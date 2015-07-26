#coding:utf-8
__author__ = 'zhangdewei'

"""
Manage redis connections
"""
import redis
import pickle
from django.conf import settings

def python_get(self, key):
    value = self.get(key)
    return pickle.loads(value) if value else value

def python_set(self, key, value, timeout=None):
    value = pickle.dumps(value)
    if not timeout:
        return self.set(key, value)
    else:
        return self.setex(key, timeout, value)

redis.StrictRedis.python_get = python_get
redis.StrictRedis.python_set = python_set

redisdb_0 = redis.StrictRedis(
    db=settings.REDIS_DEFAULT_DB,
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
)


redisdb = redisdb_0