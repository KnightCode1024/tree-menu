from django import template
from django.urls import resolve, reverse
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag("menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context["request"]
    current_url = request.path_info

    try:
        menu = Menu.objects.prefetch_related("items").get(name=menu_name)
        menu_items = menu.items.all()

        active_items = []
        for item in menu_items:
            item_url = item.get_url()
            if item_url == current_url:
                active_items.append(item)

        active_ids = set()
        for item in active_items:
            active_ids.add(item.id)
            parent = item.parent
            while parent:
                active_ids.add(parent.id)
                parent = parent.parent

        def build_tree(items, parent=None):
            tree = []
            for item in items:
                if item.parent == parent:
                    node = {
                        "item": item,
                        "children": build_tree(items, item),
                        "is_active": item.id in active_ids,
                        "is_current": item_url == current_url,
                    }
                    tree.append(node)
            return tree

        menu_tree = build_tree(menu_items)

        return {
            "menu": menu,
            "menu_tree": menu_tree,
            "current_url": current_url,
        }
    except Menu.DoesNotExist:
        return {"menu": None}
