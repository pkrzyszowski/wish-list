# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 14:35
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0004_auto_20161005_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='wish_points_increase',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 10, 5, 14, 35, 43, 976720, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]