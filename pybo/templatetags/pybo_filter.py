
from django import template
register = template.Library()

@register.filter
def sub(value, arg): # 템플릿 필터 함수
    return value-arg
