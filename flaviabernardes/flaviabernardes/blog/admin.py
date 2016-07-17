from django.contrib import admin

from image_cropping import ImageCroppingMixin

from ..cms.admin import CmsObjectAdmin, CmsDraftAdmin
from .models import Post, Draft, Category


#class ImageInline(admin.TabularInline):
#    model = Image


@admin.register(Post)
class PostAdmin(ImageCroppingMixin, CmsObjectAdmin, admin.ModelAdmin):
    #inlines = [ImageInline]
    fields = ('title', 'slug', 'description', 'tags', 'text', 'text2',
              'text3', 'text4',
              'image_banner', 'banner', 'image_banner2', 'banner2',
              'image_listing', 'listing', 'listing_half',
              'image_banner_with_content', 'banner_with_content',
              'content_for_banner', 'banner_newsletter')
    list_display = ('title', 'slug', 'created', 'updated', 'modify')


@admin.register(Draft)
class DraftAdmin(ImageCroppingMixin, CmsDraftAdmin, admin.ModelAdmin):
    fields = PostAdmin.fields
    list_display = ('title', 'post', 'slug', 'created', 'updated')
    list_filter = ('post',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


#@admin.register(Image)
#class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
#    pass
