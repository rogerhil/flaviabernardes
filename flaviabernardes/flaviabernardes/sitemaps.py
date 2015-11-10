from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from .blog.models import Post
from .cms.models import Page


class HomeSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


class PagesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Page.objects.filter(confirmation_newsletter_lists=None)

    def lastmod(self, obj):
        return obj.updated


class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated
