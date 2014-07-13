from django import template

register = template.Library()

@register.filter
def music(list, category):
    for i in list:
        if i.category == category:
            return i.title
