from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fields = [
        "title",
        "parent",
        "url",
        "named_url",
        "order",
    ]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    list_display = [
        "name",
        "slug",
    ]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "menu",
        "parent",
        "order",
    ]
    list_filter = [
        "menu",
    ]
    search_fields = [
        "title",
        "url",
        "named_url",
    ]
