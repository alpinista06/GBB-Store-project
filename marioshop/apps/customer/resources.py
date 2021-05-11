from import_export import resources
from oscar.core.compat import (existing_user_fields, get_user_model)
from tools.models import Tool
from tablib import Dataset

User = get_user_model()

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ['password', 'last_login', 'is_superuser', 'group', 'user_premissions', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'id',]

class ToolResource(resources.ModelResource):
    class Meta:
        model = Tool
        fields = ['transfer__username', 'type__name', 'type__type', 'quantity', 'value']