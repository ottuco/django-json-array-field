from django.contrib import admin

from .models import JSONArrayFieldModel


@admin.register(JSONArrayFieldModel)
class JSONArrayFieldModelAdmin(admin.ModelAdmin):
    list_display = ("list_field",)
