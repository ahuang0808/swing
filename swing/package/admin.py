from django.contrib import admin
from django.contrib.admin import ModelAdmin

from swing.package.models.package import Package


@admin.register(Package)
class PackageAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
