import math
from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
from django.template.defaultfilters import Truncator, strip_tags

from image_cropping import ImageRatioField

from ..cms.base import CmsObject, CmsDraft, DESCRIPTION_HELP_TEXT


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class BasePost(models.Model):
    text = models.TextField()
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True,
                                   help_text=DESCRIPTION_HELP_TEXT)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    tags = models.ManyToManyField(Category)
    image_banner = models.ImageField(blank=True, upload_to=settings.UPLOAD_TO)
    image_banner2 = models.ImageField(blank=True, upload_to=settings.UPLOAD_TO)
    image_listing = models.ImageField(blank=True, upload_to=settings.UPLOAD_TO)
    listing = ImageRatioField('image_listing', '1920x600')
    listing_half = ImageRatioField('image_listing', '960x600')
    banner = ImageRatioField('image_banner', '1920x600')
    banner2 = ImageRatioField('image_banner2', '1920x1200')
    image_banner_with_content = models.ImageField(blank=True,
                                                  upload_to=settings.UPLOAD_TO)
    banner_with_content = ImageRatioField('image_banner_with_content',
                                          '1920x1200')
    content_for_banner = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s: %s' % (self.__class__.__name__, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_view', None, {'slug': self.slug})

    def listing_summary(self):
        title_lines = math.ceil(len(self.title) / 28)
        summary_lines = 4 - title_lines
        return Truncator(strip_tags(self.text)).chars(30 * summary_lines)

    @property
    def is_old(self):
        month = 30
        return (datetime.now() - self.created) > timedelta(6 * month)


class Post(BasePost, CmsObject):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=64, unique=True)

    class cms:
        draft_class = 'blog.Draft'


class Draft(BasePost, CmsDraft):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=64)
    post = models.ForeignKey(Post, null=True, blank=True, editable=False,
                             on_delete=models.SET(None))

    class cms:
        draft_related_class = Post
        instance_name = 'post'
        context_object_name = 'post'
        template_preview = 'blog/post.html'
        publish_ignore = ['created']


class BaseImage(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(blank=True, upload_to='uploads')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


#class Image(BaseImage):
#    post = models.ForeignKey(Post, related_name='images')
#    ratio = ImageRatioField('image', '50x50')


#class DraftImage(BaseImage):
#    draft = models.ForeignKey(Draft)
#    ratio = ImageRatioField('image', '50x50')
