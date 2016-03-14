from django.contrib import admin

from image_cropping import ImageCroppingMixin

from .models import Original, Print


@admin.register(Original)
class OriginalAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


@admin.register(Print)
class PrintAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass
