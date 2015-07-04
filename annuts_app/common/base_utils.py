#coding:utf-8
__author__ = 'zhangdewei'

from django.http import HttpResponse
from django.views.generic import View
from django.middleware.csrf import get_token

import json

class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self, obj='', json_opts={}, mimetype="application/json", *args, **kwargs):
        content = json.dumps(obj,  **json_opts)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)

class BaseView(View):
    def _init_data(self, request):
        data = {
            'csrf_token': get_token(request)
        }
        return data