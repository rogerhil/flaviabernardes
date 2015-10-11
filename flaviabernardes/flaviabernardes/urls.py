from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
from django.contrib.sitemaps.views import sitemap

from .artwork.views import HomeView, PaintingsView, ArtworksSortJson
from .blog.views import BlogView, PostView, DraftPreview
from .cms.views import CmsDraftPublishView, CmsObjectNewDraftView
from .fbauth.views import LoginJson, LogoutJson
from .newsletter.views import LandPageView, ConfirmationView, NewsletterView
from .sitemaps import HomeSitemap, BlogSitemap

sitemaps = dict(
    home=HomeSitemap,
    blog=BlogSitemap
)

is_superuser = user_passes_test(lambda u: u.is_superuser, '/')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flaviabernardes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/(?P<app>\w+)/(?P<draft_model>\w+)/(?P<pk>\d+)/publish/$',
        csrf_exempt(is_superuser(CmsDraftPublishView.as_view())),
        name='draft_publish'),
    url(r'^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<pk>\d+)/new-draft/$',
        csrf_exempt(is_superuser(CmsObjectNewDraftView.as_view())),
        name='blog_post_new_draft'),
    url(r'^admin/(?P<app>\w+)/(?P<draft_model>\w+)/(?P<pk>\d+)/preview/$',
        csrf_exempt(is_superuser(DraftPreview.as_view())),
        name='draft_preview'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/json/$', LoginJson.as_view(), name='login'),
    #url(r'^logout/json/$', LogoutJson.as_view(), name='logout'),
    url(r'^newsletter/$', NewsletterView.as_view(), name='newsletter'),
    url(r'^confirmation/$', ConfirmationView.as_view(), name='confirmation'),
    url(r'^blog/$', BlogView.as_view(), name='blog'),
    url(r'^blog/(?P<slug>[-_\w]+)/$', PostView.as_view(),
        name='blog_post_view'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.LANDING_PAGE:
    urlpatterns += [
        url(r'^$', LandPageView.as_view(), name='landpage'),
    ]
else:
    urlpatterns += [
        url(r'^$', HomeView.as_view(), name='home'),
        url(r'^artworks/$', PaintingsView.as_view(), name='artworks'),
        url(r'^artworks/sort/$',
            csrf_exempt(is_superuser(ArtworksSortJson.as_view())),
            name='artworks_sort'),
        url(r'^about/$',
            TemplateView.as_view(template_name="about/about.html"),
            name='about')
    ]
