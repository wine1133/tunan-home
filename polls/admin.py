from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("contact", "phone", "company", "project_type", "quantity", "city", "budget", "created_at")
    list_filter = ("project_type", "budget", "created_at")
    search_fields = ("contact", "phone", "company", "message")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)