from django.contrib import admin

from .models import Tool, ToolType

admin.site.register(ToolType)
admin.site.register(Tool)
