from django.contrib import admin
from .models import Coche


@admin.register(Coche)
class CocheAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "dueno", "created_at")
    search_fields = ("marca", "modelo", "dueno")
    list_filter = ("marca",)
