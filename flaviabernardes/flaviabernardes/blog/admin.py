from django.contrib import admin

from image_cropping import ImageCroppingMixin

from .models import Blog, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Blog)
class BlogAdmin(ImageCroppingMixin, admin.ModelAdmin):
    inlines = [ImageInline]
    #list_display = ('name', 'category')


@admin.register(Image)
class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass