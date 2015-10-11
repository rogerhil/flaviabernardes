from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
from django.contrib.sitemaps.views import sitemap

from .views import HomeView, AboutView
from .artwork.views import PaintingsView, ArtworksSortJson
from .blog.views import BlogView, PostView
from .cms.views import CmsDraftPublishView, CmsObjectNewDraftView, \
                       CmsDraftPreview
from .fbauth.views import LoginJson, LogoutJson
from .newsletter.views import LandPageView, ConfirmationView, NewsletterView
from .sitemaps import HomeSitemap, BlogSitemap

sitemaps = dict(
    home=HomeSitemap,
    blog=BlogSitemap
)

is_superuser = user_passes_test(lambda u: u.is_superuser, '/')
s = lambda v: csrf_exempt(is_superuser(v))

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flaviabernardes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/(?P<app>\w+)/(?P<draft_model>\w+)/(?P<pk>\d+)/publish/$',
        s(CmsDraftPublishView.as_view()),
        name='draft_publish'),
    url(r'^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<pk>\d+)/new-draft/$',
        s(CmsObjectNewDraftView.as_view()),
        name='blog_post_new_draft'),
    url(r'^admin/(?P<app>\w+)/(?P<draft_model>\w+)/(?P<pk>\d+)/preview/$',
        s(CmsDraftPreview.as_view()),
        name='draft_preview'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/json/$', LoginJson.as_view(), name='login'),
    #url(r'^logout/json/$', LogoutJson.as_view(), name='logout'),
    url(r'^newsletter/$', NewsletterView.as_view(), name='newsletter'),
    url(r'^confirmation/$', ConfirmationView.as_view(), name='confirmation'),
    url(r'^blog/$', s(BlogView.as_view()), name='blog'),  # REMOVE S() WHEN LAUNCH
    url(r'^blog/(?P<slug>[-_\w]+)/$', PostView.as_view(),
        name='blog_post_view'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

    url(r'^artworks/$', s(PaintingsView.as_view()), name='artworks'), # REMOVE S() WHEN LAUNCH
    url(r'^artworks/sort/$', s(ArtworksSortJson.as_view()), name='artworks_sort'),  # REMOVE S() WHEN LAUNCH
    url(r'^about/$', s(AboutView.as_view()), name='about'),  # REMOVE S() WHEN LAUNCH
    url(r'^contact/$', s(TemplateView.as_view(template_name="contact/contact.html")), name='contact') # REMOVE S() WHEN LAUNCH

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.LANDING_PAGE:
    urlpatterns += [
        url(r'^$', LandPageView.as_view(), name='landpage'),
    ]
else:
    urlpatterns += [
        url(r'^$', HomeView.as_view(), name='home'),
    ]
