from django.db.models import Sum
from oscar_accounts.checkout import gateway
from django import template

register = template.Library()

@register.simple_tag
def current_balance(user):
    if user.is_authenticated:
        user_accounts = gateway.user_accounts(user)
        total_balance = user_accounts.aggregate(Sum("balance")).get("balance__sum", 0)
    else:
        total_balance = 0
    return total_balance