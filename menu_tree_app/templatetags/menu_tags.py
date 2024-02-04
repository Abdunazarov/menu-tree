from django import template
from menu_tree_app.models import MenuItem
from mptt.templatetags.mptt_tags import cache_tree_children

register = template.Library()

@register.inclusion_tag('menu_tree_app/menu.html')
def draw_menu(menu_name):
    all_menu_items = cache_tree_children(MenuItem.objects.all())
    top_menu_items = [item for item in all_menu_items if item.menu == menu_name and item.parent is None]
    print(all_menu_items)
    print(top_menu_items)
    return {'menu_items': top_menu_items}
