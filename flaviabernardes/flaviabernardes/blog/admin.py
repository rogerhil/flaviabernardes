from django.contrib import admin
from django.utils.html import format_html

from image_cropping import ImageCroppingMixin

from .models import Post, Draft, Category


#class ImageInline(admin.TabularInline):
#    model = Image


@admin.register(Post)
class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    #inlines = [ImageInline]
    list_display = ('title', 'slug', 'created', 'updated', 'modify')

    class Media:
        js = (
            'js/jquery.min.js',
            'js/ajaxloader.js',
            'js/admin/blog-post.js',
        )
        css = {
            'all': ('css/ajaxloader.css',)
        }


    def has_add_permission(self, request):
        return False

    def modify(self, obj):
        return format_html('<a class="modify" href="javacript:;" pid="%s">'
                           'New draft</a>' % obj.id)



@admin.register(Draft)
class DraftAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'post', 'slug', 'created', 'updated')

    class Media:
        js = (
            'js/jquery.min.js',
            'js/ajaxloader.js',
            'js/jquery.form.min.js',
            'tinymce/tinymce.min.js',
        'js/admin/blog-draft.js',
        )
        css = {
            'all': ('css/ajaxloader.css',)
        }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


#@admin.register(Image)
#class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
#    pass