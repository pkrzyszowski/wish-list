# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 10:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0016_auto_20161107_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 11, 7, 10, 51, 41, 748942, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='avatar/avatar1.jpg', height_field='height_field', null=True, upload_to='avatar/', width_field='width_field'),
        ),
    ]
