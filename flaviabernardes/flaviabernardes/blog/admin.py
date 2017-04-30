from django.contrib import admin

from image_cropping import ImageCroppingMixin

from ..cms.admin import CmsObjectAdmin, CmsDraftAdmin
from .models import Post, Draft, Category


#class ImageInline(admin.TabularInline):
#    model = Image


@admin.register(Post)
class PostAdmin(ImageCroppingMixin, CmsObjectAdmin, admin.ModelAdmin):
    #inlines = [ImageInline]
    fields = ('title', 'slug', 'description', 'newsletter_form_title', 'tags',
              'text', 'text2', 'image_banner', 'banner', 'image_banner2',
              'banner2', 'image_listing', 'listing', 'listing_half')
    list_display = ('title', 'slug', 'created', 'updated', 'modify')


@admin.register(Draft)
class DraftAdmin(ImageCroppingMixin, CmsDraftAdmin, admin.ModelAdmin):
    fields = PostAdmin.fields
    list_display = ('title', 'post', 'slug', 'created', 'updated')
    list_filter = ('post',)
    filter_horizontal = ('tags',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


#@admin.register(Image)
#class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
#    pass
