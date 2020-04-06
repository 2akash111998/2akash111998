# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_obj(models.Model):
	# name = models.CharField(max_length = 264)
	# email = models.EmailField(max_length = 264, unique = True)

	user = models.OneToOneField(User)

	# Additional parameters
	nick_name = models.CharField(max_length = 100)
	profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

	def __str__(self):
		return self.user.username