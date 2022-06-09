from django import template


register = template.Library()


@register.filter
def addclass(field, css):
    """Добавляет в выбронное поле HTML аттрибут"""
    return field.as_widget(attrs={'class': css})
