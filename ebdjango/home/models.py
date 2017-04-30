# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Users(models.Model):
	username = models.OneToOneField(User)
	name = models.CharField(max_length=50, default="")
	gender = models.CharField(max_length=10, default="")
	birthday = models.CharField(max_length=20, default="")
	city = models.CharField(max_length=75, default="")
	state = models.CharField(max_length=75, default="")
	sports = models.CharField(max_length=300, default="")
	music = models.CharField(max_length=300, default="")
	books = models.CharField(max_length=300, default="")
	checkins = models.CharField(max_length=300, default="")
	brands = models.CharField(max_length=300, default="")
	
	def __str__(self):
		return self.name + ',' + self.birthday + ', ' + self.city

class UserWishlist(models.Model):
	username = models.ForeignKey(User, related_name='user_wishes')
	item = models.CharField(max_length=100, default="")

