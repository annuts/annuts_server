#coding:utf-8
__author__ = 'zhangdewei'

from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import (login, authenticate, logout)
from django.shortcuts import redirect

from django.http import Http404

from dashboard.atauth.decorators import (perm, is_superuser, login_required)

class Base(View):
    TEMPLATE = 'dashboard/base.html'
    # @perm(perm_codename='all_publish')
    @login_required
    @is_superuser
    def get(self, request):

        return render(request, self.TEMPLATE, {})


class Login(View):
    TEMPLATE = 'dashboard/login.html'

    def get(self, request):

        return render(request, self.TEMPLATE, {})

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(username=username, password=password)
        if user is (None and not user.is_active and not user.is_superuser):
            raise Http404
        else:
            login(request, user)
            return redirect('/dashboard/')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/dashboard/login/')