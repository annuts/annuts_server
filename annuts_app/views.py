#coding:utf-8
from django.shortcuts import render
from django.contrib.auth.models import User
from common.base_utils import JSONResponse, BaseView

import json

class Test(BaseView):
    def get(self, request):
        data = self._init_data(request)
        data['name'] = 'dewei'
        data['method'] = 'get'
        print data
        return JSONResponse(data)

    def post(self, request):  # 需要 csrf_token 以后前端在BaseView中data里已经将csrf_token发送给了前端，通过他进行post请求
        return JSONResponse({'method': 'post'})

    def delete(self, request):
        return JSONResponse({'method': 'delete'})