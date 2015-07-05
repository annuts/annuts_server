# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annuts_app', '0002_auto_20150704_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.ForeignKey(related_name='user_city', to='annuts_app.City', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='community',
            field=models.ForeignKey(related_name='user_community', to='annuts_app.Community', null=True),
        ),
    ]
