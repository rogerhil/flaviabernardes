from django.contrib import admin
from django.utils.html import format_html

from image_cropping import ImageCroppingMixin

from .models import Blog, Image, Draft


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Blog)
class BlogAdmin(ImageCroppingMixin, admin.ModelAdmin):
    #inlines = [ImageInline]
    list_display = ('title', 'slug', 'created', 'updated', 'tags')

    def has_add_permission(self, request):
        return False


@admin.register(Draft)
class DraftAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'updated', 'tags')

    class Media:
            js = (
                'js/jquery.min.js',
                'js/jquery.form.min.js',
                'tinymce/tinymce.min.js',
                'js/admin/blog-draft.js',
              )



#@admin.register(Image)
#class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
#    pass