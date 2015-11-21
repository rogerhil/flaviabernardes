from django.db import models
from django.core.urlresolvers import reverse, NoReverseMatch
from django.core.exceptions import ValidationError

from image_cropping import ImageRatioField

from .base import CmsObject, CmsDraft, DESCRIPTION_HELP_TEXT


class BasePage(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255,
                                   help_text=DESCRIPTION_HELP_TEXT)
    image_banner1 = models.ImageField(blank=True, upload_to='uploads')
    image_banner2 = models.ImageField(blank=True, upload_to='uploads')
    image_social = models.ImageField(blank=True, upload_to='uploads')
    banner1 = ImageRatioField('image_banner1', '1920x600')
    banner2 = ImageRatioField('image_banner2', '1920x1200')
    social = ImageRatioField('image_social', '1200x630')
    content1 = models.TextField(help_text="This content appears AFTER the FIRST banner", null=True, blank=True)
    content2 = models.TextField(help_text="This content appears BEFORE the SECOND banner", null=True, blank=True)
    content3 = models.TextField(help_text="This content appears AFTER the SECOND banner", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    footer = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.sub_page_of:
            return reverse('sub_page', kwargs=dict(slug=self.sub_page_of.name,
                                                   subslug=self.name,))
        elif self.is_newsletter_confirmation_page:
            return '/nl/%s/' % self.name
        else:
            try:
                return reverse(self.name)
            except NoReverseMatch:
                return '/%s/' % self.name

    @property
    def sub_pages(self):
        return Page.objects.filter(sub_page_of=self)

    def clean(self):
        if isinstance(self, PageDraft):
            if self.page is None:
                return
            page = self.page
            existing_name = page.name
        else:
            page = Page.objects.get(id=self.id)
            existing_name = page.name
        if self.sub_page_of is None and self.name != existing_name:
            raise ValidationError('Changing the "name" of a Main Page is not '
                                  'permitted. Please check the form below, '
                                  'specifically the field "name", that you '
                                  'have changed the value to "%s". Please '
                                  'change it back to the original value '
                                  '"%s".' % (self.name, existing_name))
        if page.sub_page_of is None and self.sub_page_of is not None:
            raise ValidationError('Making a Main Page become a Sub Page is '
                                  'not permitted. You have changed the field '
                                  '"Sub page of" with the value "%s". '
                                  'Please change it back to the original none '
                                  'value "---------" .' % self.sub_page_of)

    @property
    def is_newsletter_confirmation_page(self):
        if not hasattr(self, 'confirmation_newsletter_lists'):
            return False
        return self.confirmation_newsletter_lists.exists()


class Page(BasePage, models.Model, CmsObject):
    name = models.CharField(max_length=128, unique=True, editable=False)
    sub_page_of = models.ForeignKey('Page', null=True, blank=True)
    newsletter = models.ForeignKey('newsletter.List', default=1)

    def __str__(self):
        return self.name

    class cms:
        draft_class = 'cms.PageDraft'


class PageDraft(BasePage, CmsDraft):
    name = models.CharField(max_length=128, help_text="PLEASE PROVIDE A GOOD "
        "NAME FOR THIS PAGE IF YOU ARE CREATING A NEW ONE NOW, SO YOU WON'T "
        "NEED TO CHANGE IT ANYMORE IN THE FUTURE. THIS VALUE ALSO CORRESPONDS "
        "TO THE SLUG OF THE PAGE THAT WILL APPEAR IN THE URL "
        "(e.g.: /artworks/slug/) AND IT IS COMPLICATED TO CHANGE THIS VALUE "
        "AFTERWARDS. PLEASE AVOID CHANGING THIS VALUE BECAUSE IT CORRESPONDS "
        "TO THE SLUG OF THE SUB PAGE AND IT WILL AFFECT DISQUS COMMENTS "
        "REFERENCES AND GOOGLE INDEXING.")
    sub_page_of = models.ForeignKey('Page', null=True, blank=True,
                                    related_name='pages_sub')
    newsletter = models.ForeignKey('newsletter.List', default=1)
    page = models.ForeignKey(Page, null=True, blank=True, editable=False)

    class Meta:
        ordering = ('name', '-updated')

    class cms:
        draft_related_class = Page
        instance_name = 'page'
        context_object_name = 'page'
        template_preview = 'PAGE'
        publish_ignore = ['created']
