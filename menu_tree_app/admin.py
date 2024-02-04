from django.contrib import admin
from .models import MenuItem
from mptt.admin import DraggableMPTTAdmin

@admin.register(MenuItem)
class MenuItemAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20
    list_display = ('tree_actions', 'indented_title', 'menu', 'parent', 'url_name', 'url', 'order')
    list_display_links = ('indented_title',)
