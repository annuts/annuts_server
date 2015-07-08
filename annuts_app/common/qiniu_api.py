#coding:utf-8
__author__ = 'zhangdewei'

from qiniu import auth, put_data
from django.conf import settings

access_key = settings.QINIU_ACCESS_KEY
secret_key = settings.QINIU_SECRET_KEY

bucket_name = 'annuts'
qiniu_base_url = 'http://7xk6ym.com1.z0.glb.clouddn.com/'  # 基础url

qiniu_object = auth.Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)

def push_qiniu_with_server(BucketName, file_name, data, mine_type):
    token = qiniu_object.upload_token(BucketName, file_name)
    ret, info = put_data(token, file_name, data, mime_type=mine_type, check_crc=True)
    ret["url"] = qiniu_base_url + file_name
    assert ret["key"] == file_name
    return ret

def delete_image(file_name):
    if file_name.startswith(qiniu_base_url):
        file_name = file_name.replace(qiniu_base_url, '')
    print file_name
    bucket = BucketManager(qiniu_object)
    ret, info = bucket.delete(BucketName, file_name)
    return info


if __name__ == "__main__":
    f = open('/Users/zhangdewei/dewei/0.png', 'rb')
    image = push_qiniu_with_server(bucket_name, '0.png', f.read(), MIMETYPE.image)
    print image