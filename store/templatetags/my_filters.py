from django import template


register = template.Library()


def currency(amount):
    return '{:.2f}'.format(amount) + 'SR'


register.filter('currency', currency)