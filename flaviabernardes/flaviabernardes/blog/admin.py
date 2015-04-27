from django.contrib import admin

from image_cropping import ImageCroppingMixin

from .models import Blog, Category, Tag, Image


class ImageInline(admin.TabularInline):
    model = Image



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    #list_display = ('name', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass