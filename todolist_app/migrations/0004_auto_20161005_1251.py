# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 10:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0003_auto_20161005_1041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='power',
            new_name='wish_points',
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 10, 5, 10, 51, 47, 704807, tzinfo=utc)),
        ),
    ]
