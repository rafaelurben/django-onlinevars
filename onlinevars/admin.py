from django.contrib import admin

from .models import Variable

# Register your models here.

@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields  = ["name"]

    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Wert', {'fields': ['value'], 'classes': ["collapse"]})
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["name"]
        else:
            return []
