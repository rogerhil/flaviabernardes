
from django.conf import settings

def global_context(request):
    return dict(landing_page=settings.LANDING_PAGE)
