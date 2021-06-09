from django import template
from datetime import datetime, timezone


register = template.Library()


@register.filter(name='cal_exp_day')
def cal(exp_day):
    now = datetime.now(timezone.utc)
    delta = exp_day - now
    val = '%s days, %s hours, %s seconds' % (delta.days, delta.seconds//3600, (delta.seconds//60) % 60)
    return val


@register.filter(name='fdate')
def format_date(date):
    return date.strftime("%d-%M-%Y")
