#coding:utf-8

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.CharField(max_length=255)  # 七牛头像
    gender = models.SmallIntegerField(default=0)  # 性别0，1:男，2:女
    birthday = models.DateField(blank=True, null=True)
    is_company = models.SmallIntegerField(default=0)  # 是否是员工  默认0,员工1，物业2
    city = models.ForeignKey('City', related_name='user_city', null=True)
    community = models.ForeignKey('Community', related_name='user_community', null=True)
    
    def __unicode__(self):
        return self.user

class City(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    
    def __unicode__(self):
	return self.name

class Community(models.Model):
    city = models.ForeignKey('City', related_name='city_community')
    name = models.CharField(max_length=50, db_index=True)

    def __unicode__(self):
	return self.name
