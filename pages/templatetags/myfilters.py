import datetime

from django import template

register = template.Library()


@register.filter
def first(value):
    try:
        return value[0]
    except IndexError:
        return None


@register.filter
def compare_date(value, value2):
    year, month, day = value.split('-')
    year1, month1, day1 = value2.year, value2.month, value2.day
    return datetime.datetime(year=int(year), month=int(month), day=int(day)) == datetime.datetime(year=int(year1), month=int(month1), day=int(day1))