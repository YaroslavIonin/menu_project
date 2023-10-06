from django.contrib import admin

from ..models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    prepopulated_fields = {"slug": ("title",)}
    empty_value_display = 'Меню'
