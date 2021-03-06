from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
from django.contrib.sitemaps.views import sitemap

from .views import HomeView, AboutView, ContactView, ShopifyProduct
from .shop.views import ShopOriginalsView, ShopPrintsView, ShopSortJson
from .artwork.views import PaintingsView, ArtworksSortJson, ArtworksFilter
from .blog.views import BlogView, PostView
from .cms.views import CmsDraftPublishView, CmsObjectNewDraftView, \
                       CmsDraftPreview, SubPageView, CustomPageView, \
                       UploadImageView, ImagesPathsView, PurgeUnusedImagesView
from .globalsettings.views import CloseTopBarView

from .fbauth.views import LoginJson, LogoutJson
from .newsletter.views import LandPageView, ConfirmationView, NewsletterView, \
                              CustomConfirmationView
from .sitemaps import HomeSitemap, BlogSitemap, PagesSitemap

sitemaps = dict(
    home=HomeSitemap,
    blog=BlogSitemap,
    pages=PagesSitemap
)

is_superuser = user_passes_test(lambda u: u.is_superuser, '/')
s = lambda v: csrf_exempt(is_superuser(v))

# if settings.ENABLE_SHOP:
#     urlpatterns = [
#         url(r'^shop/$', RedirectView.as_view(pattern_name='shop_originals'),
#             name='shop'),
#         url(r'^shop/originals/$', ShopOriginalsView.as_view(),
#             name='shop_originals'),
#         url(r'^shop/prints/$', ShopPrintsView.as_view(),
#             name='shop_prints'),
#         url(r'^shop/sort/$', s(ShopSortJson.as_view()),
#             name='shop_sort'),
#     ]
# else:
#     urlpatterns = [
#         url(r'^shop/$', s(RedirectView.as_view(pattern_name='shop_originals')),
#             name='shop'),
#         url(r'^shop/originals/$', s(ShopOriginalsView.as_view()),
#             name='shop_originals'),
#         url(r'^shop/prints/$', s(ShopPrintsView.as_view()),
#             name='shop_prints'),
#         url(r'^shop/sort/$', s(ShopSortJson.as_view()),
#             name='shop_sort'),
#     ]

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
    url(r'^admin/cms/image/upload/$', s(UploadImageView.as_view()),
        name='upload_image'),
    url(r'^admin/cms/image/list/$', s(ImagesPathsView.as_view()),
        name='list_images'),
    url(r'^admin/cms/image/purge_all/$', s(PurgeUnusedImagesView.as_view()),
        name='purge_all_images'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^shopify/api/product/$', ShopifyProduct.as_view(),
        name='shopify_api_product'),
    #url(r'^login/json/$', LoginJson.as_view(), name='login'),
    #url(r'^logout/json/$', LogoutJson.as_view(), name='logout'),
    url(r'^newsletter/$', NewsletterView.as_view(), name='newsletter'),
    url(r'^confirmation/$', ConfirmationView.as_view(), name='confirmation'),
    url(r'^blog/$', BlogView.as_view(), name='blog'),
    url(r'^blog/(?P<slug>[-_\w]+)/$', PostView.as_view(),
        name='blog_post_view'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

    url(r'^globalsettings/close-top-bar/$',
        csrf_exempt(CloseTopBarView.as_view()), name='close_top_bar'),

    url(r'^artworks/$', PaintingsView.as_view(), name='artworks'),
    url(r'^artworks/filter/$', ArtworksFilter.as_view(),
        name='artworks_filter'),
    url(r'^artworks/sort/$', s(ArtworksSortJson.as_view()),
        name='artworks_sort'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^nl/(?P<slug>[-_\w/]+)/$', CustomConfirmationView.as_view(),
        name='custom_confirmation_page'),
    url(r'^(?P<slug>[-_\w]+)/(?P<subslug>[-_\w]+)/$', SubPageView.as_view(), name='sub_page'),
    url(r'^(?P<slug>[-_\w/]+)/$', CustomPageView.as_view(), name='custom_page'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^$', HomeView.as_view(), name='home'),
]
