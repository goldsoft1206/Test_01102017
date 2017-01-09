import datetime

from django import template

register = template.Library()


@register.simple_tag
def get_eligible(profile):
    today = datetime.date.today()
    age = today.year - profile.birth_date.year - ((today.month, today.day) < (profile.birth_date.month, profile.birth_date.day))
    if age < 13:
        return "Blocked"
    return "Allowed"
