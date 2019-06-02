from django import template


register = template.Library()
@register.filter(name='update_variable')
def update_variable(args,value):
    """Allows to update existing variable in template"""
    return value
