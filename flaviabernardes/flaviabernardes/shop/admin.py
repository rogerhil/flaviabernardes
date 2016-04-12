from django.contrib import admin
from django.core.urlresolvers import reverse

from image_cropping import ImageCroppingMixin

from .models import Original, Print

class CommonAdmin(object):

    def link_display(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.link,
                                                        instance.link)
    link_display.allow_tags = True

    def artwork_display(self, instance):
        url = reverse('admin:artwork_artwork_change',
                      args=[str(instance.artwork.id)])
        return '<a href="%s">%s</a>' % (url, instance.artwork)
    artwork_display.allow_tags = True


@admin.register(Original)
class OriginalAdmin(ImageCroppingMixin, admin.ModelAdmin, CommonAdmin):
    list_display = ('name_display', 'description_display', 'price_display',
                    'link_display', 'artwork_display', 'disable', 'sold_out')
    list_filter = ('disable', 'sold_out')
    search_fields = ('name', 'artwork__name', 'description', 'price', 'link')


@admin.register(Print)
class PrintAdmin(ImageCroppingMixin, admin.ModelAdmin, CommonAdmin):
    list_display = ('name_display', 'description_display', 'price_display',
                    'link_display', 'artwork_display', 'disable', 'sold_out')
    list_filter = ('disable', 'sold_out')
    search_fields = ('name', 'artwork__name', 'price', 'price_from',
                     'price_to', 'link')
