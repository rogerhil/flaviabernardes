from django.db import models
from django.db.models.signals import post_save

from ..newsletter.models import List, SIGN_UP_TITLE


class GlobalSettings(models.Model):
    top_newsletter = models.ForeignKey(List, null=True, blank=True,
        default=1, on_delete=models.SET(None),
        help_text="Choose the Newsletter list to be used at the Top Bar form.")
    top_sign_up_title = models.CharField(max_length=255, default=SIGN_UP_TITLE,
         help_text="A short description to appear to the left side of the"
                   "newsletter form at the Top Bar.")

    _cache_object = None

    def __str__(self):
        return "Global Settings"

    @classmethod
    def get(cls):
        if cls._cache_object is None:
            cls._cache_object = cls.objects.get(pk=1)
        return cls._cache_object

    @staticmethod
    def refresh_cache(sender, instance, **kwargs):
        GlobalSettings._cache_object = None


post_save.connect(GlobalSettings.refresh_cache, GlobalSettings)
