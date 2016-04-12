from decimal import Decimal

from django.db import models
from django.conf import settings

from image_cropping import ImageRatioField

from ..artwork.models import Artwork


class ShopItem(object):

    def price_display(self):
        raise NotImplementedError

    def name_display(self):
        if self.name:
            return self.name
        elif self.artwork:
            return self.artwork.name
        return ""

    def description_display(self):
        raise NotImplementedError


class Original(models.Model, ShopItem):
    artwork = models.ForeignKey(Artwork, null=True, blank=True)
    name = models.CharField(max_length=64, null=True, blank=True,
        help_text="Please fill this field in case there's no artwork "
                  "associated with this shop item.")
    description = models.CharField(max_length=64, null=True, blank=True,
        help_text="If there's no artwork associated with this shop item, this "
                  "field must be filled with the following information: "
                  "'media type' and the 'size'.")
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                help_text="Price in euros")
    link = models.URLField()
    image = models.ImageField(blank=True, upload_to=settings.UPLOAD_TO)
    thumbnail = ImageRatioField('image', '640x400', size_warning=True)
    order = models.IntegerField(default=0, editable=False)
    disable = models.BooleanField(default=False)
    sold_out = models.BooleanField(default=False)

    def __str__(self):
        return "Original: %s" % str(self.name_display())

    def price_display(self):
        if self.sold_out:
            return "Sold Out"
        return "&euro; %s" % self.price  #.quantize(Decimal('0.01'))
    price_display.allow_tags = True

    def description_display(self):
        if self.description:
            return self.description
        elif self.artwork:
            return "%s, %s" % (self.artwork.type, self.artwork.size)
        return ""


class Print(models.Model, ShopItem):
    artwork = models.ForeignKey(Artwork, null=True, blank=True)
    name = models.CharField(max_length=64, null=True, blank=True,
        help_text="Please fill this field in case there's no artwork "
                  "associated with this shop item.")
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
    sold_out = models.BooleanField(default=False)

    def __str__(self):
        return "Print: %s" % str(self.name_display())

    def price_display(self):
        if self.sold_out:
            return "Sold Out"
        price = ""
        if self.price:
            price = "&euro; %s" % self.price
        else:
            if self.price_from:
                price = "from &euro; %s" % self.price_from
            elif self.price_to:
                price += " to &euro; %s" % self.price_to
        return price.strip()
    price_display.allow_tags = True

    def description_display(self):
        return self.sizes
