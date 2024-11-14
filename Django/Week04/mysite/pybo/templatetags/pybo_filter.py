from django import template

register = template.Library()

#template에서 해당 함수를 필터로 사용할 수 있게 하는 애너테이션
@register.filter 
def sub(value, arg):
    return value - arg