
from django.conf import settings
from .cms.models import Page

def global_context(request):
    context = dict(landing_page=settings.LANDING_PAGE)
    pages = Page.objects.all()
    context['main_pages'] = dict([(p.name, p) for p in pages
                                  if p.sub_page_of is None])
    context['footer_pages'] = [p for p in pages if p.footer]
    return context
