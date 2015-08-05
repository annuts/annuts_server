#coding:utf-8
__author__ = 'zhangdewei'
"""
  这里用来开发关于dashboard的各种权限的装饰器
"""

from django.shortcuts import redirect
from django.http import Http404
from django.conf import settings


def perm(**kwargs):  # 该装饰器用于验证该用户是否有访问某个页面的权限
    def get_func(func):
        def wrapped_func(request, *args):
            if not (request.request.user.is_authenticated() or
                        kwargs.get('perm_codename') or
                        request.request.user.is_superuser):
                raise Http404
            user = request.request.user

            permissions = [i.codename for i in user.user_permissions.all()]

            if kwargs['perm_codename'] not in permissions:
                raise Http404
            else:
                return func(request, *args)
        return wrapped_func
    return get_func

def is_superuser(func):  # 单纯的验证是否是超级用户（员工）
    def wrapped_func(request, *args):
        if not (request.request.user.is_authenticated() or request.request.user.is_superuser):
            raise Http404
        return func(request, *args)
    return wrapped_func

def login_required(func):
    def wrapped_func(request, *args):
        if not request.request.user.is_authenticated():
            return redirect(settings.LOGIN_DASHBOARD_URL)
        return func(request, *args)
    return wrapped_func