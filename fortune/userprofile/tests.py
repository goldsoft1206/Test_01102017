import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.template import Context, Template

from .models import UserProfile


class UserProfileTest(TestCase):
    """
    Test case for User profile
    """
    def setUp(self):
        test_user1 = User.objects.create_user(username="test1")
        self.test_user_profile1 = UserProfile(user=test_user1, birth_date=datetime.date(2003, 1, 1), random_number=30)
        self.test_user_profile1.save()
        test_user2 = User.objects.create_user(username="test2")
        self.test_user_profile2 = UserProfile(user=test_user2, birth_date=datetime.date(2006, 1, 1), random_number=12)
        self.test_user_profile2.save()

    def test_eligible_tag(self):
        """
        Test of eligible tag
        """
        self.assertEqual(self.test_user_profile1.get_eligible(),"Allowed")
        self.assertEqual(self.test_user_profile2.get_eligible(),"Blocked")


    def test_bizzfuzz_tag(self):
        """
        Test of bizzfuzz tag
        """
        self.assertEqual(self.test_user_profile1.get_bizzfuzz(),"BizzFuzz")
        self.assertEqual(self.test_user_profile2.get_bizzfuzz(),"Bizz")

