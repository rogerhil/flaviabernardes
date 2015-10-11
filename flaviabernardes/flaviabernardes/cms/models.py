from django.conf import settings
from django.db import models
from django.contrib.sitemaps import ping_google
from django.core.mail import send_mail
from django.template.defaultfilters import Truncator, strip_tags

from image_cropping import ImageRatioField


class Page(models.Model):
    name = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=255)
    image_banner1 = models.ImageField(blank=True, upload_to='uploads')
    banner1 = ImageRatioField('image_banner1', '1920x600')
    image_banner2 = models.ImageField(blank=True, upload_to='uploads')
    banner2 = ImageRatioField('image_banner2', '1920x600')
    content1 = models.TextField(null=True, blank=True)
    content2 = models.TextField(null=True, blank=True)
