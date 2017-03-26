from decimal import Decimal

from django.db import models
from django.db.models.signals import post_save

from colour import Color
from image_cropping import ImageRatioField
from image_cropping.templatetags.cropping import cropped_thumbnail
from colorfield.fields import ColorField

from ..newsletter.models import List, SIGN_UP_TITLE
from ..cms.models import Page

OPACITY_CHOICES = [(i, i) for i in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]]


class GlobalSettings(models.Model):
    top_newsletter = models.ForeignKey(List, null=True, blank=True,
        default=1, on_delete=models.SET(None),
        help_text="Choose the Newsletter list to be used at the Top Bar form.")
    top_sign_up_title = models.CharField(max_length=255, default=SIGN_UP_TITLE,
         help_text="A short description to appear to the left side of the"
                   "newsletter form at the Top Bar.")

    main_page_bg_image_1 = models.ImageField(blank=True,
                                             upload_to='uploads/main_page/')
    main_page_bg_image_2 = models.ImageField(blank=True,
                                             upload_to='uploads/main_page/')
    main_page_bg_image_3 = models.ImageField(blank=True,
                                             upload_to='uploads/main_page/')
    main_page_bg_image_4 = models.ImageField(blank=True,
                                             upload_to='uploads/main_page/')
    main_page_bg_image_5 = models.ImageField(blank=True,
                                             upload_to='uploads/main_page/')
    main_page_bg_1 = ImageRatioField('main_page_bg_image_1', '1920x1200')
    main_page_bg_2 = ImageRatioField('main_page_bg_image_2', '1920x1200')
    main_page_bg_3 = ImageRatioField('main_page_bg_image_3', '1920x1200')
    main_page_bg_4 = ImageRatioField('main_page_bg_image_4', '1920x1200')
    main_page_bg_5 = ImageRatioField('main_page_bg_image_5', '1920x1200')

    foreground_color = ColorField(null=True, blank=True)
    logo_invert_color = models.BooleanField(default=False)
    menu_bar_background_color = ColorField(null=True, blank=True)
    menu_bar_opacity = models.FloatField(choices=OPACITY_CHOICES, null=True,
                                         blank=True)

    menu_1 = models.ForeignKey(Page, null=True, blank=True, related_name="menu_1_global_setting")
    menu_2 = models.ForeignKey(Page, null=True, blank=True, related_name="menu_2_global_setting")
    menu_3 = models.ForeignKey(Page, null=True, blank=True, related_name="menu_3_global_setting")
    menu_4 = models.ForeignKey(Page, null=True, blank=True, related_name="menu_4_global_setting")
    menu_5 = models.ForeignKey(Page, null=True, blank=True, related_name="menu_5_global_setting")

    javascript_codes = models.TextField(null=True, blank=True)

    _cache_object = None

    _menus_cache = None

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
        GlobalSettings._menus_cache = None

    @property
    def foreground_color_hsl(self):
        q = lambda x : Decimal(str(x)).quantize(Decimal(".01"))
        p = lambda x : "%s%%" % str(q(x))
        color = Color(self.foreground_color)
        # base_hsl = hsl(38, 24.5%, 60%);
        return "brightness(50%%) sepia(1) " \
               "hue-rotate(%sdeg) saturate(%s) brightness(%s);" % (
                                                         q(color.hue * 360) - 38,
                                                         p(100 + (color.saturation * 100) - 24.5),
                                                         p(100 + (color.luminance * 100) - 60))
    @property
    def menu_bar_background_color_rgba(self):
        if not self.menu_bar_background_color:
            return ""
        color = self.menu_bar_background_color.strip('#')
        rgb = "%s,%s,%s" % tuple(int(color[i:i+2], 16) for i in (0, 2 ,4))
        rgba = "rgba(%s,%s)" % (rgb, self.menu_bar_opacity)
        return rgba

    @property
    def main_page_background_images(self):
        base = "main_page_bg_%s"
        cr = lambda x : cropped_thumbnail({}, self, base % x)
        return [cr(i) for i in range(1, 6) if getattr(self, base % i, None)
                                              and cr(i)]

    @classmethod
    def get_pages(cls):
        return dict([(p.name, p)
                     for p in Page.objects.filter(sub_page_of=None)])

    @property
    def menus(self):
        if not self._menus_cache:
            default = ['artworks', 'shop/originals', 'about', 'blog',
                       'contact']
            pages = self.get_pages()
            self._menus_cache = []
            for i in range(len(default)):
                page = getattr(self, 'menu_%s' % (i + 1))
                if not page:
                    page = pages[default[i]]
                self._menus_cache.append(page)
            self._menus_cache.reverse()
        return self._menus_cache

post_save.connect(GlobalSettings.refresh_cache, GlobalSettings)
post_save.connect(GlobalSettings.refresh_cache, Page)
