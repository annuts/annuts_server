#coding:utf-8
__author__ = 'zhangdewei'

from django.http import HttpResponse
from django.views.generic import View
from django.middleware.csrf import get_token
from django.core import serializers

import json

class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self, obj='', json_opts={}, mimetype="application/json", *args, **kwargs):
        content = json.dumps(obj,  **json_opts)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)

class BaseView(View):
    def _init_data(self, request):
        data = {
            'csrf_token': get_token(request),
            'user':{
                'is_auth': request.user.is_authenticated(),  # 验证是否登陆
                'username': request.user.username,  # 用户名
                'avatar':  '',  # 头像，
                'gender': 0,  # 性别
                'city': '',  # 城市
                'community': ''  # 小区
            }
        }

        if data['user']['is_auth']:  # 只有登陆才能获取 否则会报错
            data['user']['avatar'] = request.user.userprofile.avatar
            data['user']['gender'] = request.user.userprofile.gender
            if request.user.userprofile.city:
                data['user']['city'] = request.user.userprofile.city.name
                data['user']['community'] = request.user.userprofile.community.name

        return data

def obj_serializers(model_obj, muti=False, type='json'):  # django的model对象转成json形式,muti代表model_obj是单个多想还是多个
    if muti == True:
        data = serializers.serialize(type, model_obj)
        return json.loads(data)
    else:
        data = serializers.serialize(type, [model_obj])
        return json.loads(data)[0]