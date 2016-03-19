from django.contrib import admin

from .models import GlobalSettings


@admin.register(GlobalSettings)
class GlobalSettingsAdmin(admin.ModelAdmin):

    list_display = ('title', 'top_newsletter', 'top_sign_up_title')

    class Media:
        js = (
            'js/admin/globalsettings.js',
        )


    def has_add_permission(self, request):
        return False

    def title(self, instance):
        return "Global Settings"