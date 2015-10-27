
from django.conf import settings
from .cms.models import Page

def global_context(request):
    context = dict(landing_page=settings.LANDING_PAGE)
    main_pages = Page.objects.filter(sub_page_of=None)
    context['main_pages'] = dict([(p.name, p) for p in main_pages])
    return context
