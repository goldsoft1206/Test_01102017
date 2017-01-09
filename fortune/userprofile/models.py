from __future__ import unicode_literals

import datetime

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

    def get_eligible(self):
        # custom function to check if user is older than 13 years or not
        today = datetime.date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        if age < 13:
            return "Blocked"
        return "Allowed"

    def get_bizzfuzz(self):
        # get value from bizzfuzz algorithm
        if self.random_number % 3 == 0 and self.random_number % 5 == 0:
            return "BizzFuzz"
        elif self.random_number % 3 == 0:
            return "Bizz"
        elif self.random_number % 5 == 0:
            return "Fuzz"
        else:
            return self.random_number
