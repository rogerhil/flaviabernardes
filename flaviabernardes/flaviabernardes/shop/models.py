from decimal import Decimal

from django.db import models
from django.conf import settings

from image_cropping import ImageRatioField

from ..artwork.models import Artwork


class Original(models.Model):
    artwork = models.ForeignKey(Artwork)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                help_text="Price in euros")
    link = models.URLField()
    image = models.ImageField(blank=True, upload_to=settings.UPLOAD_TO)
    thumbnail = ImageRatioField('image', '640x400', size_warning=True)
    order = models.IntegerField(default=0, editable=False)
    disable = models.BooleanField(default=False)

    def __str__(self):
        return "Original: %s" % str(self.artwork)

    def price_display(self):
        return "&euro; %s" % self.price  #.quantize(Decimal('0.01'))


class Print(models.Model):
    artwork = models.ForeignKey(Artwork)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                blank=True, help_text="Price in euros")
    price_from = models.DecimalField(max_digits=10, decimal_places=2,
                                     null=True, blank=True,
                                     help_text="Price in euros")
    price_to = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                   blank=True, help_text="Price in euros")
    sizes = models.TextField()
    link = models.URLField()
    image = models.ImageField(blank=True, upload_to=settings.UPLOAD_TO)
    thumbnail = ImageRatioField('image', '640x400', size_warning=True)
    order = models.IntegerField(default=0, editable=False)
    disable = models.BooleanField(default=False)

    def __str__(self):
        return "Print: %s" % str(self.artwork)

    def price_display(self):
        price = ""
        if self.price:
            price = "&euro; %s" % self.price
        else:
            if self.price_from:
                price = "from &euro; %s" % self.price_from
            elif self.price_to:
                price += " to &euro; %s" % self.price_to
        return price.strip()
