import datetime

from django import template

register = template.Library()


@register.simple_tag
def get_eligible(profile):
    """
    Calculate user age and return "Allowed" if he/she's older than 13 years.
    If not, returns "Blocked"
    """
    today = datetime.date.today()
    age = today.year - profile.birth_date.year - ((today.month, today.day) < (profile.birth_date.month, profile.birth_date.day))
    if age < 13:
        return "Blocked"
    return "Allowed"


@register.simple_tag
def get_bizzfuzz(profile):
    """
    The BizzFuzz specification is that for multiples of three, print "Bizz" instead of the number 
    and for the multiples of five print "Fuzz".
    For numbers which are multiples of both three and five print "BizzFuzz"
    """
    if profile.random_number % 3 == 0 and profile.random_number % 5 == 0:
        return "BizzFuzz"
    elif profile.random_number % 3 == 0:
        return "Bizz"
    elif profile.random_number % 5 == 0:
        return "Fuzz"
    else:
        return profile.random_number

