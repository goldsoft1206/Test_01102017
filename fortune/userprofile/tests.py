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

    def render_template(self, string, context=None):
        context = context or {}
        context = Context(context)
        return Template(string).render(context)

    def test_eligible_tag(self):
        """
        Test of eligible tag
        """
        rendered = self.render_template(
            '{% load custom_tag %}{% get_eligible object %}',
            context = {'object': self.test_user_profile1}
        )
        self.assertEqual(rendered,"Allowed")

        rendered = self.render_template(
            '{% load custom_tag %}{% get_eligible object %}',
            context = {'object': self.test_user_profile2}
        )
        self.assertEqual(rendered,"Blocked")


    def test_bizzfuzz_tag(self):
        """
        Test of bizzfuzz tag
        """
        rendered = self.render_template(
            '{% load custom_tag %}{% get_bizzfuzz object %}',
            context = {'object': self.test_user_profile1}
        )
        self.assertEqual(rendered,"BizzFuzz")

        rendered = self.render_template(
            '{% load custom_tag %}{% get_bizzfuzz object %}',
            context = {'object': self.test_user_profile2}
        )
        self.assertEqual(rendered,"Bizz")

