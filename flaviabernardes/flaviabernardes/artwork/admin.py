from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import Artwork, ArtworkType, Tag, TagArtwork


class TagInline(admin.TabularInline):
    model = Artwork.tags.through
    extra = 1 # how many rows to show


@admin.register(Artwork)
class ArtworkAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('name', 'type', 'width', 'height',
                    'mini_thumbnail_display')
    inlines = [TagInline,]
    list_filter = ('type__name',)

    def mini_thumbnail_display(self, item):
        return '<img src="%s" />' % item.mini_thumbnail_url()
    mini_thumbnail_display.allow_tags = True


@admin.register(ArtworkType)
class ArtworkTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

