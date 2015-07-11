#coding:utf-8
__author__ = 'zhangdewei'

from django.views.generic import View
from django.shortcuts import render

class Base(View):
    TEMPLATE = 'dashboard/test.html'

    def get(self, request):

        return render(request, self.TEMPLATE, {})