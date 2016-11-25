from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    task_text = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(default=timezone.now(), blank=True)
    rank = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.task_text


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    wish_points = models.IntegerField(default=30)
    image = models.ImageField(upload_to='avatar/', null=True, blank=True,
                              height_field='height_field', width_field='width_field', default = 'avatar/avatar1.jpg')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    # something_stupid = property(lambda self: self.user.first_name + ' ' + self.user.last_name)
