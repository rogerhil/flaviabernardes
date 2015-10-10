import math

from django.conf import settings
from django.db import models
from django.contrib.sitemaps import ping_google
from django.core.mail import send_mail
from django.template.defaultfilters import Truncator, strip_tags

from image_cropping import ImageRatioField


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class BasePost(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Category)
    image_banner = models.ImageField(blank=True, upload_to=settings.UPLOAD_TO)
    image_banner2 = models.ImageField(blank=True, upload_to=settings.UPLOAD_TO)
    image_listing = models.ImageField(blank=True, upload_to=settings.UPLOAD_TO)
    listing = ImageRatioField('image_listing', '1920x600')
    listing_half = ImageRatioField('image_listing', '960x600')
    banner = ImageRatioField('image_banner', '1920x600')
    banner2 = ImageRatioField('image_banner2', '1920x600')

    class Meta:
        abstract = True

    def __str__(self):
        return '%s: %s' % (self.__class__.__name__, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_view', None, {'slug': self.slug})

    def listing_summary(self):
        title_lines = math.ceil(len(self.title) / 28)
        summary_lines = 4 - title_lines
        return Truncator(strip_tags(self.text)).chars(30 * summary_lines)



class Post(BasePost):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=64, unique=True)

    def new_draft(self):
        draft = Draft.objects.create(
            title=self.title,
            slug=self.slug,
            text=self.text,
            image_listing=self.image_listing,
            image_banner=self.image_banner,
            listing=self.listing,
            listing_half=self.listing_half,
            banner=self.banner,
            banner2=self.banner2,
            post=self
        )
        for tag in self.tags.all():
            draft.tags.add(tag)
        draft.save()
        return draft


class Draft(BasePost):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=64)
    post = models.ForeignKey(Post, null=True, blank=True, editable=False)

    class TooOldToPublish(Exception):
        pass

    def publish(self, publish_old=False):
        if not publish_old:
            if Draft.objects.filter(created__gt=self.created).count():
                raise Draft.TooOldToPublish('There are more recent drafts '
                                            'created than this one.')
        post = self.post
        new = False
        if post is None:
            new = True
            post = Post()
        post.title = self.title
        post.text = self.text
        post.slug = self.slug
        post.image_banner = self.image_banner
        post.image_listing = self.image_listing
        post.banner = self.banner
        post.banner2 = self.banner2
        post.listing = self.listing
        post.listing_half = self.listing_half
        if not new:
            for tag in self.tags.all():
                post.tags.add(tag)
        post.save()
        if new:
            self.post = post
            self.save()
            for tag in self.tags.all():
                post.tags.add(tag)
            post.save()
        try:
            ping_google()
        except Exception as err:
            subj = 'Flavia Bernardes Art: Error while trying to ping_google()'
            send_mail(subj, str(err), settings.SERVER_EMAIL,
                      [e[1] for e in settings.ADMINS])


class BaseImage(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(blank=True, upload_to='uploads')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


#class Image(BaseImage):
#    post = models.ForeignKey(Post, related_name='images')
#    ratio = ImageRatioField('image', '50x50')


#class DraftImage(BaseImage):
#    draft = models.ForeignKey(Draft)
#    ratio = ImageRatioField('image', '50x50')
