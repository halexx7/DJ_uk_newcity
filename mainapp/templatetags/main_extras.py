from datetime import datetime

from django import template

register = template.Library()

# Шаблонный фильтр проверки на новизну новости (а шаблон вешает "new")
@register.filter(name="isLastWeek")
def isLastWeek(date):
    date_now = datetime.today().replace(tzinfo=None)
    date_inst = date.replace(tzinfo=None)
    result = (date_now - date_inst).days < 14
    return result
