from django.contrib import admin

from image_cropping import ImageCroppingMixin

from ..cms.admin import CmsObjectAdmin, CmsDraftAdmin
from .models import Post, Draft, Category


#class ImageInline(admin.TabularInline):
#    model = Image


@admin.register(Post)
class PostAdmin(ImageCroppingMixin, CmsObjectAdmin, admin.ModelAdmin):
    #inlines = [ImageInline]
    list_display = ('title', 'slug', 'created', 'updated', 'modify')


@admin.register(Draft)
class DraftAdmin(ImageCroppingMixin, CmsDraftAdmin, admin.ModelAdmin):
    list_display = ('title', 'post', 'slug', 'created', 'updated')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


#@admin.register(Image)
#class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
#    pass
