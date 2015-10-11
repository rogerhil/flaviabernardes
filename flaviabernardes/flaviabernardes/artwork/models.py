from django.db import models

from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageRatioField


class ArtworkType(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Artwork(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='uploads')
    type = models.ForeignKey(ArtworkType)
    width = models.IntegerField()
    height = models.IntegerField()
    year = models.IntegerField()
    listing = models.BooleanField(default=True)
    home = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    mini_thumbnail = ImageRatioField('image', '50x50')
    #thumbnail = ImageRatioField('image', '370x320', size_warning=True)
    #thumbnail = ImageRatioField('image', '360x310', size_warning=True)
    thumbnail = ImageRatioField('image', '640x600', size_warning=True)
    full_preview = ImageRatioField('image', '960x580', free_crop=True)

    def __str__(self):
        return self.name

    def mini_thumbnail_url(self):
        field = self._meta.get_field_by_name('mini_thumbnail')[0]
        thumbnail_url = get_thumbnailer(self.image).get_thumbnail({
            'size': (field.width, field.height),
            'box': self.mini_thumbnail,
            'crop': True,
            'detail': True,
        }).url
        return thumbnail_url
