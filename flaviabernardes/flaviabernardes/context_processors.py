
from django.conf import settings
from .cms.models import Page
from .newsletter.models import List

def global_context(request):
    user = request.user
    context = dict(landing_page=settings.LANDING_PAGE)
    pages = Page.objects.all()
    context['main_pages'] = dict([(p.name, p) for p in pages
                                  if p.sub_page_of is None])
    context['footer_pages'] = [p for p in pages if p.footer]
    try:
        newsletter_list = List.objects.get(list_id='Newsletter')
    except List.DoesNotExist:
        newsletter_list = None
    context['default_newsletter_list'] = newsletter_list
    context['enable_shop'] = settings.ENABLE_SHOP or user.is_authenticated()
    return context
