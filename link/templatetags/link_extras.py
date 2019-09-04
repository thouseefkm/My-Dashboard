
from django import template

register = template.Library()

@register.simple_tag
def is_multiple_of_3(value):
    """Allows to update existing variable in template"""
    rt_value = True if value % 3 == 0 else False
    print("Return Value: of value {} is {}".format(value, rt_value))
    return rt_value
