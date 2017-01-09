import datetime

from django import template

register = template.Library()


@register.simple_tag
def get_eligible(profile):
    """
    Calculate user age and return "Allowed" if he/she's older than 13 years.
    If not, returns "Blocked"
    """
    return profile.get_eligible()


@register.simple_tag
def get_bizzfuzz(profile):
    """
    The BizzFuzz specification is that for multiples of three, print "Bizz" instead of the number 
    and for the multiples of five print "Fuzz".
    For numbers which are multiples of both three and five print "BizzFuzz"
    """
    return profile.get_bizzfuzz()

