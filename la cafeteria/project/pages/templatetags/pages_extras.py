from django import template
from pages.models import PagesModels

register = template.Library()

@register.simple_tag
def get_list_pages():
    pages = PagesModels.objects.all()
    return pages