from django.contrib import admin
from django.utils.html import format_html
from django import forms

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

PAGE_FIELDS = ('name', 'sub_page_of', 'title', 'description', 'footer',
               'show_header', 'show_top_banner', 'show_footer', 'background_cover_image',
               'background_cover', 'foreground_color', 'box_background_color', 'box_opacity', 'box_square',
               'newsletter', 'show_newsletter_form_inline', 'show_newsletter_name_field',
               'newsletter_submit_button_color', 'newsletter_submit_button_opacity',
               'content1', 'content2', 'content3', 'content4',
               'image_banner1', 'banner1', 'image_banner2', 'banner2',
               'image_social', 'social')


class PageCommon(object):

    def get_form(self, request, obj=None, **kwargs):
        if isinstance(obj, PageDraft):
            page = obj.page
        else:
            page = obj
        # if page is not None and page.id and page.sub_page_of is None:
        #     exclude = ("name", "sub_page_of",)
        #     self.fields = tuple([f for f in self.fields if f not in exclude])
        # else:
        #     self.fields = PAGE_FIELDS
        self.fields = PAGE_FIELDS
        form = super(PageCommon, self).get_form(request, obj, **kwargs)
        return form


@admin.register(Page)
class PageAdmin(PageCommon, ImageCroppingMixin, CmsObjectAdmin,
                admin.ModelAdmin):
    fields = PAGE_FIELDS
    list_display = ('name', 'modify', 'title', 'description', 'created',
                    'updated', 'sub_page_of_display', 'newsletter_display',
                    'footer')
    list_filter = ('footer', 'sub_page_of', 'newsletter')

    def sub_page_of_display(self, instance):
        return str(instance.sub_page_of or "-")
    sub_page_of_display.short_description = 'Sub Page Of'

    def newsletter_display(self, instance):
        return str(instance.newsletter or "-")
    newsletter_display.short_description = 'Newsletter'

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
class PageDraftAdmin(PageCommon, ImageCroppingMixin, CmsDraftAdmin,
                     admin.ModelAdmin):
    fields = PageAdmin.fields
    list_display = ('name', 'title', 'description', 'created', 'updated',
                    'sub_page_of_display', 'newsletter_display', 'footer')
    list_filter = ('name', 'footer', 'sub_page_of', 'newsletter')

    def sub_page_of_display(self, instance):
        return str(instance.sub_page_of or "-")
    sub_page_of_display.short_description = 'Sub Page Of'

    def newsletter_display(self, instance):
        return str(instance.newsletter or "-")
    newsletter_display.short_description = 'Newsletter'

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(PageDraftAdmin, self).formfield_for_foreignkey(db_field,
                                                             request, **kwargs)
        if db_field.name == 'sub_page_of':
            field.queryset = field.queryset.filter(sub_page_of=None)
        return field
