
from django.conf import settings
from .cms.models import Page
from .newsletter.models import List
from .globalsettings import get_global_settings


def global_context(request):
    user = request.user
    context = dict(landing_page=settings.LANDING_PAGE)
    global_settings = get_global_settings()
    context['menus'] = global_settings.menus
    context['footer_pages'] = [p for p in global_settings.get_pages().values()
                               if p.footer]
    try:
        newsletter_list = List.objects.get(list_id='Newsletter')
    except List.DoesNotExist:
        newsletter_list = None
    context['default_newsletter_list'] = newsletter_list
    context['enable_shop'] = settings.ENABLE_SHOP or user.is_authenticated()
    context['global_settings'] = global_settings
    context['enable_top_bar'] = request.session.get('enable_top_bar', True)
    return context
