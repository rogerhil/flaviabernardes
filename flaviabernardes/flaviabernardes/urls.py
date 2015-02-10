from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

from .artwork.views import HomeView, PaintingsView, ArtworksSortJson


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flaviabernardes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/$', include(admin.site.urls)),
    url(r'^artworks/$', PaintingsView.as_view(), name='artworks'),
    url(r'^artworks/sort/$', ArtworksSortJson.as_view(), name='artworks_sort'),
    url(r'^about/$', TemplateView.as_view(template_name="about/about.html"),
        name='about'),
    url(r'^$', HomeView.as_view(), name='home'),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
