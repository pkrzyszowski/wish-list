# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 12:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0010_auto_20161012_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 10, 12, 12, 35, 33, 306119, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
