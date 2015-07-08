#coding:utf-8
__author__ = 'zhangdewei'

from annuts_app.models import City
from annuts_app.common.base_utils import obj_serializers
from rest_framework.response import Response

from rest_framework.views import APIView


class TestCity(APIView):
    def get(self, request):
        return Response({'method': 'get'})

    def post(self, request):
        return Response({'method': 'post'})

    def put(self, request):
        return Response({'method': 'put'})

    def delete(self, request):
        return Response({'method': 'delete'})