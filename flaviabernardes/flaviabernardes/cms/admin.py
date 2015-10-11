from django.contrib import admin
from django.utils.html import format_html

from image_cropping import ImageCroppingMixin

from .models import Page, PageDraft


class CmsObjectAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'js/jquery.min.js',
            'js/ajaxloader.js',
            'js/admin/cmsobjectlist.js',
        )
        css = {
            'all': ('css/ajaxloader.css',)
        }


    def has_add_permission(self, request):
        return False

    def modify(self, obj):
        return format_html('<a class="modify" href="javacript:;" model="%s" '
                           'draft-model="%s" obj_id="%s" view-url="%s">'
                           'Modify</a>' % (
                            obj.model_name, obj.draft_model_name, obj.id,
                            obj.get_absolute_url()))


class CmsDraftAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'js/jquery.min.js',
            'js/ajaxloader.js',
            'js/jquery.form.min.js',
            'tinymce/tinymce.min.js',
            'js/admin/cmsdraft.js',
        )
        css = {
            'all': ('css/ajaxloader.css',)
        }


@admin.register(Page)
class PageAdmin(ImageCroppingMixin, CmsObjectAdmin, admin.ModelAdmin):
    list_display = ('name', 'title', 'description', 'modify')

    def has_add_permission(self, request):
        return False

    class Media:
        js = (
            'js/jquery.min.js',
            'js/ajaxloader.js',
            'js/jquery.form.min.js',
            'tinymce/tinymce.min.js'
        )
        css = {
            'all': ('css/ajaxloader.css',)
        }


@admin.register(PageDraft)
class PageDraftAdmin(ImageCroppingMixin, CmsDraftAdmin, admin.ModelAdmin):
    list_display = ('name', 'title', 'description')
