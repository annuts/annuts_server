__author__ = 'zhangdewei'

import jpush as jpush
from annuts_server import celery_app

@celery_app.task(bind=True)
def add(self, x, y):
    return x + y

@celery_app.task(bind=True)
def push_message(**kwargs):
    if not kwargs.get('ios_content') and not kwargs.get('android_content'):
        print 'no message'
        return False
    jpush = jpush.JPush(settings.JPUSH_APP_KEY, settings.JPUSH_MASTER_SECRET)

    push = _jpush.create_push()
    push.audience = jpush.all_
    ios_msg = jpush.ios(alert=kwargs.get('ios_content'), badge="+1", extras={'k1':'v1'}, sound_disable=True)
    android_msg = jpush.android(alert=kwargs.get('android_content'))
    push.notification = jpush.notification(alert=kwargs.get('title'), android=android_msg, ios=ios_msg)
    push.platform = jpush.all_
    push.send()

@celery_app.task(bind=True)
def test(self, a):
    print a
    return a