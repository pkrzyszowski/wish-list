# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 13:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0012_auto_20161012_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 10, 12, 13, 30, 15, 370402, tzinfo=utc)),
        ),
    ]