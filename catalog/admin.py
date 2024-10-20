from django.contrib import admin

from catalog.models import Category, Product, Version
from users.models import User


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "is_published")
    list_filter = ("price", "name", "category", "is_published")
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("product", "version_number", "version_name", "is_active")
    list_filter = ("is_active", "product")

