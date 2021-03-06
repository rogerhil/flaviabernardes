
from django.db import models
from django.db.models.signals import pre_save

from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.exceptions import InvalidImageFormatError
from image_cropping import ImageRatioField


class ArtworkType(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class TagArtwork(models.Model):
    artwork = models.ForeignKey('Artwork', related_name='link_to_tag')
    tag = models.ForeignKey(Tag)
    order = models.IntegerField(default=0, editable=False)

    class Meta:
        ordering = ('order',)

    @staticmethod
    def update_order(sender, instance, **kwargs):
        if instance.id:
            tgs = TagArtwork.objects.filter(tag=instance.tag)
            order = max([a.order for a in tgs]) + 1
            instance.order = order


pre_save.connect(TagArtwork.update_order, TagArtwork)



class Artwork(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='uploads')
    type = models.ForeignKey(ArtworkType, verbose_name='Medium')
    tags = models.ManyToManyField(Tag, through=TagArtwork)
    width = models.IntegerField()
    height = models.IntegerField()
    year = models.IntegerField()
    listing = models.BooleanField(default=True)
    order = models.IntegerField(default=0, editable=False)
    mini_thumbnail = ImageRatioField('image', '50x50')
    #thumbnail = ImageRatioField('image', '370x320', size_warning=True)
    #thumbnail = ImageRatioField('image', '360x310', size_warning=True)
    thumbnail = ImageRatioField('image', '640x400', size_warning=True)
    full_preview = ImageRatioField('image', '960x580', free_crop=True)

    id_number = models.IntegerField(null=True, blank=True)
    edition = models.CharField(max_length=128, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=True, blank=True)
    frame_cost = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=True, blank=True)
    other_cost = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=True, blank=True)
    sold = models.BooleanField(default=False)
    collector_contact = models.CharField(max_length=128, null=True, blank=True)
    sold_by = models.CharField(max_length=128, null=True, blank=True)
    exhibition = models.CharField(max_length=128, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('name', 'id')

    def __str__(self):
        return "%s: %s" % (self.id, self.name)

    def mini_thumbnail_url(self):
        field = self._meta.get_field_by_name('mini_thumbnail')[0]
        try:
            thumbnail_url = get_thumbnailer(self.image).get_thumbnail({
                'size': (field.width, field.height),
                'box': self.mini_thumbnail,
                'crop': True,
                'detail': True,
            }).url
        except InvalidImageFormatError:
            return ''
        return thumbnail_url

    @staticmethod
    def update_order(sender, instance, **kwargs):
        if not instance.id:
            order = max([a.order for a in Artwork.objects.all()]) + 1
            instance.order = order

    @property
    def size(self):
        return "%sx%scm" % (self.height, self.width)



pre_save.connect(Artwork.update_order, Artwork)
