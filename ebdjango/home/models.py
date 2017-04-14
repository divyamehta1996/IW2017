from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
	name = models.CharField(max_length=75)
	gender = models.CharField(max_length=10)
	birthday = models.CharField(max_length=20)
	city = models.CharField(max_length=75)
	facebook_id = models.IntegerField(default=0)


class Facebook(models.Model):
	sports = models.CharField(max_length=100)
	music = models.CharField(max_length=100)
	books = models.CharField(max_length=100)
	checkins = models.CharField(max_length=100)
	hometown = models.CharField(max_length=100)