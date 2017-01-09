from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	"""
	UserProfile model extends User model for birthdate and random number
	"""
	user = models.OneToOneField(User, related_name="profile")

	birth_date = models.DateField()

	# random number should be range(1, 100)
	random_number = models.PositiveSmallIntegerField(default=1)

