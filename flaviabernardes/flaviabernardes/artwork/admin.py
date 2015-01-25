from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import Artwork, ArtworkType


@admin.register(Artwork)
class ArtworkAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('name', 'type', 'mini_thumbnail_display')

    def mini_thumbnail_display(self, item):
        return '<img src="%s" />' % item.mini_thumbnail_url()
    mini_thumbnail_display.allow_tags = True


@admin.register(ArtworkType)
class ArtworkTypeAdmin(admin.ModelAdmin):
    pass

