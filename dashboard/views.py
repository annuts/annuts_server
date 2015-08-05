#coding:utf-8
__author__ = 'zhangdewei'

from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from dashboard.atauth.decorators import perm, is_superuser

class Base(View):
    TEMPLATE = 'dashboard/base.html'
    # @perm(perm_codename='all_publish')
    @is_superuser
    def get(self, request):

        return render(request, self.TEMPLATE, {})