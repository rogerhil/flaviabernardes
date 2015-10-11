from django.db import models

from image_cropping import ImageRatioField


class Page(models.Model):
    name = models.CharField(max_length=128, unique=True, editable=False)
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

    def __str__(self):
        return self.name
