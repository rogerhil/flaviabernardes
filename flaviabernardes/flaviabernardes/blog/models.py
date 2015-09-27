from django.db import models
from django.contrib.sitemaps import ping_google

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
    image_banner = models.ImageField(blank=True, upload_to='uploads')
    image_listing = models.ImageField(blank=True, upload_to='uploads')
    listing = ImageRatioField('image_listing', '305x305')
    banner = ImageRatioField('image_banner', '1920x300')

    class Meta:
        abstract = True

    def __str__(self):
        return '%s: %s' % (self.__class__.__name__, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_view', None, {'slug': self.slug})


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
            banner=self.banner,
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

    def publish(self):
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
        post.listing = self.listing
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
            pass


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
