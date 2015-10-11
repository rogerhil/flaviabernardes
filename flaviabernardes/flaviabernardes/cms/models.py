from datetime import datetime

from django.db import models

from image_cropping import ImageRatioField


from .base import CmsObject, CmsDraft


class BasePage(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_banner1 = models.ImageField(blank=True, upload_to='uploads')
    image_banner2 = models.ImageField(blank=True, upload_to='uploads')
    image_social = models.ImageField(blank=True, upload_to='uploads')
    banner1 = ImageRatioField('image_banner1', '1920x600')
    banner2 = ImageRatioField('image_banner2', '1920x600')
    social = ImageRatioField('image_social', '1200x630')
    content1 = models.TextField(null=True, blank=True)
    content2 = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, default=datetime.now(),
                                   editable=False)
    updated = models.DateTimeField(auto_now=True, default=datetime.now(),
                                   editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return (self.name,)


class Page(BasePage, models.Model, CmsObject):
    name = models.CharField(max_length=128, unique=True, editable=False)

    def __str__(self):
        return self.name

    class cms:
        draft_class = 'cms.PageDraft'


class PageDraft(BasePage, CmsDraft):
    name = models.CharField(max_length=128, editable=False)
    page = models.ForeignKey(Page, null=True, blank=True, editable=False)

    class cms:
        draft_related_class = Page
        instance_name = 'page'
        context_object_name = 'page'
        template_preview = 'PAGE'
