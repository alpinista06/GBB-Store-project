from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth import get_user_model

from .models import Tool

User = get_user_model()

class ToolForm(ModelForm):
    user = ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Tool
        fields = ['user',"type","quantity"]


class ToolImportForm(ModelForm):
    user = ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Tool
        fields = ['user', 'type', 'quantity',]