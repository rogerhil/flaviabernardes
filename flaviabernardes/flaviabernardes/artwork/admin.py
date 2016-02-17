from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import Artwork, ArtworkType, Tag, TagArtwork


class TagInline(admin.TabularInline):
    model = Artwork.tags.through
    extra = 1 # how many rows to show


@admin.register(Artwork)
class ArtworkAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('mini_thumbnail_display',
                    'name', 'type', 'width', 'height', 'tags_display',
                    'id_number', 'edition', 'total_price', 'frame_cost',
                    'other_cost', 'sold', 'collector_contact', 'sold_by',
                    'exhibition', 'notes')

    inlines = [TagInline,]
    list_filter = ('type__name', 'sold', 'sold_by')
    search_fields = ('name', 'width', 'height', 'id_number', 'edition',
                     'collector_contact', 'exhibition', 'notes')

    def mini_thumbnail_display(self, item):
        return '<img src="%s" />' % item.mini_thumbnail_url()
    mini_thumbnail_display.allow_tags = True
    mini_thumbnail_display.short_description = 'Thumb'

    def tags_display(self, item):
        return ', '.join([i.name for i in item.tags.all()])
    tags_display.short_description = 'Tags'


@admin.register(ArtworkType)
class ArtworkTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

