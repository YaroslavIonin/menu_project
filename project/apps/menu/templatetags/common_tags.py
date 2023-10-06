from django import template

from apps.menu.models import Menu

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name):
    menu_items = Menu.objects.get(
        name=name
    ).menuitem.get_family()

    current_path = context.request.path

    return {
        'current_path': current_path,
        'menu': menu_items,
    }
