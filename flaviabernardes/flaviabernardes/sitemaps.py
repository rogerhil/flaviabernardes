from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from .blog.models import Post


class HomeSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ['landpage']

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.7

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated
